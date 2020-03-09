def getBudget(c):
    if(c == 1):
        return 0.5
    elif(c == 2):
        return 1.5
    elif(c ==3):
        return 2.5

def getPlaceType(p):
    if(p == 1):
        return "historical"
    elif(p == 2):
        return "hill station"
    elif(p ==3):
        return "desert"
    elif(p == 4):
        return "beach"

def getPopDen(b):
    if(b == 1):
        return "high"
    elif(b == 2):
        return "low"

def getClimate(c):
    if(c == 1):
        return "cold"
    elif(c == 2):
        return "moderate"
    elif(c ==3):
        return "hot"

def getGov(g):
    if(g == 1):
        return "democracy"
    elif(g == 2):
        return "communist"
    elif(g ==3):
        return "monarchy"
    elif(g == 4):
        return "republic"
    elif(g ==5):
        return "federal"

def getReligion(r):
    if(r == 1):
        return "christianity"
    elif(r == 2):
        return "buddhism"
    elif(r ==3):
        return "hinduism"
    elif(r == 4):
        return "islam"
    elif(r ==5):
        return "atheist"

def getWorkType(w):
    if(w==1):
        return "bussiness"
    else:
        return "job"

def getImpExp(xa):
    if xa == 1:
        return "import"

    elif xa == 2:
        return "export"

def getField(fdomain):
    if fdomain == 1:
        return "technology"

    elif fdomain == 2:
        return "manufacturing"

    elif fdomain == 3:
        return "tourism"

    elif fdomain == 4:
        return "infrastructure"

