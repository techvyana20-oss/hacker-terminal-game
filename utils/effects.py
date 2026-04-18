import time

def slow_text(text):
    for line in text.strip().split("\n"):
        for c in line:
            print(c, end="", flush=True)
            time.sleep(0.02)
        print()
        time.sleep(0.2)
