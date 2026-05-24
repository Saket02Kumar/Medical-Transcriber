from graph import app
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()

print("Starting Medical Transcriber. Speak into the microphone after the welcome prompt.")
engine.say("Hey doctor how can i help?")
engine.runAndWait()

thread = {"configurable": {"thread_id": "1"}}
initial_state = {
    "messages": [HumanMessage(content="start")],
    "spoken_messages": [],
    "recorded_text": "",
    "formatted_conversation": "",
    "reask_doctor": "",
    "soap": ""
}

for event in app.stream(initial_state, thread, stream_mode="values"):
    if event.get("spoken_messages"):
        message_content = event["spoken_messages"][-1].content
        if message_content and message_content.strip():
            print(f"Bot: {message_content}")
            engine.say(message_content)
            engine.runAndWait()

