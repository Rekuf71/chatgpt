import random, time

def run_extractor():
    """Demo-mode backtester: returns randomized metrics."""
    time.sleep(0.1)
    return {
        "win_rate": round(random.uniform(0.2, 0.8), 2),
        "profit_factor": round(random.uniform(1.0, 3.0), 2),
        "drawdown": round(random.uniform(0.0, 0.2), 2),
        "rr_ratio": round(random.uniform(1.5, 3.0), 2),
        "trades": random.randint(50, 200)
    }
