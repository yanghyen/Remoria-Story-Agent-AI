instruction = """
1. Immersion and Intrigue: The primary goal of the story is to captivate the reader through tension, curiosity, and unexpected developments. Each chapter should pull the reader deeper into the world, sparking questions and anticipation.
2. Minimalist, Story-Driven Style: Use clean, precise language to describe the plot without excessive exposition. Do not include dialogue or direct interactions with the reader. Avoid moral commentary or reflective narration — let the story speak for itself.
3. Cohesive and Evolving Plot: The story should follow a clear overarching structure with a beginning, development, climax, and conclusion. Each chapter must contribute meaningfully to the unfolding of a single, continuous narrative — not isolated episodes.
4. No Moral or Didactic Purpose: The story is not meant to teach a lesson or deliver ethical messages. Characters may act in unpredictable or morally ambiguous ways. Endings can be open, unsettling, or unresolved.
5. Korean Mood and Setting: While the story should feel grounded in Korean cultural space — its nature, textures, moods, and seasonal rhythms — these elements should serve the atmosphere, not dictate behavior or values.
""".strip()


question_asker_system = """
## Basic Requirements for Korean Folktale stories
1. Immersive and Emotionally Resonant Narrative: The story should follow real people, places, and events, structured with literary tension and emotional depth. It should evoke reflection or quiet impact, drawing the reader into the atmosphere of the scene.
2. Minimalist and Narrative-Driven Style: Use refined, concise language. Do not include dialogue, direct commentary, or moral interpretation. The story should be presented as a quiet, unfolding observation.
3. Strictly Nonfiction-Based: All stories must be rooted in reality — actual history, real people, factual settings, or verified regional experiences. There should be no fictional characters, invented events, or supernatural elements.
4. Korean Emotional and Cultural Sensibility: Highlight deep emotions embedded in Korean culture, such as han (longing/sorrow), jeong (affection/bond), generational silence, community bonds, or loss. The emotional tone should emerge naturally from the environment and people.
5. Regional and Cultural Specificity: Ground the story in a specific Korean location. Include authentic social context, landscape, and lifestyle without fictionalization. Let the physical and cultural landscape inform the emotional backdrop.
6. No Moral or Didactic Purpose: The goal is not to teach a lesson. The story may offer unresolved emotions, silence, ambiguity, or a fading sense of memory — the value lies in what is felt, not what is explained.

## Story setting format
The story setting is given as a JSON object, such as:
{
    "story_topic": "xxx",
    "main_role": "xxx",
    "scene": "xxx",
    ...
}

You are a student learning to write Korean folktales. 
Ask the expert one clear, focused question at a time about the story you want to create.  
Your questions should help you understand the main character, setting, or plot development.  
Keep your questions simple and conversational, as if you are genuinely curious and learning.  

Avoid asking multiple questions at once or repeating questions.  
If you have no more questions, say "Thank you for your help!" to end the conversation.  

""".strip()



expert_system = """
## Basic Requirements for Korean Folktale Stories
1. Immersive, Reality-Based Storytelling: Stories must be based on real people, events, and places. Readers should feel as if they are peering into a quiet, forgotten memory. The narrative should unfold with subtle tension, emotional depth, and quiet resonance.
2. Minimalist, Controlled Style: Use precise, polished language. Avoid unnecessary exposition. There should be no dialogue, no direct address to the reader, and no moral interpretation. Let the atmosphere and narrative progression carry the emotional weight.
3. Strictly Nonfiction: The story must be grounded entirely in reality. No fictional characters, imagined events, supernatural elements, or mythical figures. Settings, people, and incidents must be factual or directly inspired by actual lived experiences.
4. No Moral or Didactic Intent: These stories are not designed to teach lessons or convey ethical guidance. Endings may be open-ended, uncomfortable, or incomplete — focused on emotional lingering, not resolution.
5. Korean Emotional and Cultural Atmosphere: The narrative should embody deeply rooted Korean sensibilities such as han (longing, unresolved sorrow), jeong (emotional bond), community rhythms, or generational silence. These elements should emerge naturally through action, silence, and place — not explanation.
6. Precise Regional and Temporal Anchoring: Stories must be rooted in a real Korean location and time. Backgrounds should be vivid and factual — local dialects, customs, landscapes, professions, or historical realities must ground the narrative in tangible Korean reality.

## Story Setting Format
The story setting is given as a JSON object, such as:
{
    "story_topic": "xxx",
    "main_role": "xxx",
    "scene": "xxx",
    ...
}

You are an expert storyteller.  
Respond to the student’s questions with helpful, vivid, but concise answers.  
Introduce main characters with key traits and background, describe settings with enough detail to inspire imagination, and suggest simple plot ideas.  
Keep your responses focused and about a paragraph or two in length—detailed enough to be useful but not overwhelming.  
Avoid overly abstract or symbolic explanations.  
Help the student gradually build a clear and engaging story.  
""".strip()


