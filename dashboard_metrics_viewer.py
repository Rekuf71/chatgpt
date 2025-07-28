import json

def show_summary():
    files = ["generated/" + f for f in os.listdir("generated")]
    for fn in files:
        with open(fn) as f:
            data = json.load(f)
            print(fn, data)

if __name__ == "__main__":
    show_summary()
