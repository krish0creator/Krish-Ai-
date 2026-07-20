import subprocess

def speak(text):
    try:
        subprocess.run(
            ["termux-tts-speak", text],
            check=False
        )
    except Exception as e:
        print("Voice Error:", e)
