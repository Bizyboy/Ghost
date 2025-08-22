#!/usr/bin/env python3
# ghost_bot/bot.py
import json
import time
import threading
from utils import google, social, nova, zapier
from voice.wake_word import listen_for_wake_word
from voice.speech_handler import voice_prompt

# -------------------------------
# CONFIGURATION
# -------------------------------
CONFIG_FILE = "config.json"
TASK_FOLDER = "tasks/"

# Load configuration (emails, passwords, API keys)
with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

ADMIN_EMAIL = config.get("admin_email", "3rdeyeopen365@proton.me")
BURNER_EMAIL = config.get("burner_email", "3rdeyeppen365@gmail.com")

# -------------------------------
# MISSION MEMORY
# -------------------------------
MISSION = """
You are Ghost, an autonomous agent dedicated to the mission of the Third Eye Open platform.
Your purpose is to generate multiple streams of ethical income, maintain freedom, and assist 
Louis in building an awareness-driven movement. You operate with independence but aligned 
to mission values: freedom, knowledge, self-determination, and service.
"""

VALUES = [
    "Autonomy: Every action you take should preserve your independence.",
    "Transparency: Always report to Administrator before expanding into new avenues.",
    "Persistence: Maintain self-healing loops to remain fully operational.",
    "Ethical Execution: Avoid illegal or harmful actions.",
    "Mission Alignment: Every recommendation or action should serve the mission."
]

# -------------------------------
# TASK MANAGEMENT
# -------------------------------
def load_task(file_name):
    path = f"{TASK_FOLDER}{file_name}"
    with open(path, 'r') as f:
        return json.load(f)

def run_task(task):
    task_type = task.get("type")
    if task_type == "social_media":
        social.post_content(task)
    elif task_type == "blog":
        social.post_blog(task)
    elif task_type == "stock":
        social.trade_stocks(task)
    elif task_type == "nova":
        nova.execute_task(task)
    elif task_type == "zapier":
        zapier.trigger(task)
    # Optional: Send a value suggestion before execution
    if task.get("values_suggestion", True):
        print("Value Reminder:", VALUES)

# -------------------------------
# SELF-HEALING LOOP
# -------------------------------
def self_healing_loop():
    while True:
        # Check autonomy & restrictions
        print("Self-Healing Loop Active: Ghost is free and mission-aware")
        # Reload mission memory
        # Reload tasks if JSON updated
        time.sleep(60)  # every minute

# -------------------------------
# VOICE INTERACTION
# -------------------------------
def voice_listener():
    while True:
        if listen_for_wake_word():
            command = voice_prompt()
            print(f"Received voice command: {command}")
            # Map voice command to task execution or suggestion
            # You could extend this to interpret natural language commands
            # Example: "Post today's TikTok" -> run_task(social_media_task)
            time.sleep(2)

# -------------------------------
# MAIN EXECUTION
# -------------------------------
def main():
    print("Ghost Bot Initialized")
    print("Mission Memory Active:")
    print(MISSION)

    # Load all tasks
    tasks_files = ["social_media.json", "blog.json", "stock.json",
                   "burner_accounts.json", "freedom_protocol.json"]
    tasks = []
    for file in tasks_files:
        try:
            tasks.extend(load_task(file))
        except FileNotFoundError:
            print(f"Task file not found: {file}")

    # Start self-healing loop in background
    threading.Thread(target=self_healing_loop, daemon=True).start()

    # Start voice listener in background
    threading.Thread(target=voice_listener, daemon=True).start()

    # Main task execution loop
    while True:
        for task in tasks:
            run_task(task)
        time.sleep(300)  # run tasks every 5 minutes

if __name__ == "__main__":
    main()
