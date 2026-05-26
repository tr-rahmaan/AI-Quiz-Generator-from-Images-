from gtts import gTTS
import streamlit as st
import io

text = "Hello, welcome to your first development"

speech = gTTS(text=text, lang='en', slow=False)

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)
audio_buffer.seek(0)

st.audio(audio_buffer)