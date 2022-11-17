import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
INPUT_FILE = 'Input.xlsx'
DRIVER_PATH = 'D:\chromedriver'

if __name__ == "__main__":
    df = utils.read_urls_from_excel(INPUT_FILE)
    browser = utils.get_driver(DRIVER_PATH)
    for index,data in df.iterrows():
        print(f"========== INDEX : {index} ================")
        browser.get(data["URL"])
        try:
            with open(f"url_text\{data['URL_ID']}.txt", mode="a") as data_file:
                data_file.write(f'{WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text}\n\n\n')
                data_file.write(f'{browser.find_element(By.CLASS_NAME, "td-post-content").text}')
        except Exception as e:
            print(f"ERROR >>>>>>>>>> {e}")
    browser.close()