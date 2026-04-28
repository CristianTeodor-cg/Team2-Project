import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if not page:
            return

        # Screenshot (do NOT let it crash the test run)
        try:
            png_bytes = page.screenshot(timeout=5000)  # 5s instead of 30s default
            allure.attach(
                png_bytes,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            # If screenshot hangs/timeouts, we still want the run to continue
            allure.attach(
                str(e),
                name="Screenshot failed (ignored)",
                attachment_type=allure.attachment_type.TEXT
            )

        # Page HTML (also protect it)
        try:
            html = page.content()
            allure.attach(
                html,
                name="Page HTML",
                attachment_type=allure.attachment_type.HTML
            )
        except Exception as e:
            allure.attach(
                str(e),
                name="HTML capture failed (ignored)",
                attachment_type=allure.attachment_type.TEXT
            )