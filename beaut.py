from selenium import webdriver

import pandas as pd
import csv


PATH ="/Library/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("http://books.toscrape.com/")

for x in range(5):
    for x in range(20):
        books = driver.find_elements_by_class_name("thumbnail")
        books[x].click()
        name = driver.find_element_by_class_name("product_main")
        s = (name.text).split("\n")
        s.pop(3)
        # print(f"Product name = {s[0]}")
        # print(f"Product price = {s[1]}")
        # print(f"Availability = {s[2]}")

        rating = driver.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]')
        rate = rating.get_attribute('class')
        # print(f"Rate = {rate[12::]}")

        description = driver.find_element_by_xpath('//*[@id="content_inner"]/article/p')
        # print(f"Product description = {description.text}")

        info = driver.find_element_by_xpath('//*[@id="content_inner"]/article/table/tbody/tr[1]/td')
        # print(f"Product Info = {info.text}")

        category = driver.find_element_by_xpath('//*[@id="default"]/div/div/ul/li[3]/a')
        # print(f"Category = {category.text} \n\n")

        try:
            list_of_books = [s[0], s[1], s[2], rate[12::], description.text, info.text, category.text]
            with open('book.csv', 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = csv.writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(list_of_books)

        except FileNotFoundError:
            book_data = {
                "name": [s[0]],
                "price": [s[1]],
                "availability": [s[2]],
                "rate": [rate[12::]],
                "description": [description.text],
                "info": [info.text],
                "category": [category.text],
            }

            data = pd.DataFrame(book_data)
            data.to_csv('book.csv')

        #move back
        driver.back()

    #to the next page
    driver.find_element_by_link_text('next').click()
# name,price,availability,rate,description,info,category