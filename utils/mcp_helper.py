def analyze_failure(error_message):

    if "NoSuchElementException" in error_message:

        return "Suggested Fix: Verify locator or use self-healing locator strategy."

    elif "TimeoutException" in error_message:

        return "Suggested Fix: Increase explicit wait or improve synchronization."

    else:

        return "Suggested Fix: Review logs and screenshots for analysis."