def to_pine(config):
    return "// Pine code..."

if __name__ == "__main__":
    import json
    cfg = json.load(open("config.json"))
    print(to_pine(cfg))
