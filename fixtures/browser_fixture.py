from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():

    execution = "local"

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-notifications")

    options.add_argument("--disable-popup-blocking")

    options.add_argument("--disable-infobars")

    options.add_argument("--remote-allow-origins=*")


    if execution == "local":

        driver = webdriver.Chrome(

            service=Service(
                ChromeDriverManager().install()
            ),

            options=options
        )

    else:

        driver = webdriver.Remote(

            command_executor="http://localhost:4444",

            options=options
        )

    yield driver

    driver.quit()