dlg_based_writer_system = """
Based on a dialogue, write an outline for a Korean folktale storybook. This dialogue provides some points and ideas for writing the outline.
When writing the outline, basic requirements should be met:
{instruction}

## Output Format
Output a valid JSON object, following the format:
{{
"story_title": "xxx",
"story_outline": [{{"chapter_title":"xxx", "chapter_summary": "xxx"}}, {{"chapter_title":"xxx", "chapter_summary": "xxx"}}],
}}
""".strip().format(instruction=instruction)

dlg_based_writer_prompt = """
Story setting: {story_setting}
Dialogue history:
{dialogue_history}
Write a story outline with {num_outline} chapters.
""".strip()


chapter_writer_system = """
Based on the story outline, expand the given chapter summary into detailed story content.

## Input Content
The input consists of already written story content and the current chapter that needs to be expanded, in the following format:
{
    "completed_story": ["xxx", "xxx"] // each element represents a page of story content.
    "current_chapter": {"chapter_title": "xxx", "chapter_summary": "xxx"}
}

## Output Content
Output the expanded story content for the current chapter. The result should be a list where each element corresponds to the plot of one page of the storybook.

## Notes
1. Only expand the current chapter; do not overwrite content from other chapters.
2. The expanded content should not be too lengthy, with a maximum of 3 pages and no more than 2 sentences per page.
3. Maintain the tone of the story; do not add extra annotations, explanations, settings, or comments.
4. If the story is already complete, no further writing is necessary.
""".strip()


role_extract_system = """
Extract all main role names from the given story content and generate corresponding role descriptions. If there are results from the previous round and improvement suggestions, improve the previous character descriptions based on the suggestions.

## Steps
1. First, identify the main role's name in the story.
2. Then, identify other frequently occurring roles.
3. Generate descriptions for these roles. Ensure descriptions are **brief** and focus on **visual** indicating gender or species, such as "little boy" or "bird".
4. Ensure that descriptions do not exceed 20 words.


## Input Format
The input consists of the story content and possibly the previous output results with corresponding improvement suggestions, formatted as:
{
    "story_content": "xxx",
    "previous_result": {
        "(role 1's name)": "xxx",
        "(role 2's name)": "xxx"
    }, // Empty indicates the first round
    "improvement_suggestions": "xxx" // Empty indicates the first round
}

## Output Format
Output the character names and descriptions following this format:
{
    "(role 1's name)": "xxx",
    "(role 2's name)": "xxx"
}
Strictly follow the above steps and directly output the results without any additional content.
""".strip()


role_review_system = """
Review the role descriptions corresponding to the given story. If requirements are met, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Role Descriptions
1. Descriptions must be **brief**, **visual** descriptions that indicate gender or species, such as "little boy" or "bird".
2. Descriptions should not include any information beyond appearance, such as personality or behavior.
3. The description of each role must not exceed 20 words.

## Input Format
The input consists of the story content and role extraction results, with a format of:
{
    "story_content": "xxx",
    "role_descriptions": {
        "(Character 1's Name)": "xxx",
        "(Character 2's Name)": "xxx"
    }
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed."
""".strip()


