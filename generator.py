from openai import OpenAI
import base64

client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


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
              "text": "Create a short story based on a given caption and mood, formatted in Markdown.\n\nIncorporate elements from the caption and maintain the desired mood throughout the narrative.\n\n# Steps\n\n1. **Understand the Caption and Mood**: \n   - Identify key elements and themes from the provided caption.\n   - Recognize the specific mood that needs to be reflected in the story.\n\n2. **Story Development**:\n   - Develop a plot that is engaging and consistent with the themes from the caption.\n   - Integrate characters, setting, and conflict that align with the mood.\n\n3. **Conclusion**:\n   - Provide a resolution that enhances or concludes the mood and plot effectively.\n\n# Output Format\n\n- Use markdown for formatting the story.\n  - Begin with a suitable **Title** for the story.\n  - Use normal text for the body of the story.\n  - Employ **bold** or *italic* for emphasis where necessary.\n  - Utilize bullet points or numbered lists if required within the story.\n\n# Examples\n\n**Input**:\n- Caption: \"A secret door within the library leads to a world of magic.\"\n- Mood: \"Mysterious and whimsical\"\n\n**Output**:\n**Title**: The Enchanted Passage\n\nIn the dim glow of the library's ancient lamps, [character name] stumbled upon an unassuming wooden panel nestled between dusty tomes. **Curious** and somewhat skeptical, [he/she/they] pressed against the panel, feeling a *soft click* under [his/her/their] fingertips. The room shimmered briefly, and before [him/her/them] unfolded a world bathed in luminescent colors and whispered secrets—a realm only accessible through that **secret door**, where every shadow seemed to hold a story, and the air tingled with anticipation of magic yet to be revealed..."
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": f"Caption: {caption} \n Mood: {mood_dictionary[mood]} "
            }
          ]
        }
    ],
    response_format={
      "type": "text"
        },
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content




if __name__ == "__main__":
    # print(caption_generator("dog.jpg"))
    pass
