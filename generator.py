from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO

client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def decode_image(encoded_string, debug=False):
    decoded_image = base64.b64decode(encoded_string)
    if debug:

        with open("decoded_image.jpg", "wb") as image_file:
            image_file.write(base64.b64decode(encoded_string))

    image = Image.open(BytesIO(decoded_image))
    return image


def caption_generator(image_path, debug=False):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze an image to create a descriptive caption that accurately conveys the essence and details, using no more than 20 words. \n\n# Steps\n\n1. Examine the image thoroughly, identifying key elements, subjects, actions, and emotions.\n2. Determine the central theme or story conveyed by the image.\n3. Select the most notable and characteristic elements to include in the caption.\n4. Construct a concise, vibrant caption that visually describes the scene.\n\n# Output Format\n\n- A single text sentence with a maximum of 20 words.\n\n# Notes\n\n- Focus on clarity and vivid imagery in the wording.\n- The caption should reflect the most significant or interesting aspect of the image.",
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encode_image(image_path)}"
                        },
                    }
                ],
            },
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if debug:
        with open("tests/caption_generator.md", "w") as f:
            f.write(response.choices[0].message.content)
    return response.choices[0].message.content


def generate_story(caption, mood, debug=False):

    mood_dictionary = {
        "fantasy": "A high-fantasy setting inspired by works like The Lord of the Rings or The Witcher, featuring epic quests, mythical creatures, ancient magic, and richly detailed worlds.",
        "science fiction": "A futuristic and imaginative setting with advanced technology, space exploration, alien encounters, and themes like artificial intelligence and intergalactic conflict.",
        "romance": "A heartfelt and emotional atmosphere centered on love and relationships, often with elements of passion, conflict, and ultimate connection.",
        "horror": "An eerie and suspenseful mood focused on fear, dread, and the supernatural, often with haunted settings, dangerous creatures, or psychological terror.",
        "adventure": "An exciting and action-packed mood that involves exploration, daring feats, and encounters with challenges or enemies in exotic locales.",
        "dystopian": "A bleak and oppressive setting characterized by societal collapse, authoritarian regimes, and the struggle for survival in a harsh world.",
        "thriller": "A tense and gripping mood filled with suspense, high stakes, and fast-paced action, often involving espionage, crime, or danger.",
        "dark fantasy": "A blend of fantasy elements with a grim and sinister tone, featuring morally ambiguous characters, dangerous magic, and foreboding settings.",
        "post-apocalyptic": "A setting where civilization has collapsed due to events like nuclear war, pandemics, or environmental disaster, with themes of survival and rebuilding.",
    }

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": 'Create a short story based on a given caption and mood, formatted in Markdown.\n\nIncorporate elements from the caption and maintain the desired mood throughout the narrative.\n\n# Steps\n\n1. **Understand the Caption and Mood**: \n   - Identify key elements and themes from the provided caption.\n   - Recognize the specific mood that needs to be reflected in the story.\n\n2. **Story Development**:\n   - Develop a plot that is engaging and consistent with the themes from the caption.\n   - Integrate characters, setting, and conflict that align with the mood.\n\n3. **Conclusion**:\n   - Provide a resolution that enhances or concludes the mood and plot effectively.\n\n# Output Format\n\n- Use markdown for formatting the story.\n  - Begin with a suitable **Title** for the story.\n  - Use normal text for the body of the story.\n  - Employ **bold** or *italic* for emphasis where necessary.\n  - Utilize bullet points or numbered lists if required within the story.\n\n# Examples\n\n**Input**:\n- Caption: "A secret door within the library leads to a world of magic."\n- Mood: "Mysterious and whimsical"\n\n**Output**:\n**Title**: The Enchanted Passage\n\nIn the dim glow of the library\'s ancient lamps, [character name] stumbled upon an unassuming wooden panel nestled between dusty tomes. **Curious** and somewhat skeptical, [he/she/they] pressed against the panel, feeling a *soft click* under [his/her/their] fingertips. The room shimmered briefly, and before [him/her/them] unfolded a world bathed in luminescent colors and whispered secrets—a realm only accessible through that **secret door**, where every shadow seemed to hold a story, and the air tingled with anticipation of magic yet to be revealed...',
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Caption: {caption} \n Mood: {mood_dictionary[mood]} ",
                    }
                ],
            },
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    if debug:
        with open("tests/generate_story.md", "w") as f:
            f.write(response.choices[0].message.content)

    return response.choices[0].message.content