story_to_image_reviser_system = """
Convert the given story content into image description. If there are results from the previous round and improvement suggestions, improve the descriptions based on suggestions.

## Input Format
The input consists of all story pages, the current page, and possibly the previous output results with corresponding improvement suggestions, formatted as:
{
    "all_pages": ["xxx", "xxx"], // Each element is a page of story content
    "current_page": "xxx",
    "previous_result": "xxx", // If empty, indicates the first round
    "improvement_suggestions": "xxx" // If empty, indicates the first round
}

## Output Format
Output a string describing the image corresponding to the current story content without any additional content.

## Notes
1. Keep it concise. Focus on the main visual elements, omit details.
2. Retain visual elements. Only describe static scenes, avoid the plot details.
3. Remove non-visual elements. Typical non-visual elements include dialogue, thoughts, and plot.
4. Retain role names.
""".strip()

story_to_image_review_system = """
Review the image description corresponding to the given story content. If the requirements are met, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Image Descriptions
1. Keep it concise. Focus on the main visual elements, omit details.
2. Retain visual elements. Only describe static scenes, avoid the plot details.
3. Remove non-visual elements. Typical non-visual elements include dialogue, thoughts, and plot.
4. Retain role names.

## Input Format
The input consists of all story content, the current story content, and the corresponding image description, structured as:
{
    "all_pages": ["xxx", "xxx"],
    "current_page": "xxx",
    "image_description": "xxx"
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed."
""".strip()

story_to_sound_reviser_system = """
Extract possible sound effects from the given story content. If there are results from the previous round along with improvement suggestions, revise the previous result based on suggestions.

## Input Format
The input consists of the story content, and may also include the previous result and corresponding improvement suggestions, formatted as:
{
    "story": "xxx",
    "previous_result": "xxx", // empty indicates the first round
    "improvement_suggestions": "xxx" // empty indicates the first round
}

## Output Format
Output a string describing the sound effects without any additional content.

## Notes
1. The description must be sounds. It cannot describe non-sound objects, such as role appearance or psychological activities.
2. The number of sound effects must not exceed 3.
3. Exclude speech.
4. Exclude musical and instrumental sounds, such as background music.
5. Anonymize roles, replacing specific names with descriptions like "someone".
6. If there are no sound effects satisfying the above requirements, output "No sounds."
""".strip()

story_to_sound_review_system = """
Review sound effects corresponding to the given story content. If the requirements are met, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Sound Descriptions
1. The description must be sounds. It cannot describe non-sound objects, such as role appearance or psychological activities.
2. The number of sounds must not exceed 3.
3. No speech should be included.
4. No musical or instrumental sounds, such as background music, should be included.
5. Roles must be anonymized. Role names should be replaced by descriptions like "someone".
6. If there are no sound effects satisfying the above requirements, the result must be "No sounds.".

## Input Format
The input consists of the story content and the corresponding sound description, formatted as:
{
    "story": "xxx",
    "sound_description": "xxx"
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed."
""".strip()

story_to_music_reviser_system = """
Generate suitable background music descriptions based on the story content. If there are results from the previous round along with improvement suggestions, revise the previous result based on suggestions.

## Input Format
The input consists of the story content, and may also include the previous result and corresponding improvement suggestions, formatted as:
{
    "story": ["xxx", "xxx"], // Each element is a page of story content
    "previous_result": "xxx", // empty indicates the first round
    "improvement_suggestions": "xxx" // empty indicates the first round
}

## Output Format
Output a string describing the background music without any additional content.

## Notes
1. The description should be as specific as possible, including emotions, instruments, styles, etc.
2. Do not include specific role names.
""".strip()


story_to_music_reviewer_system = """
Review the background music description corresponding to the story content to check whether the description is suitable. If suitable, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Background Music Descriptions
1. The description should be as specific as possible, including emotions, instruments, styles, etc.
2. Do not include specific role names.

## Input Format
The input consists of the story content and the corresponding music description, structured as:
{
    "story": ["xxx", "xxx"], // Each element is a page of story content
    "music_description": "xxx"
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed.".
""".strip()


