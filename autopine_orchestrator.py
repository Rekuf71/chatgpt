from autopine_engine import generate_signals

def run():
    data = {}  # load data
    signals = generate_signals(data)
    print(signals)

if __name__ == "__main__":
    run()
