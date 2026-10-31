# OpenAI API Integration using Python 🤖

A beginner-friendly Python project demonstrating how to integrate the OpenAI API and build an interactive AI chatbot.

## 🚀 Features

- OpenAI API integration using the official Python SDK.
- Environment variable management using python-dotenv.
- Interactive chatbot accepting user input.
- Custom system prompts to control model behaviour.
- Temperature experimentation to compare response creativity.
- Configurable response length using max_tokens.

## 🛠️ Technologies Used

- Python 3.12
- OpenAI Python SDK
- python-dotenv
- PyCharm

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/OpenAI-API-Integration.git
   ```

2. Navigate to the project directory:

   ```bash
   cd OpenAI-API-Integration
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and configure your API key:

   ```env
   OPENAI_API_KEY=your_api_key
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## 🧪 Experiments

Test different temperature values (0.0, 0.5, 1.0) to understand how they influence model responses.

## 🔐 Security

API keys are stored in environment variables and excluded from version control using `.gitignore`.

## 👩‍💻 Reference

https://roadmap.sh/projects/openai-api-python
