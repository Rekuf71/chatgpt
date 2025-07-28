import time, json
from backtest_result_extractor import run_extractor

def save_strategy_file(config):
    ts = int(time.time())
    fname = f"strategy_{config['name']}_{ts}.json"
    results = run_extractor()
    with open(f"generated/{fname}", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    # no-op
    pass
