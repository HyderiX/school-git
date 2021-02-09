import os
from selenium import webdriver
from time import sleep
import courses
import json

def get_schedule():
    with open('credentials.txt', 'r') as f:
        credentials = f.readlines()
    for line in credentials:
        credentials[credentials.index(line)] = line.strip()

    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    driver.get('https://vklass.se')

    login = driver.find_element_by_xpath('/html/body/div/div/section/div[2]/div/div[1]/a[3]')
    login.click()

    uname = driver.find_element_by_xpath('//*[@id="Username"]')
    uname.click()
    uname.send_keys(credentials[0])
    password = driver.find_element_by_xpath('//*[@id="Password"]')
    password.click()
    password.send_keys(credentials[1])

    submitbutton = driver.find_element_by_xpath('/html/body/div/div/section/div[2]/div/form/div[4]/button')
    submitbutton.click()

    schedulelink = driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/ul/li[2]/a')
    schedulelink.click()

    lessions = driver.find_elements_by_xpath('//*[@class="resv-span6"]')

    days = dict()
    days_str = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]

    for i in range(len(days_str)):
        days[days_str[i]]=list()

    for lession in lessions:
        try:
            for day in days_str:
                if lession.text.split('\n')[0].startswith(day):
                    days[day].append((lession.text.split('\n')[0].replace(day+' ', ''), lession.text.split('\n')[1]))
            #print(lession.text.split('\n')[0])
            #print(courses.courses[lession.text.split('\n')[1]])
        except Exception as e:
            print("_______")
            print(e)
            print("_______")
    with open('schedulejson.txt', 'w') as f:
        f.write(json.dumps(days))
    driver.close()
    return True
if __name__ == '__main__':
    get_schedule()