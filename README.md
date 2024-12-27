# AI Interactive Story Co-Creation 📚✨

An interactive storytelling platform that combines human creativity with AI to generate unique stories based on images and emotions. This project uses OpenAI's GPT-4 for story generation and image analysis, creating a unique collaborative experience between humans and AI.

## 🌟 Features

- **Image Caption Generation**: Upload your images and get AI-generated descriptive captions
- **Caption Editing**: Fine-tune the AI-generated captions to match your vision
- **Genre-Based Storytelling**: Choose from various genres (Adventure, Dark fantasy, Science fiction, etc.)
- **Story Generation**: AI crafts unique stories combining your image captions with chosen genres
- **Image Generation**: Get AI-generated illustrations that complement your story
- **Feedback System**: Share your experience through our integrated feedback form

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/j1mb0o/gpteller
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your API key: `OPENAI_API_KEY='your-api-key'`

## 🎮 How to Use

1. **Start the Application**
   ```bash
   streamlit run app.py
   ```

2. **Upload an Image**
   - Choose an appropriate image (SFW only)
   - Supported formats: JPG, PNG
   - The AI will generate a caption for your image

3. **Customize Your Story**
   - Review and edit the generated caption if needed
   - Select a genre from the sidebar (Adventure, Fantasy, Sci-fi, etc.)
   - Generate your unique story and accompanying illustration

4. **Share Your Experience**
   - Provide feedback through our feedback form
   - Help us improve the story generator

## 🛠️ Technical Stack

- **Python**: Core programming language
- **Streamlit**: Web interface
- **OpenAI API**: 
  - GPT-4 for text generation and story creation
  - DALL-E for image generation
- **Environment Management**: python-dotenv for API key security

## ⚠️ Content Guidelines

- Only upload appropriate, Safe For Work (SFW) images
- Prohibited content includes:
  - Nudity or explicit content
  - Violence or gore
  - Abuse or harassment
  - Drug-related content
  - Other inappropriate material

## 🔒 Security Note

- Never commit your `.env` file
- Keep your API keys secure
- Review the `.gitignore` file to ensure sensitive data is excluded

## 📚 Examples

Check out our examples directory `example-results` to see sample stories and images generated.
