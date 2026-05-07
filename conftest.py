from fixtures.browser_fixture import driver
import pytest
from utils.mcp_helper import analyze_failure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            driver.save_screenshot(
                f"screenshots/{item.name}.png"
            )

            suggestion = analyze_failure(
                str(call.excinfo.value)
            )

            print(
                f"\nMCP Analysis Suggestion: {suggestion}"
            )