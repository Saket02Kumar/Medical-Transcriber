"""
Text-mode test version of main.py for testing without a microphone.
Use this to verify the graph and workflow.
"""
from graph import app
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

print("Starting Medical Transcriber (TEXT MODE - no microphone).")
print("=" * 60)

thread = {"configurable": {"thread_id": "1"}}
initial_state = {
    "messages": [HumanMessage(content="start")],
    "spoken_messages": [],
    "recorded_text": "",
    "formatted_conversation": "",
    "reask_doctor": "",
    "soap": ""
}

event_count = 0
for event in app.stream(initial_state, thread, stream_mode="values"):
    event_count += 1
    print(f"\n--- Event {event_count} ---")
    
    # Print current state keys
    print(f"State keys: {list(event.keys())}")
    
    # Print messages if present
    if event.get("messages"):
        msg = event["messages"][-1] if event["messages"] else None
        if msg:
            print(f"Latest message: {msg.content}")
    
    # Print spoken_messages if present
    if event.get("spoken_messages"):
        msg = event["spoken_messages"][-1] if event["spoken_messages"] else None
        if msg:
            print(f"Spoken message: {msg.content}")
    
    # Print other fields
    if event.get("recorded_text"):
        print(f"Recorded text: {event['recorded_text'][:100]}...")
    if event.get("formatted_conversation"):
        print(f"Formatted conversation: {event['formatted_conversation'][:100]}...")
    if event.get("reask_doctor"):
        print(f"Reask doctor: {event['reask_doctor'][:100]}...")
    if event.get("soap"):
        print(f"SOAP: {event['soap'][:100]}...")
    
    if event_count > 20:  # Safety limit
        print("\nStopping after 20 events (safety limit).")
        break

print("\n" + "=" * 60)
print(f"Total events processed: {event_count}")
