import streamlit as st
from flask import Flask, request
from threading import Thread

# Flask app to receive webhook messages
flask_app = Flask(__name__)
messages = []  # List to store received messages

@flask_app.route('/webhook', methods=['POST'])
def webhook():
    global messages
    data = request.json  # Parse incoming JSON data
    messages.append(data)
    return "Message received", 200

# Function to run Flask in a separate thread
def run_flask():
    flask_app.run(port=8888)

# Start Flask server in a separate thread
flask_thread = Thread(target=run_flask, daemon=True)
flask_thread.start()

# Streamlit interface to display messages
st.title("Car Infotainment App")
st.subheader("Messages from AJO Adobe")

# Button to refresh messages
if st.button("Refresh"):
    st.rerun()

# Display received messages
st.write("Received Messages:")
for idx, msg in enumerate(messages, 1):
    st.write(f"**Message {idx}:** {msg}")
