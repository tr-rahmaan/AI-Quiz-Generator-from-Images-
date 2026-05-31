from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS
from PIL import Image

# loading the stevn

load_dotenv()

my_api_key=os.getenv("GEMINI_API_KEY")

#initializing the client

client=genai.Client(api_key=my_api_key)

#note generator 

def note_generator(images):
    prompt="""Summarize the images as text format at most 100 words,
    Also make sure to do necessary markdown"""
    response=client.models.generate_content( 
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text 


def generated_audio(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    
    return audio_buffer

def quiz_genarator(images,difficulty):
    prompt=f"""Summarize the images and make quize on the {difficulty},
    make sure to do markdown
    Generate 3 quiz"""
    
    response=client.models.generate_content( 
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text 