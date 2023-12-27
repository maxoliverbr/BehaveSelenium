import time
from behave import given, when, then
from selenium.webdriver.common.by import By


@given("the user is in Disney Plus home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get('https://www.disneyplus.com/')
    assert context.driver.title == "Disney+ | Disney, Pixar, Marvel & National Geographic"


@when("the user clicks on the Sign Up")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.XPATH, "//a[@data-testid='standalone_cta_annual_hero']").click()



@then("the app shows an email form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.title == 'Sign Up | Disney+'
