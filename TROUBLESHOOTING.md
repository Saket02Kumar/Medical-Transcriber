# Medical Transcriber - Troubleshooting Guide

## Current Status

### ✅ Fixed Issues
1. **PyTorch warning** - This is just a warning from `transformers`. It does not block functionality.
2. **GROQ_API_KEY error** - Fixed by loading from environment variable. You must set it before running.
3. **Missing `twilio` dependency** - Installed and added to `requirements.txt`.
4. **Empty initial state** - Fixed by properly initializing the graph state with `messages` field.

### 🔄 Current Behavior

When you run `python main.py`:
1. The bot says "Hey doctor how can i help?"
2. The app starts the LangGraph workflow
3. The first node `record_intro_speech` opens your **microphone** and waits for you to speak
4. It listens for 3 seconds of audio
5. When it detects speech, it converts it to text using Groq's speech recognition
6. The text is then processed through the graph nodes

**This is expected behavior.** The app is not stuck—it's waiting for you to speak into the microphone.

---

## How to Run (Production Mode with Microphone)

### 1. Set your Groq API Key

**For current session only:**
```powershell
$env:GROQ_API_KEY = 'your_groq_api_key_here'
```

**Permanently (for all future sessions):**
```powershell
setx GROQ_API_KEY "your_groq_api_key_here"
# Then open a new PowerShell window
```

### 2. Run the bot
```powershell
cd "C:\Users\Saket Kumar\Downloads\Medical-Transcriber-main\Medical-Transcriber-main\bot"
python main.py
```

### 3. Speak into the microphone
- After the "Hey doctor how can i help?" prompt
- Wait for "Listening...." to appear
- Speak clearly
- The bot will transcribe and respond

---

## Test Mode (Without Microphone)

If you want to test the graph workflow without a microphone:

```powershell
cd "C:\Users\Saket Kumar\Downloads\Medical-Transcriber-main\Medical-Transcriber-main\bot"
python main_test.py
```

This version will:
- Skip all microphone input
- Print detailed state transitions
- Show what each node returns
- Help debug the workflow logic

---

## Troubleshooting

### Issue: "No speech detected for 3 seconds"
- Your microphone may not be working
- Try checking your system audio settings
- Test with: `python -m speech_recognition` (if installed)

### Issue: "RuntimeError: GROQ_API_KEY environment variable is not set"
- You forgot to set the environment variable
- Follow the steps in "Set your Groq API Key" above

### Issue: "ModuleNotFoundError: No module named 'X'"
- Run: `pip install -r requirements.txt`
- Make sure you're in the `bot` directory and your venv is activated

### Issue: MongoDB connection error
- Check `bot/mongo.py` for the connection string
- Ensure MongoDB is running on your system

---

## Project Structure

```
bot/
├── main.py              # Entry point (microphone mode)
├── main_test.py         # Test mode (text-based, no microphone)
├── graph.py             # LangGraph workflow definition
├── tools.py             # Tool functions for graph nodes
├── model.py             # Groq LLM initialization
├── classes.py           # MessageState TypedDict
├── call.py              # Twilio integration
├── mongo.py             # MongoDB integration
└── requirements.txt     # Python dependencies
```

---

## Next Steps

1. **Verify Groq API Key** - Confirm you have a valid key from https://platform.groq.com
2. **Test microphone** - Ensure your microphone works on Windows
3. **Run production mode** - Execute `python main.py` and speak into the microphone
4. **Or use test mode** - Execute `python main_test.py` to debug without audio

Good luck! 🎤
