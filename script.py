from selenium import webdriver
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


'''def automateFillForm(activities):
    browser = webdriver.Chrome()
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfcICjPZq5DOYDifFVqiWIDS9mrBs5vSb7-pfmIVZMi5J0gKg/viewform")

    pyautogui.sleep(5)'''



    
