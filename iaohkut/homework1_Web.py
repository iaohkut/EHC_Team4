from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

yourmail = input("Enter your email: ")
password = getpass.getpass(prompt="Enter your password: ")
url1 = "https://github.com/session"
url = "https://github.com/login?return_to=%2Fjoin%3Fsource%3Dheader-home"

driver = webdriver.Firefox()
driver.get(url)

mail = driver.find_element_by_id("login_field")
mail.send_keys(yourmail)

passw = driver.find_element_by_id("password")
passw.send_keys(password)

driver.find_element_by_name("commit").click()
