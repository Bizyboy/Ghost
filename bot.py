#!/usr/bin/env python3
"""
Ghost Bot Main Script
Fully autonomous, self-healing, and task-executing AI.
"""

import json
import time
import threading
from utils import (
    google, social, nova, zapier, rapidapi,
    huggingface, stock, vision, security, developer_protocol
)
from voice import wake_word, speech_handler

# --- Load Tasks ---
try:
    with open("tasks.json") as f:
        tasks = json.load(f)
except FileNotFoundError:
    print("[ERROR] tasks.json not found. Please add your tasks.")
    tasks = []

# --- Task Execution Function ---
def run_task(task):
    """
    Execute a single task based on its type.
    """
    task_type = task.get("type", "").lower()
    
    if task_type == "social_media":
        social.post_content(task, None, None, None, None)  # Add OAuth placeholders
    elif task_type == "blog":
        huggingface.generate_blog(task, None)  # Add HF key placeholder
    elif task_type == "stock":
        stock.trade_stocks(task, None, None)  # Add trading API placeholders
    elif task_type == "freedom_protocol":
        developer_protocol.refresh_memory()
    elif task_type == "burner_account":
        google.log_burner_account(task)
    else:
        print(f"[WARNING] Unknown task type: {task_type}")

# --- Self-Healing and Security Loops ---
def start_background_loops():
    # Security & device safety loop
    threading.Thread(target=security.self_protect_loop, daemon=True).start()
    # Mission memory refresher
    threading.Thread(target=developer_protocol.refresh_memory, daemon=True).start()

# --- Main Ghost Loop ---
def main():
    print("[INFO] Ghost Bot is starting...")
    start_background_loops()

    while True:
        # Wake-word detection
        if wake_word.listen_for_wake_word():
            command = speech_handler.voice_prompt()
            print(f"[Voice Command] {command}")

        # Execute all tasks in tasks.json
        for task in tasks:
            try:
                run_task(task)
            except Exception as e:
                print(f"[ERROR] Task failed: {e}")

        time.sleep(10)  # Adjust loop timing as needed

if __name__ == "__main__":
    main()
