import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# book = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# book.click()
# element = driver.find_element_by_css_selector(".product_title.entry-title")
# element_get_text = element.text
# assert "HTML5 Forms" in element_get_text

#тест2
# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# html = driver.find_element_by_link_text("HTML")
# html.click()
# element = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19.current-cat > span")
# element_get_text = element.text
# assert "3" in element_get_text

#тест3
#
# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# default = driver.find_element_by_css_selector('[value="menu_order"]')
# default_selected = default.get_attribute("selected")
# print("value of default_selected: ", default_selected)
# if default_selected is not None:
#      print("по умолчанию")
# else:
#      print("шляпа")
# from selenium.webdriver.support.select import Select
# price = driver.find_element_by_name("orderby")
# select = Select(price)
# select.select_by_value("price-desc")
# time.sleep(1)
# check = driver.find_element_by_css_selector('[value="price-desc"]')
# check_selected = check.get_attribute("selected")
# print("value of check_selected: ", check_selected)
# if default_selected is not None:
#      print("high to low")
# else:
#      print("шляпа")

#тест4

# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# book = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
# book.click()
# element = driver.find_element_by_css_selector("del > .woocommerce-Price-amount.amount")
# element_get_text = element.text
# assert "600" in element_get_text
# element2 = driver.find_element_by_css_selector("ins > .woocommerce-Price-amount.amount")
# element2_get_text = element2.text
# assert "450" in element2_get_text
# ssylka = WebDriverWait(driver, 10).until(
#     EC.url_to_be(("https://practice.automationtesting.in/product/android-quick-start-guide/")) )
# obl = driver.find_element_by_css_selector(".attachment-shop_single.size-shop_single.wp-post-image")
# obl.click()
# ssylka1 = WebDriverWait(driver, 10).until(
#     EC.url_to_be(("https://practice.automationtesting.in/product/android-quick-start-guide/")) )
# btn = driver.find_element_by_class_name("pp_close")
# btn.click()

#test5

# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# book = driver.find_element_by_css_selector("[data-product_id='182']")
# book.click()
# time.sleep(5)
# element = driver.find_element_by_class_name("cartcontents")
# element_get_text = element.text
# assert "1" in element_get_text
# element2 = driver.find_element_by_class_name("amount")
# element2_get_text = element2.text
# assert "180" in element2_get_text
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
# ssylka = WebDriverWait(driver, 10).until(
#      EC.url_to_be(("https://practice.automationtesting.in/basket/")) )
# element3 = driver.find_element_by_css_selector("[data-title='Subtotal']")
# element3_get_text = element3.text
# assert "180" in element3_get_text
# print (element3_get_text)
# element4 = driver.find_element_by_class_name("order-total")
# element4_get_text = element4.text
# assert "183.60" in element4_get_text
# print (element4_get_text)

#test6

# my_accaunt = driver.find_element_by_id("menu-item-50")
# my_accaunt.click()
# username = driver.find_element_by_name('username')
# username.send_keys("Bomge@google.com")
# password = driver.find_element_by_id('password')
# password.send_keys("Bomge777!")
# time.sleep(1)
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book = driver.find_element_by_css_selector("[data-product_id='182']")
# book.click()
# time.sleep(3)
# book2 = driver.find_element_by_css_selector("[data-product_id='180']")
# book2.click()
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
# time.sleep(3)
# remove = driver.find_element_by_class_name("remove")
# remove.click()
# time.sleep(3)
# undo = driver.find_element_by_link_text("Undo?")
# undo.click()
# time.sleep(3)
# clear = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
# clear.clear()
# quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
# quantity.send_keys('3')
# remove = driver.find_element_by_name("update_cart")
# remove.click()
# time.sleep(5)
# element = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
# element_check = element.get_attribute("value")
# assert element_check == '3'
# time.sleep(1)
# apply = driver.find_element_by_name("apply_coupon")
# apply.click()
# time.sleep(1)
# massage = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"),"Please enter a coupon code") )

#test7

driver.execute_script("window.scrollBy(0, 300);")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
book = driver.find_element_by_css_selector("[data-product_id='182']")
book.click()
time.sleep(1)
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
ssylka = WebDriverWait(driver, 10).until(
    EC.url_to_be(("https://practice.automationtesting.in/basket/")))
ptc = driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward")
ptc.click()
ssylka2 = WebDriverWait(driver, 10).until(
    EC.url_to_be(("https://practice.automationtesting.in/checkout/")))
FN = driver.find_element_by_id("billing_first_name")
FN.send_keys('Pop')
LN = driver.find_element_by_id("billing_last_name")
LN.send_keys('Smoke')
email = driver.find_element_by_id("billing_email")
email.send_keys('Pop@google.com')
phone = driver.find_element_by_id("billing_phone")
phone.send_keys('7777777777')
country = driver.find_element_by_id("select2-chosen-1")
country.click()
country_text = driver.find_element_by_id("s2id_autogen1_search")
country_text.send_keys('India')
country_vyb = driver.find_element_by_css_selector("#select2-result-label-460 > span")
country_vyb.click()
addres = driver.find_element_by_id("billing_address_1")
addres.send_keys('77 Street')
City = driver.find_element_by_id("billing_city")
City.send_keys('77 City')
state = driver.find_element_by_id("select2-chosen-2")
state.click()
state_text = driver.find_element_by_id("s2id_autogen2_search")
state_text.send_keys('bihar')
state_vyb = driver.find_element_by_css_selector("#select2-result-label-504 > span")
state_vyb.click()
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys('Pop postcode')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
option = driver.find_element_by_id("payment_method_cheque")
option.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
time.sleep(2)
check_text = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"),"Thank you. Your order has been received") )
check_text2 = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3)"),"Check Payments") )
