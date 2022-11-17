import pandas as pd
from selenium import webdriver

def read_urls_from_excel(path):
    df = pd.read_excel(path)
    return df

def get_driver(driver_path):
    browser = webdriver.Chrome(executable_path=driver_path)
    return browser