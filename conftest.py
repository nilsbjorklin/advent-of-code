import pytest
import logging


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO, format="%(message)s")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.failed:
            logging.info(f"FAILED: {report.nodeid}")
        elif report.passed:
            logging.info(f"PASSED: {report.nodeid}")
        elif report.skipped:
            logging.info(f"SKIPPED: {report.nodeid}")
