from selenium import webdriver

def launch_browser(chrome_path):
    opts = webdriver.ChromeOptions()
    return webdriver.Chrome(executable_path=chrome_path, options=opts)

if __name__ == "__main__":
    driver = launch_browser("chromedriver.exe")
    driver.get("https://example.com")
