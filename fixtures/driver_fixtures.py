import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

PLATFORM = "android"

@pytest.fixture(scope="session")
def driver():
    appium_server_url = "http://127.0.0.1:4723"

    if PLATFORM == "android":
        caps = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "Android",
            "appium:udid": "emulator-5554",
            "appium:appPackage": "com.android.contacts",
            "appium:appActivity": "com.android.contacts.activities.PeopleActivity",
            "appium:noReset": True
        }

        options = UiAutomator2Options().load_capabilities(caps)

        driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=options
        )

        package_name = caps["appium:appPackage"]

        app_state = driver.query_app_state(package_name)

        if app_state < 4:
            driver.activate_app(package_name)

        yield driver

        driver.quit()