def decide(results):
    return "long" if results["win_rate"] > 0.5 else "flat"

if __name__ == "__main__":
    print(decide({"win_rate":0.6}))
