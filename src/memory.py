import json
import os

MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def remember(key, value):
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def recall(key):
    return memory.get(key)

def forget(key):
    if key in memory:
        del memory[key]
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)

def show_memory():
    return memory

def clear_memory():
    global memory
    memory = {}
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)
