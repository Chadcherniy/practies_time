import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
#окно регистрации
# my_accaunt = driver.find_element_by_id("menu-item-50")
# # my_accaunt.click()
# # email = driver.find_element_by_name('email')
# # email.send_keys("Bomge@google.com")
# # password = driver.find_element_by_id('reg_password')
# # password.send_keys("Bomge777!")
# # time.sleep(1)
# # register = driver.find_element_by_name('register')
# # register.click()

#окно логина
my_accaunt = driver.find_element_by_id("menu-item-50")
my_accaunt.click()
username = driver.find_element_by_name('username')
username.send_keys("Bomge@google.com")
password = driver.find_element_by_id('password')
password.send_keys("Bomge777!")
time.sleep(1)
login = driver.find_element_by_name('login')
login.click()
element = driver.find_element_by_link_text("Logout")
element_get_text = element.text
assert "Logout" in element_get_text

