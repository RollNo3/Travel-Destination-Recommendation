import zipfile, io, re, csv, sys


def getTourism():
    tourism = {}
    placeList = []
    f = open("Tourism.csv")
    try:
        reader = csv.reader(f)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].lower()
            placeList.append(row)
    finally:
        f.close()

    l = len(placeList)
    for i in range(1, l):
        tourism[placeList[i][0]] = {}

    for i in range(1, l):
        for j in range(len(placeList[0])):
            if placeList[0][j] != "" and placeList[i][j] != "":
                tourism[placeList[i][0]][placeList[0][j]] = placeList[i][j]

    return tourism

def getCountryDetails():
    countryDetails = {}
    countryList = []
    f = open("countries.csv")
    try:
        reader = csv.reader(f)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].lower()
            countryList.append(row)
    finally:
        f.close()

    l = len(countryList)
    for i in range(1, l):
        countryDetails[countryList[i][0]] = {}

    for i in range(1, l):
        for j in range(len(countryList[0])):
            if countryList[0][j] != "" and countryList[i][j] != "":
                countryDetails[countryList[i][0]][countryList[0][j]] = countryList[i][j]

    return countryDetails
