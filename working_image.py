import streamlit as st
from api_calling import note_generator


from google import genai
from dotenv import load_dotenv
import os

from PIL import Image

# loading the stevn

load_dotenv()

my_api_key=os.getenv("GEMINI_API_KEY")

#initializing the client

client=genai.Client(api_key=my_api_key)

images = st.file_uploader(
    "Upload images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)



if images:

    pil_image=[]
    for img in images:
        pil_img=Image.open(img)
        pil_image.append(pil_img)


    prompt="""Summarize the images as text format at most 100 words,
    Also make sure to do necessary markdown"""
    response=client.models.generate_content( 
        model="gemini-3-flash-preview",
        contents=[pil_image,prompt]
    )

    st.markdown(response.text)
     
  