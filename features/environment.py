# -- FILE: features/environment.py

from playwright.sync_api import sync_playwright
from behave import fixture, use_fixture


@fixture
def browser_chrome(context):
    p = sync_playwright().start()
    #browser = p.chromium.launch(headless=False, slow_mo=500, channel="chrome")
    browser = p.chromium.launch(channel="chrome")
    context.browser = browser
    context.page = browser.new_page()
    yield context.page
    p.stop();

def before_scenario(context,scenario):
     use_fixture(browser_chrome, context)


def after_scenario(context, scenario):
    pass