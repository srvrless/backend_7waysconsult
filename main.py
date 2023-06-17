# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

# import time

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в безголовом режиме
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.google.com/")
# box = driver.find_element("xpath", ("//*/form/div[1]/div[1]/div[1]/div/div[2]/input"))
# print("The input Element is: ", box)
# box.send_keys("Send")
# box.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.close()
# from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()

options.add_argument("--disable-cookies")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

# button = driver.find_element(By.CLASS_NAME, u"infoDismiss")
# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(button).click(button).perform()
time.sleep(5)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("птица")
search_box.submit()


driver.quit()
