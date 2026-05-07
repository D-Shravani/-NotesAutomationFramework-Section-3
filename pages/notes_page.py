import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.self_healing import find_element_with_healing


class NotesPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

        self.add_note_btn = (
            By.XPATH,
            "//button[@data-testid='add-new-note']"
        )

        self.title = (
            By.ID,
            "title"
        )

        self.description = (
            By.ID,
            "description"
        )

        self.category = (
            By.XPATH,
            "//select"
        )

        self.save_btn = (
            By.XPATH,
            "//button[contains(text(),'Create')]"
        )

    def create_note(self, title, description, category):

        # Wait before next action
        time.sleep(2)

        # Click Add Note
        add_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.add_note_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        # Wait for modal
        self.wait.until(
            EC.visibility_of_element_located(
                self.title
            )
        )

        # Enter title
        title_box = find_element_with_healing(
            self.driver
        )

        title_box.clear()

        title_box.send_keys(title)

        # Enter description
        description_box = self.driver.find_element(
            *self.description
        )

        description_box.clear()

        description_box.send_keys(description)

        # Select category
        category_box = self.driver.find_element(
            *self.category
        )

        category_box.send_keys(category)

        # Small wait before clicking Create
        time.sleep(2)

        # Click Create button
        create_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.save_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            create_btn
        )

        # Wait after note creation
        time.sleep(3)