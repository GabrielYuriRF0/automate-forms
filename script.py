from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui

dataFrame = pd.read_excel('weekly-activities.xlsx')

def extractData(dataFrame):
    days = ["Segunda" , "Terca", "Quarta", "Quinta", "Sexta"]
    activitiesOfWeek = ""
    j = -1

    for day in days:
        activitiesOfWeek += day + " : "
        j += 1
        for i in range(3):
            if type(activitiesOfWeek) == type(dataFrame.loc[j][i+1]):
                activitiesOfWeek += str (dataFrame.loc[j][i+1]) + ", "

        activitiesOfWeek = activitiesOfWeek[:-2]        
        activitiesOfWeek += "\n"

    return activitiesOfWeek       


def automateFillForm(activities):
    email = ''
    passWord = ''
    day = datetime.now().day
    day = str(day)
    month = datetime.now().month
    month = str(month)
    year = datetime.now().year
    year = str(year)
    browser = webdriver.Chrome()
   
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfcICjPZq5DOYDifFVqiWIDS9mrBs5vSb7-pfmIVZMi5J0gKg/viewform")
    
    pyautogui.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passWord)
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    pyautogui.sleep(10)

    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(day +"/" + month + "/" + year)
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(activities)
    pyautogui.sleep(3)

    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div/span/span').click()
    pyautogui.sleep(3)

automateFillForm(extractData(dataFrame))

    
