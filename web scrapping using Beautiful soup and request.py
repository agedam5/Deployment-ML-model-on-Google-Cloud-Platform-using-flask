# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:41:48 2020

@author: DELL
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import pandas as pd
import numpy as np

my_url = ['https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=1','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=2','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=3','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=4','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=5','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=6','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=7','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=8','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=9','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=10','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=11','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=12','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=13','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=14','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=15','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=16','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=17','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=18','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=19','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=20','https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&page=21']

phone_name = []
ram_size = []
rom_size = []
battery_capacity = []
pricing = []

for url in my_url:

    u_client = ureq(url)

    page_html = u_client.read()

    page_soup = soup(page_html,"html.parser")

    containers = page_soup.find_all("div",{"class":"_3O0U0u"})

    container = containers[0]

    for container in containers:

        name=container.find_all("div",{"class":"_3wU53n"})
        print(name[0].text.split(" ")[0])
        phone_name.append(name[0].text.split(" ")[0])

        memory =container.find_all("li",{"class":"tVe95H"})[0].text.split("|")
        ram = memory[0].strip()
        rom = memory[1].strip()
        print(ram.split(" ")[0])
        print(rom.split(" ")[0])
        ram_size.append(ram.split(" ")[0])
        rom_size.append(rom.split(" ")[0])


        battery =container.find_all("li",{"class":"tVe95H"})[3]
        print(battery.text[0:4])
        battery_capacity.append(battery.text[0:4])

        price = container.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
        print(price[0].text[1:])
        pricing.append(price[0].text[1:])
    
main_data = pd.DataFrame({'Phone':phone_name,'Battery':battery_capacity,'RAM':ram_size,'ROM':rom_size,'Price':pricing})

main_data.to_csv('flipkart.csv')












