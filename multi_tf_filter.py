import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("strategy_file")
    args = p.parse_args()
    print("Filtering", args.strategy_file)

if __name__ == "__main__":
    main()
