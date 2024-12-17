import streamlit as st
import os
import time
from dotenv import load_dotenv
from PIL import Image
from generator import caption_generator, generate_story, generate_image, decode_image

# Load environment variables
load_dotenv()

# Debug placeholder image URL
DEBUG_IMAGE_URL = "https://picsum.photos/1024"

# Set page configuration
st.set_page_config(
    page_title="AI Story Co-Creation",
    page_icon="📚",
    layout="centered"
)

def main():
    # Title and description
    st.title("📚 AI Interactive Story Co-Creation")
    st.markdown("Upload an image and let's create a story together!")

    # Sidebar for mood selection
    with st.sidebar:
        st.header("Story Settings")
        mood = st.selectbox(
            "Choose the mood for your story:",
            [
                "Adventure",
                "Dark fantasy",
                "Dystopian",
                "Fantasy",
                "Science fiction",
                "Romance",
                "Horror",
                "Thriller",
                "Post-apocalyptic"
            ]
        )
        
        # Debug mode toggle
        debug_mode = st.checkbox("Debug Mode (Skip API calls)", value=True)

    # Image upload section
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Generate caption button
        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                try:
                    if debug_mode:
                        time.sleep(2)  # Simulate API call
                        caption = "Debug mode: This is a sample caption for the uploaded image."
                    else:
                        image_path = f"temp_{uploaded_file.name}"
                        image.save(image_path)
                        caption = caption_generator(image_path)
                        os.remove(image_path)
                    
                    if caption:
                        st.session_state['caption'] = caption
                        st.success("Caption generated!")
                except Exception as e:
                    st.error(f"Error generating caption: {str(e)}")

    # Caption editing section
    if 'caption' in st.session_state:
        st.markdown("### Edit Caption")
        edited_caption = st.text_area(
            "You can edit the caption before generating the story:",
            value=st.session_state['caption'],
            height=100
        )
        st.session_state['caption'] = edited_caption

        # Story generation
        if st.button("Generate Story"):
            with st.spinner("Creating your story and image..."):
                try:
                    if debug_mode:
                        time.sleep(3)  # Simulate API call
                        story = f"Debug mode: This is a sample story based on the caption: '{edited_caption}' with {mood} mood."
                    else:
                        story = generate_story(edited_caption, mood.lower())
                    
                    if story:
                        st.session_state['story'] = story
                        st.markdown("### Your Story")
                        st.write(story)
                        
                        # Generate and display story image
                        # with st.spinner("Generating story image..."):
                        if debug_mode:
                            time.sleep(2)  # Simulate API call
                            st.info("Debug mode: Using placeholder image")
                            st.image(DEBUG_IMAGE_URL, caption="Debug Story Illustration", use_container_width=True)
                        else:
                            image_url = generate_image(story)
                            image = decode_image(image_url)
                            if image_url:
                                st.image(image=image, caption="Story Illustration", use_container_width=True)
                except Exception as e:
                    st.error(f"Error generating story: {str(e)}")

        # Feedback section
            st.markdown("### Share Your Feedback")
            st.markdown("""
                We'd love to hear your thoughts on the Story Generator! 
                Please take a moment to fill out our feedback form.
            """)
            st.markdown("[📝 Share Your Feedback](https://forms.gle/YourGoogleFormLink)", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 