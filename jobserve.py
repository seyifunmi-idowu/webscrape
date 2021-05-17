from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "seyiidowu24@yahoo.com"

PATH ="/Library/chromedriver"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 20)
driver.get("https://www.jobserve.com/gb/en/Job-Search/")

driver.find_element_by_xpath('//*[@id="txtKey"]').send_keys("Data Scientist")
driver.find_element_by_id("btnSearch").click()
# driver.get("https://www.jobserve.com/gb/en/JobSearch.aspx?shid=415E7EF3D52E66613550")

# jobs = driver.find_elements_by_class_name("jobsum")
# jobs[1].click()

data = driver.find_element_by_id("td_jobpositionlink")

if "data scientist" in data.text.lower():

    driver.find_element_by_link_text("Apply").click()

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#appFrame")))
    email = driver.find_element_by_css_selector(".questionblock2>.questionInput>input")
    email.send_keys(EMAIL)
    Select(driver.find_element_by_id("Q0133_ans")).select_by_visible_text("Sponsorship Required")
    driver.find_element_by_id('filCV').send_keys("/Users/mac/PycharmProjects/pythonProject/seyifunmi.docx")
    driver.find_element_by_class_name('AppButton').click()

    driver.close()

