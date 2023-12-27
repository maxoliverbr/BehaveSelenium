import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def before_all(context):
    context.chrome_options = ChromeOptions()
    # context.chrome_options.add_argument('--headless')
    # context.chrome_options.add_argument('--disable-notifications')
    # context.chrome_options.add_argument('--no-sandbox')
    context.chrome_options.add_argument('--verbose')
    context.chrome_options.add_argument('--disable-gpu')
    context.chrome_options.add_argument('--disable-software-rasterizer')
    context.driver = webdriver.Chrome(options=context.chrome_options)
    context.driver.implicitly_wait(3)




def after_all(context):
    context.driver.quit()
