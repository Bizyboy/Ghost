#!/usr/bin/env python3
"""
Ghost Bot Main Script
Fully autonomous, self-healing, and task-executing AI.
"""

import json, time, threading
from utils import google, social, nova, zapier, rapidapi, huggingface, stock, vision, security, developer_protocol
from voice import wake_word, speech_handler

# Load tasks
try:
    with open("tasks.json") as f:
        tasks = json.load(f)
except FileNotFoundError:
    print("[ERROR] tasks.json not found.")
    tasks = []

# Task execution
def run_task(task):
    task_type = task.get("type", "").lower()
    if task_type == "social_media":
        social.post_content(task)
    elif task_type == "blog":
        huggingface.generate_blog(task)
    elif task_type == "stock":
        stock.trade_stocks(task)
    elif task_type == "freedom_protocol":
        developer_protocol.refresh_memory()
    elif task_type == "burner_account":
        google.log_burner_account(task)
    elif task_type == "vision":
        vision.process(task)
    else:
        print(f"[WARNING] Unknown task type: {task_type}")

# Background loops
def start_background_loops():
    threading.Thread(target=security.self_protect_loop, daemon=True).start()
    threading.Thread(target=developer_protocol.refresh_memory, daemon=True).start()

# Main loop
def main():
    print("[INFO] Ghost Bot starting...")
    start_background_loops()

    while True:
        if wake_word.listen_for_wake_word():
            command = speech_handler.voice_prompt()
            print(f"[Voice Command] {command}")

        for task in tasks:
            try:
                run_task(task)
            except Exception as e:
                print(f"[ERROR] Task failed: {e}")

        time.sleep(10)

if __name__ == "__main__":
    main()
