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


def caption_generator(image_path):
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
    return response.choices[0].message.content


# rint(caption_generator("dog.jpg"))
def generate_story(caption, mood):

    mood_dictionary = {
        "fantasy": "A high-fantasy setting inspired by works like The Lord of the Rings or The Witcher, featuring epic quests, mythical creatures, ancient magic, and richly detailed worlds.",
        "science fiction": "A futuristic and imaginative setting with advanced technology, space exploration, alien encounters, and themes like artificial intelligence and intergalactic conflict.",
        "romance": "A heartfelt and emotional atmosphere centered on love and relationships, often with elements of passion, conflict, and ultimate connection.",
        "horror": "An eerie and suspenseful mood focused on fear, dread, and the supernatural, often with haunted settings, dangerous creatures, or psychological terror.",
        "mystery": "A puzzling and intrigue-driven tone where characters uncover secrets, solve crimes, or unravel conspiracies, with suspense and unexpected twists.",
        "adventure": "An exciting and action-packed mood that involves exploration, daring feats, and encounters with challenges or enemies in exotic locales.",
        "dystopian": "A bleak and oppressive setting characterized by societal collapse, authoritarian regimes, and the struggle for survival in a harsh world.",
        "historical": "A setting rooted in a specific historical period, with detailed attention to the culture, politics, and events of the time.",
        "comedy": "A lighthearted and humorous tone with witty dialogue, absurd situations, and a focus on creating laughter and joy.",
        "thriller": "A tense and gripping mood filled with suspense, high stakes, and fast-paced action, often involving espionage, crime, or danger.",
        "slice of life": "A realistic and grounded atmosphere focused on the everyday experiences, relationships, and emotions of the characters.",
        "dark fantasy": "A blend of fantasy elements with a grim and sinister tone, featuring morally ambiguous characters, dangerous magic, and foreboding settings.",
        "post-apocalyptic": "A setting where civilization has collapsed due to events like nuclear war, pandemics, or environmental disaster, with themes of survival and rebuilding.",
        "noir": "A gritty and moody atmosphere with themes of crime, moral ambiguity, and shadowy characters, often set in urban environments with a vintage or retro feel.",
    }
    # p

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

    return response.choices[0].message.content


# step open summarize the story


def summarize_story(story):
    # from openai import OpenAI
    # client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Summarize a story concisely in less than 1000 characters.\n\n# Steps\n\n1. **Identify Key Elements**: Extract the main plot, characters, and settings relevant to the story.\n2. **Simplify the Plot**: Rewrite the essential storyline by focusing on the crucial events and their outcomes.\n3. **Highlight Themes**: Mention any overriding themes or messages that are important to the story.\n4. **Ensure Clarity**: Use clear and concise language to convey the story’s essence without losing important details.\n\n# Output Format\n\n- The summary should be one continuous paragraph.\n- Ensure the total character count does not exceed 1000 characters including spaces and punctuation.\n\n# Example\n\n**Input:** A classic tale of a determined young hero who embarks on a journey to save their kingdom from a looming threat.\n**Output:** In a medieval kingdom, a courageous young hero sets out to defeat a terrifying dragon threatening their homeland. With bravery and wit, the hero navigates through treacherous terrains, battling mythical creatures and overcoming personal fears. Guided by an ancient prophecy and a loyal companion, the hero ultimately confronts and vanquishes the dragon, restoring peace to the realm and becoming a legendary figure in the kingdom's lore. Themes of bravery, friendship, and perseverance shine throughout this epic adventure.\n\n# Notes\n\n- Focus on conveying the story’s essence and main points within the character limit.\n- Avoid unimportant subplots or minor character details that don't affect the overall understanding of the story.",
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

    return response.choices[0].message.content

def generate_image(prompt):
    
    # client = OpenAI()

    response = client.images.generate(
    model="dall-e-3",
    prompt=f"{prompt}",
    size="1024x1024",
    quality="standard",
    response_format="b64_json",
    n=1,
    )

    # print(response)
    return response.data[0].b64_json

if __name__ == "__main__":
    # print(caption_generator("dog.jpg"))
    pass