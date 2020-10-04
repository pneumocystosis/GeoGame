import csv
import random as rd
import time as t
score = 0
inscore = 0
answer = ""
staus = ""
listcountries, listcapitals, listcontinents = [], [], []
#open file and setup
with open(r"C:\Users\hugop\1_NSI\jeu capitals\country-capitals.csv") as f:
    csv_reader = csv.reader(f)
    line_count = 0
    list1 = list(csv.reader(f))
    for j in range (1,len(list1)):
        listcountries.append(list1[j][0])
        listcapitals.append(list1[j][1])
        listcontinents.append(list1[j][5])
    lenlist = len(list1)
    f.close()

#loop for game
while answer != "STOP":
    countryno = rd.randint(1,lenlist-2)
    country = listcountries[countryno]
    capital = listcapitals[countryno]
    continent = listcontinents[countryno]
    print("What's the capital of "+country+", "+continent+"?")
    answer = input().upper()
    if answer != "STOP":
        if answer == capital.upper():
            score += 1
            print("Correct!\nScore: {}\n".format(score))
            t.sleep(0.3)
        else:
            inscore += 1
            print("Incorrect!\nThe correct answer was {}\nScore: {}\n".format(capital, score))
            t.sleep(0.3)
if score - inscore <= -4:
    status = "Appaling!"
elif score - inscore >=  -3 and score - inscore <= 5:
    status = "Meh"
else:
    status = "Great!"
t.sleep(0.5)
print("Overview:\nCorrect answers: {}\nIncorrect answers: {}\n{}".format(score, inscore, status))
input()
