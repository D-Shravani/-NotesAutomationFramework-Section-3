from selenium.webdriver.common.by import By


def find_element_with_healing(driver):

    locators = [

        (By.ID, "title"),

        (By.NAME, "title"),

        (
            By.XPATH,
            "//input[@placeholder='Enter title']"
        )
    ]

    for locator in locators:

        try:

            element = driver.find_element(
                *locator
            )

            print(
                f"Element found using: {locator}"
            )

            return element

        except:

            continue

    raise Exception(
        "Element not found using any locator"
    )