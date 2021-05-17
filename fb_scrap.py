from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


email = input("enter your email: ")
password = input("enter your password: ")

PATH ="/Library/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8")

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_name("login").click()

driver.find_element_by_class_name("bt").click()
driver.find_element_by_class_name("bh").click()
driver.find_element_by_link_text("Friends").click()
friends = driver.find_elements_by_class_name("ch")

list = []

for friend in friends:
    list.append(friend.text)
print(list)

lenght = len(list)
num = -1

for x in range(lenght):
    num += 1
    driver.find_element_by_link_text(list[num]).click()
    try:
        driver.find_element_by_link_text("Likes").click()
    except:
        pass
    else:
        all = driver.find_elements_by_class_name('bp')

        likes_list = []
        for a in all:
            likes_list.append(a.text)
            NAME = list[num]
            DETAILS = likes_list

            friends_dict = {
                NAME: {
                    "likes": DETAILS
                }
            }

            try:
                with open("friend.json", "r") as file:
                    # reading the data
                    data = json.load(file)

            except FileNotFoundError:
                with open("friend.json", "w") as file:
                    # writing into the data
                    json.dump(friends_dict, file, indent=4)

            else:
                # updating the data
                data.update(friends_dict)

                with open("friend.json", "w") as file:
                    # writing into the data
                    json.dump(data, file, indent=4)

        driver.back()

    driver.back()






# friend_like = []
# friend = {
#     "mutuals" : "",
#     "likes" : "",
#     "female" : "",
# }
#
#
# email = input("enter your email: ")
# password = input("enter your password: ")
#
# PATH ="/Library/chromedriver"
# driver = webdriver.Chrome(PATH)
# driver.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8")
#
# driver.find_element_by_name("email").send_keys(email)
# driver.find_element_by_name("pass").send_keys(password)
# driver.find_element_by_name("login").click()
#
# driver.find_element_by_class_name("bo").click()
# driver.find_element_by_class_name("bh").click()
# driver.find_element_by_link_text("Friends").click()
#
# driver.find_element_by_link_text("Ogechukwuka O Chigbogwu").click()
#
#
# driver.find_element_by_link_text("Friends").click()

# mutuals = driver.find_element_by_class_name("cd").text
# friends = driver.find_elements_by_class_name("ch")
#
# list = []
#
# for friend in friends:
#     list.append(friend.text)
# print(list)
#
# lenght = len(list)
# num = -1
#
# for x in range(lenght):
#     num += 1
#     driver.find_element_by_link_text(list[num]).click()
#     driver.find_elements_by_class_name("")

