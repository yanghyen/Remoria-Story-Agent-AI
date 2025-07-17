import json
from typing import Dict
import random
import ipdb

from tqdm import trange, tqdm

from ..utils.llm_output_check import parse_list
from ..base import register_tool, init_tool_instance
from ..prompts_en2 import rewriter_system, rawdata_refine_prompt, scene_amateur_system, scene_expert_system, scene_writer_system, scene_writer_prompt

def json_parse_scene(scene):
    scene = scene.strip("```json").strip("```")
    try:
        scene = json.loads(scene)
        if not isinstance(scene, dict):
            return False
        if scene.keys() != {"scene_number", "description"}:
            return False
    except json.decoder.JSONDecodeError:
        return False
    return True

@register_tool("qa_outline_story_writer")
class QAOutlineStoryWriter:

    def __init__(self,
                 cfg: Dict):
        self.cfg = cfg
        self.temperature = cfg.get("temperature", 1.0)
        self.max_conv_turns = cfg.get("max_conv_turns", 3)
        self.num_scene = cfg.get("num_scene", 4)
        self.llm_type = cfg.get("llm", "qwen")

    def refine_rawdata(self, params):
        rewriter = init_tool_instance({
            "tool": self.llm_type,
            "cfg": {
                "system_prompt": rewriter_system,
                "track_history": False
            }
        })

        rewriter_prompt = rawdata_refine_prompt.format(
            story_setting=params
        )

        full_text = rewriter.call(rewriter_prompt)

        return full_text

    def split_text_into_scenes(self, full_text):
        expert = init_tool_instance({
            "tool": self.llm_type,
            "cfg": {
                "system_prompt": scene_expert_system,
                "track_history": False
            }
        })

        amateur = init_tool_instance({
            "tool": self.llm_type,
            "cfg": {
                "system_prompt": scene_amateur_system,
                "track_history": False
            }
        })

        dialogue = []
        for turn in trange(self.max_conv_turns):
            dialogue_history = "\n".join(dialogue)

            question, success = amateur.call(
                f"Story setting: {full_text}\nDialogue history: \n{dialogue_history}\n",
                temperature=self.temperature
            )

            if not success:
                raise ValueError("Failed to get valid question from amateur")

            question = question.strip()
            if question == "Thank you for your help!":
                break
            dialogue.append(f"Amateur: {question}")

            answer, success = expert.call(
                f"Story setting: {full_text}\nQuestion: \n{question}\nAnswer: ",
                temperature=self.temperature
            )

            answer = answer.strip()
            dialogue.append(f"Expert: {answer}")

        writer = init_tool_instance({
            "tool": self.llm_type,
            "cfg": {
                "system_prompt": scene_writer_system,
                "track_history": False
            }
        })

        writer_prompt = scene_writer_prompt.format(
            story_setting=full_text,
            dialogue_history="\n".join(dialogue),
            num_scene=self.num_scene
        )

        scenes, success = writer.call(writer_prompt)

        return scenes

    

    def call(self, params):
        full_text = self.refine_rawdata(params)
        scenes = self.split_text_into_scenes(full_text)

        ipdb.set_trace()
        return scenes