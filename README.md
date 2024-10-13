# Gemini & Llama3 ChatBot Application

This is a Streamlit-based chatbot application that allows users to interact with two AI models: Google's Gemini Pro and Llama3. The user can select which model to use for generating a response to their questions.

## Features
- **Model Selection:** Choose between Gemini Pro (Google Generative AI) and Llama3 (Langchain Ollama) models.
- **Interactive Q&A:** Users can input their questions, and the selected model will provide responses.
- **Conversation History:** Maintains the conversation context between the user and the AI for a more coherent dialog.

## Setup Instructions

### Prerequisites
- Python 3.8 or later.
- Streamlit for the frontend.
- Environment variables set up using `.env` (API key for Google Gemini Pro).
- Required libraries:
  - `streamlit`
  - `google-generativeai`
  - `langchain-ollama`
  - `langchain-core`
  - `python-dotenv`

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/gemini-llama-chatbot.git
   cd gemini-llama-chatbot
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key for Gemini Pro:
   ```bash
   GOOGLE_API_KEY=<your-google-api-key>
   ```

### Running the Application

1. **Start the Streamlit App**
   ```bash
   streamlit run app.py
   ```

2. **Access the App**
   Open your browser and go to `http://localhost:8501`.

## Code Structure

- `app.py`: Main script containing the Streamlit app and logic for model selection and interaction.
- **Environment Variables**: API keys for Google Gemini are loaded from the `.env` file using `dotenv`.
- **Model Configuration**:
  - **Gemini Pro**: Utilizes `google.generativeai` to interact with the Gemini model.
  - **Llama3**: Uses `langchain_ollama` to set up and interact with the Llama3 model.
  
## Usage

1. **Select Model**: Choose either "Gemini Pro" or "Llama3" from the dropdown menu.
2. **Ask a Question**: Type your question in the input field and click the "Ask the question" button.
3. **View Response**: The chatbot's response from the selected model will be displayed below the input.

### Notes
- The conversation context is maintained across interactions, allowing for multi-turn conversations.
- Ensure the correct API key is configured for the Google Gemini model in the `.env` file.

## Dependencies

Here are the key dependencies used in this project:

- `streamlit`: For building the web interface.
- `google-generativeai`: For interacting with Google's Gemini Pro model.
- `langchain-ollama`: For working with the Llama3 model.
- `python-dotenv`: For loading environment variables.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

---

Feel free to modify the file based on your specific project details or preferences!
