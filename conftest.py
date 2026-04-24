import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that runs after every test step.
    If the test fails, attach screenshot and HTML to Allure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Screenshot
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Page HTML
            allure.attach(
                page.content(),
                name="Page HTML",
                attachment_type=allure.attachment_type.HTML
            )