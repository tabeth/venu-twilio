#-- Reads the Valentine Website and categorizes information --#

import urllib2
import time



def main():
    createMenu('Breakfast')

def stripdata(string):
    # Removes the code from the text.
    #if ('&lt;br&gt;' in string):
    string = string.replace('&lt;br&gt;', ',  ')

    string = string.replace('&quot;Pizza &amp; Pasta Bar&quot;', 'Pizza &amp; Pasta Bar')
    string = string.replace('&amp;', '&')
    string = string.replace('&apos;', '\'')
    #string = string.replace('<description>', '')

    while ('&lt;' or '&gt;') in string:
        string =  string[0:string.index('&lt;')] + string[string.index('&gt;')+4:]
        
    return(string)

def verifytolist(string):
    #Verifies the list:
    grill = 'Grill:'
    grilllst = []
    pastry = 'Pastry Selection:'
    pastrylst = []
    soup = 'Soup:'
    souplst = []
    lighter = 'Lighter Side:'
    lighterlst = []
    traditional = 'Traditional:'
    traditionallst = []
    deli = 'Deli:'
    delilst = []
    pasta = 'Pasta:'
    pastalst = []
    pizza = 'Pizza:'
    pizzalst = []
    salad = 'Salads:'
    saladlst = []
    bread = 'Pastry and Bread:'
    breadlst = []
    checklistlst = [grilllst, pastrylst, souplst, lighterlst, traditionallst, delilst, pastalst, pizzalst, breadlst, saladlst]
    checklist = [grill, pastry, soup, lighter, traditional, deli, pasta, pizza, bread, salad]
    
    #Takes the string, converts it into a list and parses it
    lst = string.split(',  ')

    #Take the raw data, add into separate lists.
    go = False
    
    # A list with the locations of where items in checklist appear in lst
    sequence = []
    for i in range(len(lst)):
        if '<description>' in lst[i]:
           lst[i] = lst[i].replace('<description>', '')
        for j in range(len(checklist)):
            if checklist[j] in lst[i]:
                sequence.append(i)

    sequence.append(len(lst))
    
    for k in range(len(sequence)-1):
        checklistlst[k] = lst[sequence[k]:sequence[k+1]]

    #Secondary clean up
    for count in range(len(checklistlst), 0, -1):
        if count > 1 and checklistlst[count-1] == []:
            checklistlst.pop(count-1)



    #Final clean up, erases the indicators , 'Soup:, etc'
    #for a in range(len(checklistlst)):
    #   for b in range(len(checklistlst[a])):
    #       for c in range(len(checklist)):
    #            if checklist[c] in checklistlst[a][b]:
    #                checklistlst[a][b] = checklistlst[a][b].replace(str(checklist[c]) + ' ', '')
                
                                 

    return checklistlst

def createMenu(menuName):
    if menuName == 'Breakfast':
        breakfast = ''
        rawdata = urllib2.urlopen("http://www3.amherst.edu/intranet/valentine/rss.xml")
        rawdata = str(rawdata.read())
        breakfastmenu = rawdata[findIt(rawdata, '<description>', 2):findIt(rawdata, '</description>', 2)]
        breakfastmenu = stripdata(breakfastmenu)
        breakfastmenu = verifytolist(breakfastmenu)
        return breakfastmenu

    if menuName == 'Lunch':
        lunch = ''
        rawdata = urllib2.urlopen("http://www3.amherst.edu/intranet/valentine/rss.xml")
        rawdata = str(rawdata.read())
        lunchmenu = rawdata[findIt(rawdata, '<description>', 3):findIt(rawdata, '</description>', 3)]
        lunchmenu = stripdata(lunchmenu)
        lunchmenu = verifytolist(lunchmenu)
        return lunchmenu
    
    if menuName == 'Dinner':
        dinner = ''
        rawdata = urllib2.urlopen("http://www3.amherst.edu/intranet/valentine/rss.xml")
        rawdata = str(rawdata.read())
        dinnermenu = rawdata[findIt(rawdata, '<description>', 4):findIt(rawdata, '</description>', 4)]
        dinnermenu = stripdata(dinnermenu)
        dinnermenu = verifytolist(dinnermenu)
        return dinnermenu



def menu(menuName, number):
    if menuName == 'Breakfast':
        LIST = BREAKFAST

    elif menuName == 'Lunch':
        LIST = LUNCH  

    elif menuName == 'Dinner':
        LIST = DINNER
        
    themenu = ""

    try:
        themenu = (", ".join(str(e) for e in LIST[number]))
        themenu = themenu.replace("'", '')

    except Exception:
        pass

    return themenu

def findIt(lst, item, occurence):
    count = 1
    totalIndex = 0
    temp1 = ''
    temp2 = ''

    if occurence == 1:
        return lst.index(item)

    while count != occurence:
        temp1 = '*' * (lst.index(item)+len(item))

        temp2 = lst[(lst.index(item)+len(item)):]

        lst = temp1 + temp2
        count = count + 1
        totalIndex = lst.index(item)

    return totalIndex

BREAKFAST = createMenu('Breakfast')
LUNCH = createMenu('Lunch')
DINNER = createMenu('Dinner')