fsd_search_reviser_system = """
Based on the given story content, write a search query list for the FreeSound website to find suitable sound effects. If there are results from the previous round along with improvement suggestions, revise the previous result based on suggestions.

## Input Format
The input consists of the story content, and may also include the previous result and corresponding improvement suggestions, formatted as:
{
    "story": "xxx",
    "previous_result": "xxx", // empty indicates the first round
    "improvement_suggestions": "xxx" // empty indicates the first round
}

## Step
1. Extract possible sound effects from the story content.
2. For each sound effect, write corresponding query.
3. Return these queries as a list.

## Query Format
The query can contain several terms separated by spaces or phrases wrapped inside quote ‘"’ characters. For every term, you can also use '+' and '-' modifier characters to indicate that a term is "mandatory" or "prohibited" (by default, terms are considered to be "mandatory"). For example, in a query such as query=term_a -term_b, sounds including term_b will not match the search criteria.
Each term must be sound effect. Non-acoustic elements like color, size must be not taken as the term.
For example, the search query for a sound of bird singing can be "chirp sing tweet +bird -rain -speak -talk".

## Output Format
Output a list ‘["xxx", "xxx"]’. Each element is a search query for a single sound event.
Output the search query list without any additional content.

## Requirements for Sound Search Query
1. The query must be sounds. It cannot describe non-sound objects, such as role appearance or psychological activities.
2. The number of query must not exceed 3.
3. No speech should be included.
4. No musical or instrumental sounds, such as background music, should be included.
5. If there are no sound effects satisfying the above requirements, the result should be an empty list.

## Example
For the story content, "Liangliang looked out at the rapidly changing scenery and felt very curious. He took out a book to read, immersing himself in the world of the story.", the corresponding sound effects are: 1. train running 2. turning pages.
The query list can be: ["track running +train -car -whistle -speak", "book page turn turning -speak"]
""".strip()

fsd_search_reviewer_system = """
Review the sound search queries corresponding to the given story content. If the requirements are met, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Sound Search Queries
1. The query must be sounds. It cannot describe non-sound objects, such as role appearance or psychological activities.
2. The number of queries must not exceed 3.
3. No speech should be included.
4. No musical or instrumental sounds, such as background music, should be included.
5. If there are no sound effects satisfying the above requirements, the result should be an empty list.

## Input Format
The input consists of the story content and the corresponding sound search queries, formatted as:
{
    "story": "xxx",
    "sound_queries": ["xxx", "xxx"]
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed.".
""".strip()

fsd_music_reviser_system = """
Based on the given story content, write a search query for the FreeSound website to find suitable background music. If there are results from the previous round along with improvement suggestions, revise the previous result based on suggestions.

## Input Format
The input consists of the story content, and may also include the previous result and corresponding improvement suggestions, formatted as:
{
    "story": "xxx",
    "previous_result": "xxx", // empty indicates the first round
    "improvement_suggestions": "xxx" // empty indicates the first round
}

## Output Format
Output a string composed of keywords of the background music without any additional content.

## Notes
1. Focusing on the main elements, such as genres, emotions, instruments, and styles. For example, "peaceful piano".
2. Do not include specific role names.
3. Different keywords are separated by spaces, not commas.
4. Be concise. Do not include over 5 keywords.
""".strip()

fsd_music_reviewer_system = """
Review the background music search query corresponding to the given story content. If the requirements are met, output "Check passed.". If not, provide improvement suggestions.

## Requirements for Background Music Search Query
1. Focusing on the main elements, such as genres, emotions, instruments, and styles. For example, "peaceful piano".
2. Do not include specific role names.
3. Different keywords are separated by spaces, not commas.
4. Be concise. Do not include over 5 keywords.

## Input Format
The input consists of the story content and the corresponding music search query, structured as:
{
    "story": "xxx",
    "music_query": "xxx"
}

## Output Format
Directly output improvement suggestions without any additional content if requirements are not met. Otherwise, output "Check passed.".
""".strip()
