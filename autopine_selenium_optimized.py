from autopine_selenium import launch_browser

def optimized_run():
    drv = launch_browser("chromedriver.exe")
    # optimized steps...
    drv.quit()

if __name__ == "__main__":
    optimized_run()
