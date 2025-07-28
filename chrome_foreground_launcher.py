import subprocess

def launch_in_foreground():
    subprocess.Popen(["start", "chrome", "--new-window", "https://example.com"], shell=True)

if __name__ == "__main__":
    launch_in_foreground()
