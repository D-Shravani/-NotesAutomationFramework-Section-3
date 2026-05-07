import time

from utils.config_reader import read_config


def test_ui_load_time(driver):

    config = read_config()

    start_time = time.time()

    driver.get(
        config["base_url"]
    )

    end_time = time.time()

    load_time = end_time - start_time

    print(
        f"\nUI Load Time: {load_time} seconds"
    )

    # SAVE INTO LOG FILE
    with open(
        "logs/performance_log.txt",
        "a"
    ) as file:

        file.write(
            f"UI Load Time: {load_time} seconds\n"
        )

    assert load_time < 10