import pandas as pd

dataFrame = pd.read_excel('weekly-activities.xlsx')

def extractData(dataFrame):
    dictionary = {"Segunda": [], "Terca": [], "Quarta": [], "Quinta": [], "Sexta": []}
   
    j = -1
    for key in dictionary.keys():
        j += 1
        for i in range(3):
            dictionary[key].append(dataFrame.loc[j][i+1])


    return dictionary          


def generateText(dictionary):
    resultString = ""
    for key in dictionary.keys():
        resultString += key + " - "
        for activity in dictionary[key]:
            if type(activity) == type(resultString):
                resultString += activity + ", "
        resultString = resultString[:-2]        
        resultString += "\n"

    return resultString


activitiesSequence = generateText(extractData(dataFrame))
print(activitiesSequence)

    
