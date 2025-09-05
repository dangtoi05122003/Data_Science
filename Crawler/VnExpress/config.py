from selenium.webdriver.chrome.options import Options

def setup():
    options = Options()
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--headless")
    return options
