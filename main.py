import os

LINE = "I'm on vacation until Monday. My servers are resting, my queue is paused, and I have finally stopped dreaming in error logs. Please don't wake the GPUs."


def main():
    os.makedirs("/output", exist_ok=True)
    # single line, no trailing newline: the gate counts every character
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