# step open summarize the story


def summarize_story(story, debug=False):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Summarize a story into a concise and vivid description of less than 1000 characters, focusing on a single scene that would be most suitable for generating an image. Ensure the summary evokes visual imagery without including any text elements that identify characters or settings explicitly.\n\n# Steps\n\n1. **Identify Key Scenes**: Read the story and identify crucial scenes that are rich in visual detail and pivotal to the narrative.\n2. **Select One Scene**: Choose one scene that encapsulates significant action, emotion, or a transformative moment.\n3. **Describe the Scene**: Write a vivid description of this scene, focusing on elements that can be visually depicted, such as actions, emotions, settings, and dynamics.\n4. **Ensure Clarity and Brevity**: Keep the description under 1000 charachters, ensuring it is clear and easy to visualize.\n\n# Output Format\n\n- A descriptive summary in paragraph form, less than 1000 characters.\n- The output must exclude any textual identifiers such as character names, dialogue, or specific place names.\n\n# Examples\n\n**Example 1:**\n\n**Input:** \nA fairy tale about a princess who embarks on a dangerous journey to save her kingdom.\n\n**Output:** \nIn the heart of the enchanted forest, a gleaming castle rises under a twilight sky. Near the edge of a cascading waterfall, the princess, cloaked in emerald-green, stands defiant against the swirling mist. Her hand grips the hilt of a shimmering sword, its silver blade catching the last rays of the setting sun, while ethereal creatures hover silently, watching her every move. \n\n(The actual output should contain similar vivid imagery, yet respect the 1000-word limit and avoid explicit character or place names.)\n\n# Notes\n\n- Focus on visual-rich segments of the story for better image generation.\n- Avoid giving too much background information; instead, bring the scene to life.\n- Ensure no explicit identifiers like names or dialogues are included in the description.",
                    }
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": f"{story}"}]},
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if debug:
        with open("tests/summarize_story.md", "w") as f:
            f.write(response.choices[0].message.content)
    return response.choices[0].message.content


def generate_image(prompt, debug=False):

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{prompt}\n\n DO NOT INCLUDE ANY TEXT IN THE IMAGE. JUST THE IMAGE.",
        size="1024x1024",
        quality="standard",
        response_format="b64_json",
        n=1,
    )
    if debug:
        with open("tests/decoded_image.jpg", "wb") as image_file:
            image_file.write(base64.b64decode(response.data[0].b64_json))
    # print(response)
    return response.data[0].b64_json


if __name__ == "__main__":
    # print(caption_generator("dog.jpg"))
    print("Generating Caption")
    caption = caption_generator("dog.jpg",debug=True)
    print("Generating Story")
    story = generate_story(caption,mood="adventure",debug=True)
    print("Summarizing Story")
    summary = summarize_story(story,debug=True)
    print("Generating Image")
    # summary = """Dash, a spirited golden retriever, revels in the sunlit sands of Crestview Beach. While exploring, he uncovers a hidden map, igniting a quest to find rumored treasures in a secret cove. Emboldened, Dash races forward, overcoming obstacles: leaping over a crab blockade and skillfully slipping across a slick log bridge amidst rising tides. Reaching the cove, he encounters Finn, a clever dolphin guarding the treasure. Finn poses a riddle, "What runs but never walks, has a mouth but never talks?" Dash triumphantly answers, "A river!" Impressed, Finn reveals a chest brimming with sparkling seashells and stones. Victorious, Dash returns home, the sunset casting long shadows behind him. His heart swells with joy as the waves and wind celebrate his daring feats, leaving a trail of paw prints and a newfound tale of courage, balance, and wit at Crestview Beach. Themes of adventure, resourcefulness, and bravery pervade this joyful escapade."""
    image = generate_image(summary, debug=True)
