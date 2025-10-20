import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get your Groq API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The uploaded PDF file (stream).
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_groq(prompt, max_tokens=500):
    """
    Sends a prompt to the Groq API and returns the response.
    
    Args:
        prompt (str): The text prompt for Groq.
        max_tokens (int): The maximum response length.
        
    Returns:
        str: The model's response.
    """
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",  # You can also use "mixtral-8x7b" or "gemma-7b"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.5
    )

    return response.choices[0].message.content
