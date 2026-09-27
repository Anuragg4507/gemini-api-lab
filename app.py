from google import genai
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Check API key
if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit()


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


# Ask user for question
question = input("Enter your question: ")


# Send request to Gemini
response = client.interactions.create(
    model="gemini-3.8-flash",
    input=question
)


# Print response
print("\nGemini Response:")
print(response.output_text)