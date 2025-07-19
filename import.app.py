import streamlit as st
from translate import Translator

st.set_page_config(page_title="English to Urdu Translator", layout="centered")

st.title("🈯 English to Urdu Translator")
st.write("Translate any English sentence into Urdu.")

# Input
text = st.text_input("Enter English text")

if text:
    try:
        # Translator setup
        translator = Translator(to_lang="ur")
        translation = translator.translate(text)

        st.success("**Translation in Urdu:**")
        st.write(translation)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
import streamlit as st
from translate import Translator
st.set_page_config(page_title="English to Urdu Translator")
st.title("Your First Ever translator")
st.write("Translate any text in English to Urdu")
m = st.text_input("Please your text here in English...")
if m:
    try:
        n = Translator(to_lang="ur")
        u = n.translate(m)
        st.success("Your translation in urdu")
        st.write(u)
    except Exception as h:
        st.error(f"Something went wrong: {h}")



import streamlit as st
from translate import Translator

# Page settings
st.set_page_config(page_title="Text Translator", page_icon="🌐")

st.title("🌐 English ↔ Urdu Translator")
st.markdown("Translate between **English and Urdu** instantly.")

# Language selection
direction = st.selectbox("Choose translation direction:", ["English to Urdu", "Urdu to English"])

# Input text
text = st.text_area("✏️ Enter text to translate:")

# Buttons
col1, col2 = st.columns(2)
with col1:
    translate_btn = st.button("Translate")
with col2:
    clear_btn = st.button("Clear")

# Clear input
if clear_btn:
    st.experimental_rerun()

# Translation logic
if translate_btn:
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            if direction == "English to Urdu":
                translator = Translator(to_lang="ur")
            else:
                translator = Translator(to_lang="en")

            translation = translator.translate(text)
            st.success("✅ Translation Successful!")
            st.text_area("📘 Translated Text:", value=translation, height=150)
        except Exception as e:
            st.error(f"Something went wrong: {e}")



import streamlit as st
import speech_recognition as sr
import pyttsx3

st.set_page_config(page_title="🗣️ Voice Agent", layout="centered")
st.title("🗣️ Offline Voice Agent (No API Used)")

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.info("Listening... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Error connecting to speech service."

def process_command(command):
    # Basic logic from your previous knowledge
    command = command.lower()
    if "hello" in command:
        return "Hello! How can I help you?"
    elif "calculator" in command:
        return "You can open your calculator app for that."
    elif "translate" in command:
        return "I can help translate English to Urdu if you type it."
    else:
        return "Sorry, I don't know how to respond to that yet."

if st.button("🎤 Start Listening"):
    query = listen()
    st.write("You said:", query)
    response = process_command(query)
    st.success(response)
    speak(response)


import speech_recognition as sr
import pyttsx3
from transformers import pipeline

# Load lightweight Hugging Face model
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

# Text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and convert speech to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech service is down."

# Main loop
while True:
    query = listen()
    if "stop" in query.lower():
        speak("Goodbye!")
        break
    if query.strip() == "":
        continue
    response = qa_pipeline(query, max_length=100)[0]["generated_text"]
    print("🤖 Bot:", response)
    speak(response)
