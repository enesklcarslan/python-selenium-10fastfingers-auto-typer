import selenium
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path= r"driver\chromedriver.exe")
from selenium.webdriver.common.keys import Keys

driver.get("https://10fastfingers.com/advanced-typing-test/") #or you can insert any other link on the website here (challenges etc)
sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div[2]/a[3]').click()
sleep(1)
try:
    while True:
        word = driver.find_element_by_css_selector('span.highlight').text + " "
        inputField = driver.find_element_by_css_selector('input#inputfield.form-control')
        inputField.send_keys(word)
        sleep(0.1)
except:
    print("No more words to type.")
