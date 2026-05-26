import streamlit as st
from api_calling import note_generator, generated_audio, quiz_genarator
from PIL import Image

st.set_page_config(page_title="AI Quiz Generator", page_icon="🧠", layout="wide")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4F46E5;'>🧠 Quiz Generator from Notes</h1>
    <p style='text-align: center; color: gray;'>Upload images, generate notes, audio, and quizzes using AI</p>
""", unsafe_allow_html=True)

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Control Panel")

    images = st.file_uploader(
        "Upload up to 3 images",
        type=['jpg', 'png', 'jpeg'],
        accept_multiple_files=True
    )

    pil_image = []

    if images:
        if len(images) > 3:
            st.error("You can upload maximum of 3 images")
        else:
            st.success(f"{len(images)} image(s) uploaded")

        st.subheader("Preview")
        cols = st.columns(len(images))

        for i, img in enumerate(images):
            pil_img = Image.open(img)
            pil_image.append(pil_img)

            with cols[i]:
                st.image(img, use_container_width=True, caption=f"Image {i+1}")

    seleected_option = st.selectbox(
        "Select Quiz Difficulty",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    if seleected_option:
        st.info(f"Selected difficulty: {seleected_option}")
    else:
        st.warning("Please select a difficulty")

    st.divider()
    pressed = st.button("🚀 Generate AI Quiz", type="primary", use_container_width=True)

# Main execution
if pressed:
    if not images:
        st.error("Please upload at least one image")
    elif not seleected_option:
        st.error("Please select difficulty level")
    else:
        # NOTE GENERATION
        with st.container():
            st.markdown("## 📘 Generated Notes")
            with st.spinner("Analyzing images and generating notes..."):
                generated_text = note_generator(pil_image)
                st.success("Notes generated successfully!")
                st.markdown(generated_text)

        st.divider()

        # AUDIO GENERATION
        with st.container():
            st.markdown("## 🔊 Audio Version")
            with st.spinner("Converting notes to audio..."):
                cleaned_text = generated_text.replace("#", "").replace("*", "").replace("-", "").replace("`", "")
                audio_transcription = generated_audio(cleaned_text)
                st.audio(audio_transcription)
                st.success("Audio ready!")

        st.divider()

        # QUIZ GENERATION
        with st.container():
            st.markdown("## 📝 Quiz Section")
            st.info(f"Generating a {seleected_option} level quiz...")

            with st.spinner("Creating quiz questions..."):
                quiz_show = quiz_genarator(pil_image, seleected_option)
                st.markdown(quiz_show)

        st.balloons()