from operator import truediv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

URL = 'https://coinmarketcap.com/'
s = Service('C:\edgedriver\msedgedriver')
driver = webdriver.Edge(service=s)
driver.get(URL)
driver.execute_script("window.scrollTo(0, 1800);")
tbody = driver.find_element_by_tag_name("tbody")
currencies = tbody.text.splitlines()
crypt = []
for i in range (1,250,9):
    list = []
    list.append(currencies[i])
    list.append(currencies[i + 2])
    list.append(currencies[i + 5])
    crypt.append(list)
time.sleep(2.5)
os.system("cls")
flag = True
while(flag):
    print("1. Print currencies")
    print("2. Find currency")
    print("0. Exit")
    cmd = input("Select: ")
    if cmd == "1":
        for i in range(len(crypt)):
            print(i,". ", crypt[i], sep = "")
        input("Press any key to continue...")
        os.system("cls")
    elif cmd == "2":
        name = input("Enter name: ")
        for i in crypt:
            if name in i[0]:
                print(i)
                print()
        input("Press any key to continue...")
        os.system("cls")
    elif cmd == "0":
        flag = False
