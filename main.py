import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Function to generate AI responses
def generate_response(user_input, temperature=0.7):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and friendly AI assistant."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=temperature,
        max_tokens=300
    )

    return response.choices[0].message.content


# Interactive chatbot
print("Welcome to the OpenAI Chatbot!")
print("Type 'exit' to quit.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    answer = generate_response(user_input)

    print("\nAI:", answer)