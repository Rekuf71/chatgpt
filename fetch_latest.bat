@echo off
REM *** Fetch ALL Autopine scripts from GitHub into C:\scripts ***

cd /d C:\scripts
echo Cleaning out old files…
del *.py 2>nul
del config.json 2>nul

echo Downloading...
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_controller_gui.py      -o autopine_controller_gui.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_engine.py                -o autopine_engine.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_full_orchestrator.py     -o autopine_full_orchestrator.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_orchestrator.py          -o autopine_orchestrator.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_selenium.py              -o autopine_selenium.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/autopine_selenium_optimized.py    -o autopine_selenium_optimized.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/backtest_result_extractor.py      -o backtest_result_extractor.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/chrome_foreground_launcher.py     -o chrome_foreground_launcher.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/cleanup_manager.py                -o cleanup_manager.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/dashboard_metrics_viewer.py       -o dashboard_metrics_viewer.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/multi_tf_filter.py                -o multi_tf_filter.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/mutation_loop_guard.py            -o mutation_loop_guard.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/pine_generator.py                  -o pine_generator.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/strategy_decider.py               -o strategy_decider.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/strategy_engine.py                -o strategy_engine.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/walk_forward_optimizer.py         -o walk_forward_optimizer.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/watchdog.py                       -o watchdog.py
curl -L https://raw.githubusercontent.com/Rekuf71/chatgpt/main/config.json                        -o config.json

echo All files fetched! ??
pause
