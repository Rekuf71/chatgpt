# autopine_full_orchestrator.py
import subprocess
import time
import os
import signal
import json

# Configurable thresholds, read from config.json
with open("config.json") as f:
    cfg = json.load(f)

CYCLE_DELAY = cfg.get("cycle_delay", 10)  # seconds between iterations

def run_step(script_name, args=None):
    """Run a Python script and stream its output."""
    cmd = ["python", script_name] + (args or [])
    proc = subprocess.Popen(cmd, cwd=os.getcwd())
    proc.communicate()
    return proc.returncode

def main_loop():
    while True:
        # 1) Generate Pine script & strategy JSON
        run_step("pine_generator.py")
        # 2) Backtest & extract results
        run_step("backtest_result_extractor.py")
        # 3) Decide on the strategy
        run_step("strategy_decider.py")
        # 4) Clean up old files
        run_step("cleanup_manager.py")
        # 5) Pause before next cycle
        print(f"[⏳] Waiting {CYCLE_DELAY}s before next cycle…")
        time.sleep(CYCLE_DELAY)

if __name__ == "__main__":
    try:
        print("[🔁] Starting Autopine full orchestrator…")
        main_loop()
    except KeyboardInterrupt:
        # Allow graceful shutdown if STOP sends SIGTERM
        print("[🛑] Orchestrator received stop signal, exiting.")
        os.kill(os.getpid(), signal.SIGTERM)
