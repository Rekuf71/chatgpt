import os, glob

def clean_generated():
    for f in glob.glob("generated/*"):
        os.remove(f)

if __name__ == "__main__":
    clean_generated()
