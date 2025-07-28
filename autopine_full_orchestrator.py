import json
from strategy_engine import save_strategy_file

def main():
    with open("config.json") as f:
        cfg = json.load(f)
    save_strategy_file(cfg)

if __name__ == "__main__":
    main()
