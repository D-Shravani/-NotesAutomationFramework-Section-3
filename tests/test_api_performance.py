import requests
import time

from utils.config_reader import read_config


def test_api_response_time():

    config = read_config()

    start_time = time.time()

    response = requests.get(
        config["base_url"] + "/api/notes"
    )

    end_time = time.time()

    response_time = end_time - start_time

    print(
        f"\nAPI Response Time: {response_time} seconds"
    )

    # SAVE INTO LOG FILE
    with open(
        "logs/performance_log.txt",
        "a"
    ) as file:

        file.write(
            f"API Response Time: {response_time} seconds\n"
        )

    assert response_time < 5