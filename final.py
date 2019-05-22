#----------------------------------------------------------------------------------------#
#NAME: Christina Sadak
#DUE DATE: 3/20/2019 (prototype) & Final Exam Day (final project)
#CLASS: CSCI 431
#PURPOSE: Python Program to evaluate the supplied airline flight data. Analyzes the input file to determine the best circumstances for booking a seat on a flight that will not be cancelled and will deliver you to your destination. Examine the effect of the following: Distance, Carrier, Origin City, Destination City, Aircraft, Month, State, and codistanceBinations of these. The source of the input file is http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=259&DB_Short_Name=Air%20Carriers

#OS - macOS Mojave
#GUI - Tkinter
#PYTHON VERSION - python3
#----------------------------------------------------------------------------------------#

import tkinter as tk #GUI
import pandas as pd #Dataframe
from tkinter import ttk #treeviews

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#BEGIN retrieving initial data
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#retrieve data
data = pd.read_csv('ProjectDataEDITED.csv')
#data = pd.read_csv('CarrierData.csv')

df = pd.DataFrame(data) #sets the dataframe for the entire dataset

#creates lists of each criteria I want the user to be able to search using so I can use these lists to create drop down menus and make other calculations
carrierList = df["CARRIER_NAME"].unique().tolist()
carrierList.sort() #sorted list of unique carriers
originCityList = df["ORIGIN_CITY_NAME"].unique().tolist()
originCityList.sort() #sorted list of unique origin cities
destCityList = df["DEST_CITY_NAME"].unique().tolist()
destCityList.sort() #sorted list of unique destination cities
aircraftList = df["AIRCRAFT_TYPE"].unique().tolist()
monthList = df["MONTH"].unique().tolist()
monthList.sort() #sorted list of unique months
orgStateList = df['ORIGIN_STATE_ABR'].unique().tolist()
orgStateList.sort() #sorted list of unique origin states
destStateList = df['DEST_STATE_ABR'].unique().tolist()
destStateList.sort() #sorted list of unique destination states
distanceList = [] #programmer defined list of distances to match the assignment requirements for breaking the distances down into ranges
distanceList.append("0-99")
distanceList.append("100-199")
distanceList.append("200-299")
distanceList.append("300-399")
distanceList.append("400-499")
distanceList.append("500-999")
distanceList.append("1000-1499")
distanceList.append("1500-1999")
distanceList.append("2000-2499")
distanceList.append("2500-2999")

#declares lists to be uses later
resultsLofL = [] #holds results of user mode searches
bestMonth = [] #holds the list of best months to travel for auto mode
bestAirline = [] #holds list of best airlines
bestOrgCities = [] #holds list of best origin cities
bestDestCities = [] #holds list of best destination cities
bestAircraft = [] #holds list of best aircrafts
bestOrgState = [] #holds list of best origin state
bestDestState = [] #holds list of best destination state
bestDist = [] #holds list of best distance range
bestAirlineInBestMonth = [] #holds list of best airlines in top three best months
bestOrgStInBestMonth = [] #holds best origin cities in the top three best months
bestDestCityInBestMonth = [] #holds best destination citites in top three best months

divider = df.loc[:,'DEPARTURES_PERFORMED'].mean() #calculates the divider to be used in algorithms throughout the rest of the program
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#END retrieving initial data
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#BEGIN auto mode functionality
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Auto mode functionality...
def autoMode():
    print ("Auto Mode.")
    autoWindow = tk.Tk()
    autoWindow.title("Auto Mode")
    autoWindow.geometry("1700x700")

#FUNCTION TO FIND BEST MONTH
    #do not have to do the same algorithm on this criteria because I am not going row by row through dataset
    def findBestMonth(monthL = []):

        deptPerf = monthL.loc[:,'DEPARTURES_PERFORMED'].mean() #gets the average departures performed for the passed month
        deptSch = monthL.loc[:,'DEPARTURES_SCHEDULED'].mean() #gets the avdrage departures scheduled for the passed month
        Avg = deptPerf/deptSch #calculates the avre rate of departures performed ot scheduled
        avgPerc = Avg * 100
        Seats = monthL.loc[:,'SEATS'].mean()
        Score = Avg * Seats

        mMonth = monthL.loc[:, 'MONTH'].mean()

        #gets the month name basedon the month number
        if mMonth == 1:
            monthName = "January"
        elif mMonth == 2:
            monthName = "February"
        elif mMonth == 3:
            monthName = "March"
        elif mMonth == 4:
            monthName = "April"
        elif mMonth == 5:
            monthName = "May"
        elif mMonth == 6:
            monthName = "June"
        elif mMonth == 7:
            monthName = "July"
        elif mMonth == 8:
            monthName = "August"
        elif mMonth == 9:
            monthName = "September"
        elif mMonth == 10:
            monthName = "October"
        elif mMonth == 11:
            monthName = "November"
        else:
            monthName = "December"

        bestMonth.append((Score,monthName, avgPerc, Seats))

    ##CALLS FIND BEST MONTH FUNCTION FOR EACH MONTH
    dfJan = df.loc[df['MONTH'] == 1]
    findBestMonth(dfJan)
    dfFeb = df.loc[df['MONTH'] == 2]
    findBestMonth(dfFeb)
    dfMarch = df.loc[df['MONTH'] == 3]
    findBestMonth(dfMarch)
    dfApril = df.loc[df['MONTH'] == 4]
    findBestMonth(dfApril)
    dfMay = df.loc[df['MONTH'] == 5]
    findBestMonth(dfMay)
    dfJune = df.loc[df['MONTH'] == 6]
    findBestMonth(dfJune)
    dfJuly = df.loc[df['MONTH'] == 7]
    findBestMonth(dfJuly)
    dfAug = df.loc[df['MONTH'] == 8]
    findBestMonth(dfAug)
    dfSept = df.loc[df['MONTH'] == 9]
    findBestMonth(dfSept)
    dfOct = df.loc[df['MONTH'] == 10]
    findBestMonth(dfOct)
    dfNov = df.loc[df['MONTH'] == 11]
    findBestMonth(dfNov)
    dfDec = df.loc[df['MONTH'] == 12]
    findBestMonth(dfDec)

    sortedBestMonth = sorted(bestMonth, reverse=True) #sorts months from highest to lowest score (why score is appended to the list first)

##FIND BEST CARRIERS

    numCarriers = len(carrierList) #gets the number of unique carriers in the dataset

    for x in range(numCarriers): #sets each index in bestAirline list to an empty/zero typle to avoid segmentation faults if I try to get the previous score of a slot that doesn't have anything in it already
        innerTuple = (0,'',0,0)
        bestAirline.append(innerTuple)

    for row in df.itertuples(): #loops through dataframe and determines the best airline

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        originalSeats = row.SEATS
        newSeats = originalSeats/divider
        Score = newAvg * newSeats

        carrierName = row.CARRIER_NAME

        airlineIndex = carrierList.index(carrierName) #gets the index of the carrier from the carrier list to use as the index for where to store scores for that month in the bestAirline list
        prevScore = bestAirline[airlineIndex][0] #gets the current airline's previous score
        newScore = prevScore + Score #adds the previous score to the current score and puts it back in the same index so that a total of the scores per airline can be kept in this way.
        innerTuple = (newScore, carrierName, avgPerc, originalSeats)
        bestAirline[airlineIndex] = innerTuple

    bestAirline.sort(reverse=True)

#FIND BEST ORIGIN CITY

    numOrgCities = len(originCityList)

    for x in range(numOrgCities):
        innerTuple = (0,'',0,0)
        bestOrgCities.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        originCity = row.ORIGIN_CITY_NAME

        originCityIndex = originCityList.index(originCity)
        prevScore = bestOrgCities[originCityIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, originCity, avgPerc, Seats)
        bestOrgCities[originCityIndex] = innerTuple

    bestOrgCities.sort(reverse=True)

#FIND BEST DESTINATION CITY
    numDestCities = len(destCityList)

    for x in range(numDestCities):
        innerTuple = (0,'',0,0)
        bestDestCities.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        destinationCity = row.DEST_CITY_NAME

        destCityIndex = destCityList.index(destinationCity)
        prevScore = bestDestCities[destCityIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, destinationCity, avgPerc, Seats)
        bestDestCities[destCityIndex] = innerTuple

    bestDestCities.sort(reverse=True)

#FIND BEST AIRCRAFT

    numAircrafts = len(aircraftList)

    for x in range(numAircrafts):
        innerTuple = (0,'',0,0)
        bestAircraft.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        aircraftType = row.AIRCRAFT_TYPE

        aircraftIndex = aircraftList.index(aircraftType)
        prevScore = bestAircraft[aircraftIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, aircraftType, avgPerc, Seats)
        bestAircraft[aircraftIndex] = innerTuple

    bestAircraft.sort(reverse=True)

#FIND BEST ORIGIN STATE

    numOrgStates = len(orgStateList)

    for x in range(numOrgStates):
        innerTuple = (0,'',0,0)
        bestOrgState.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        orgState = row.ORIGIN_STATE_ABR

        orgStateIndex = orgStateList.index(orgState)
        prevScore = bestOrgState[orgStateIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, orgState, avgPerc, Seats)
        bestOrgState[orgStateIndex] = innerTuple

    bestOrgState.sort(reverse=True)

#FIND BEST DESTINATION STATE

    numDestStates = len(destStateList)

    for x in range(numDestStates):
        innerTuple = (0,'',0,0)
        bestDestState.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        destState = row.DEST_STATE_ABR

        destStateIndex = destStateList.index(destState)
        prevScore = bestDestState[destStateIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, destState, avgPerc, Seats)
        bestDestState[destStateIndex] = innerTuple

    bestDestState.sort(reverse=True)

#FIND BEST DISTANCE

    for x in range(10):
        innerTuple = (0,'',0,0)
        bestDist.append(innerTuple)

    for row in df.itertuples():

        deptSch = row.DEPARTURES_SCHEDULED
        deptPerf = row.DEPARTURES_PERFORMED

        if deptPerf > deptSch:
            originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

        else: #there were not more flights that took off than were scheduled
            originalAvg = deptPerf/deptSch

        newdeptPerf = deptPerf/divider
        newAvg = newdeptPerf/deptSch

        avgPerc = originalAvg * 100 #original percentage before calculating weight becaue this makes more sense to user
        Seats = row.SEATS
        newSeats = Seats/divider
        Score = newAvg * newSeats

        distance = row.DISTANCE

        #series of if else statements to  get the index of a range of distances to use in the bestDistance array
        if row.DISTANCE > 0 and row.DISTANCE <= 99:
            distanceIndex = 0
            distanceString = "0-99"
        elif row.DISTANCE >= 100 and row.DISTANCE <= 199:
            distanceIndex = 1
            distanceString = "100-199"
        elif row.DISTANCE > 200 and row.DISTANCE <= 299:
            distanceIndex = 2
            distanceString = "200-299"
        elif row.DISTANCE > 300 and row.DISTANCE <= 399:
            distanceIndex = 3
            distanceString = "300-399"
        elif row.DISTANCE > 400 and row.DISTANCE <= 499:
            distanceIndex = 4
            distanceString = "400-499"
        elif row.DISTANCE > 500 and row.DISTANCE <= 999:
            distanceIndex = 5
            distanceString = "500-999"
        elif row.DISTANCE > 1000 and row.DISTANCE <= 1499:
            distanceIndex = 6
            distanceString = "1000-1499"
        elif row.DISTANCE > 1500 and row.DISTANCE <= 1999:
            distanceIndex = 7
            distanceString = "1500-1999"
        elif row.DISTANCE > 2000 and row.DISTANCE <= 2499:
            distanceIndex = 8
            distanceString = "2000-2499"
        else:
            distanceIndex = 9
            distanceString = "2500-2999"

        prevScore = bestDist[distanceIndex][0]
        newScore = prevScore + Score
        innerTuple = (newScore, distanceString, avgPerc, Seats)
        bestDist[distanceIndex] = innerTuple

    bestDist.sort(reverse=True)

#FIND BEST CARRIER AND MONTH

    def findbestCarrinMo(topMonth): #get top carriers for top 3 months

        if topMonth == "January":
            monthNum = 1
        elif topMonth == "February":
            monthNum = 2
        elif topMonth == "March":
            monthNum = 3
        elif topMonth == "April":
            monthNum = 4
        elif topMonth == "May":
            monthNum = 5
        elif topMonth == "June":
            monthNum = 6
        elif topMonth == "July":
            monthNum = 7
        elif topMonth == "August":
            monthNum = 8
        elif topMonth == "September":
            monthNum = 9
        elif topMonth == "October":
                monthNum = 10
        elif topMonth == "November":
            monthNum = 11
        else:
            monthNum = 12

        #creates dataframe for the month that was passed to this function so the best ___ of that month can be calculated
        topMonthdf = df.loc[df['MONTH'] == monthNum]

        numCarriers = len(carrierList)

        for x in range(numCarriers):
            innerTuple = (0,'',0,0)
            bestAirlineInBestMonth.append(innerTuple)

        for row in topMonthdf.itertuples():
            deptSch = row.DEPARTURES_SCHEDULED
            deptPerf = row.DEPARTURES_PERFORMED

            if deptPerf > deptSch:
                originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

            else: #there were not more flights that took off than were scheduled
                originalAvg = deptPerf/deptSch

            newdeptPerf = deptPerf/divider
            newAvg = newdeptPerf/deptSch

            avgPerc = originalAvg * 100
            Seats = row.SEATS
            newSeats = Seats/divider
            Score = newAvg * newSeats

            carrierName = row.CARRIER_NAME

            airlineIndex = carrierList.index(carrierName)
            prevScore = bestAirlineInBestMonth[airlineIndex][0]
            newScore = prevScore + Score
            innerTuple = (newScore, carrierName, avgPerc, Seats)
            bestAirlineInBestMonth[airlineIndex] = innerTuple

        bestAirlineInBestMonth.sort(reverse=True)

#FIND BEST ORIGIN STATE AND MONTH

    def findbestOrgStinMo(topMonth): #get top carriers for top 3 months

        if topMonth == "January":
            monthNum = 1
        elif topMonth == "February":
            monthNum = 2
        elif topMonth == "March":
            monthNum = 3
        elif topMonth == "April":
            monthNum = 4
        elif topMonth == "May":
            monthNum = 5
        elif topMonth == "June":
            monthNum = 6
        elif topMonth == "July":
            monthNum = 7
        elif topMonth == "August":
            monthNum = 8
        elif topMonth == "September":
            monthNum = 9
        elif topMonth == "October":
            monthNum = 10
        elif topMonth == "November":
            monthNum = 11
        else:
            monthNum = 12

        topMonthdf = df.loc[df['MONTH'] == monthNum]

        numOrgStates = len(orgStateList)

        for x in range(numOrgStates):
            innerTuple = (0,'',0,0)
            bestOrgStInBestMonth.append(innerTuple)

        for row in topMonthdf.itertuples():
            deptSch = row.DEPARTURES_SCHEDULED
            deptPerf = row.DEPARTURES_PERFORMED

            if deptPerf > deptSch:
                originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

            else: #there were not more flights that took off than were scheduled
                originalAvg = deptPerf/deptSch

            newdeptPerf = deptPerf/divider
            newAvg = newdeptPerf/deptSch

            avgPerc = originalAvg * 100
            Seats = row.SEATS
            newSeats = Seats/divider
            Score = newAvg * newSeats

            orgState = row.ORIGIN_STATE_ABR

            orgStateIndex = orgStateList.index(orgState)
            prevScore = bestOrgStInBestMonth[orgStateIndex][0]
            newScore = prevScore + Score
            innerTuple = (newScore, orgState, avgPerc, Seats)
            bestOrgStInBestMonth[orgStateIndex] = innerTuple

        bestOrgStInBestMonth.sort(reverse=True)


#FIND BEST DESTINATION CITY AND MONTH

    def findbestDestCityinMo(topMonth): #get top carriers for top 3 months

        if topMonth == "January":
            monthNum = 1
        elif topMonth == "February":
            monthNum = 2
        elif topMonth == "March":
            monthNum = 3
        elif topMonth == "April":
            monthNum = 4
        elif topMonth == "May":
            monthNum = 5
        elif topMonth == "June":
            monthNum = 6
        elif topMonth == "July":
            monthNum = 7
        elif topMonth == "August":
            monthNum = 8
        elif topMonth == "September":
            monthNum = 9
        elif topMonth == "October":
            monthNum = 10
        elif topMonth == "November":
            monthNum = 11
        else:
            monthNum = 12

        topMonthdf = df.loc[df['MONTH'] == monthNum]

        numDestCities = len(destCityList)

        for x in range(numDestCities):
            innerTuple = (0,'',0,0)
            bestDestCityInBestMonth.append(innerTuple)

        for row in topMonthdf.itertuples():
            divider = topMonthdf.loc[:,'DEPARTURES_PERFORMED'].mean()

            deptSch = row.DEPARTURES_SCHEDULED
            deptPerf = row.DEPARTURES_PERFORMED

            if deptPerf > deptSch:
                originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter

            else: #there were not more flights that took off than were scheduled
                originalAvg = deptPerf/deptSch

            newdeptPerf = deptPerf/divider
            newAvg = newdeptPerf/deptSch

            avgPerc = originalAvg * 100
            Seats = row.SEATS
            newSeats = Seats/divider
            Score = newAvg * newSeats

            destCity = row.DEST_CITY_NAME

            destCityIndex = destCityList.index(destCity)
            prevScore = bestDestCityInBestMonth[destStateIndex][0]
            newScore = prevScore + Score
            innerTuple = (newScore, destCity, avgPerc, Seats)
            bestDestCityInBestMonth[destCityIndex] = innerTuple

        bestDestCityInBestMonth.sort(reverse=True)

##PRINT TREEVIEW
    testFrame = tk.Frame(autoWindow)
    testFrame.pack(expand=True, fill='y')

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=10, bd=0, font=('Calibri', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    tree = ttk.Treeview(testFrame)

    tree["columns"]=("one","two","three","four") #main result columns
    tree.column("one", width=300)
    tree.column("two", width=300)
    tree.column("three", width=300)
    tree.column("four", width=300)
    tree.heading("one", text="Chosen Criteria")
    tree.heading("two", text="UNWEIGHTED PERF TO SCH %")
    tree.heading("three", text="UNWEIGHTED SEATS")
    tree.heading("four", text="WEIGHTED SCORE (weighted avg * weighted seats)")

    tree.insert("" , 0, text="")

    def treeInsert(idNum, insertList = []):
        numItems = len(insertList)
        if numItems < 10: #prints the number of result a query has in all green to prevent a seg fault
            for y in range(numItems):
                if insertList[y][2] > 0:
                    tree.insert(idNum, "end", text="", values=(insertList[y][1], insertList[y][2], insertList[y][3],insertList[y][0]), tags=('green',))
        elif len(insertList) >= 10: #color code results if there are more than ten
            for y in range(10):
                if y<3:
                    tree.insert(idNum, "end", text="", values=(insertList[y][1], insertList[y][2], insertList[y][3],insertList[y][0]), tags=('green',))
                elif y>=3 and y<7:
                    tree.insert(idNum, "end", text="", values=(insertList[y][1], insertList[y][2], insertList[y][3],insertList[y][0]), tags=('gold',))
                else:
                    tree.insert(idNum, "end", text="", values=(insertList[y][1], insertList[y][2], insertList[y][3],insertList[y][0]), tags=('red',))

    id1 = tree.insert("", 1, text="Best Month to Fly")
    for x in range(12): #prints for months, the only thng with the need to show 12
        if x<3:
            tree.insert(id1, "end", text="", values=(sortedBestMonth[x][1], sortedBestMonth[x][2],sortedBestMonth[x][3],sortedBestMonth[x][0]), tags=('green',))
        elif x>=3 and x<9:
            tree.insert(id1, "end", text="", values=(sortedBestMonth[x][1], sortedBestMonth[x][2],sortedBestMonth[x][3],sortedBestMonth[x][0]), tags=('gold',))
        else:
            tree.insert(id1, "end", text="", values=(sortedBestMonth[x][1], sortedBestMonth[x][2],sortedBestMonth[x][3],sortedBestMonth[x][0]), tags=('red',))

    id2 = tree.insert("", 2, text="Best Airline to Fly")
    treeInsert(id2, bestAirline)

    id3 = tree.insert("", 3, text="Best Origin City")
    treeInsert(id3, bestOrgCities)

    id4 = tree.insert("", 4, text="Best Destination City")
    treeInsert(id4, bestDestCities)

    id5 = tree.insert("", 5, text="Best Aircraft")
    treeInsert(id5, bestAircraft)

    id6 = tree.insert("", 6, text="Best Distance")
    treeInsert(id6, bestDist)

    id7 = tree.insert("", 7, text="Best Origin State")
    treeInsert(id7, bestOrgState)

    id8 = tree.insert("", 8, text="Best Destination State")
    treeInsert(id8, bestDestState)

    id9 = tree.insert("", 9, text="Best Airlines/Month")
    index = 0
    for index in range(3):
        del bestAirlineInBestMonth[:]
        findbestCarrinMo(sortedBestMonth[index][1])
        tree.insert(id9, "end", text="", values=(sortedBestMonth[index][1]), tags=('black',))
        treeInsert(id9, bestAirlineInBestMonth)

    id10 = tree.insert("", 10, text="Best Origin States/Months")
    for index in range(3): #call this function a couple of times to make sure we get the top ___ for the top 3 months
        del bestOrgStInBestMonth[:]
        findbestOrgStinMo(sortedBestMonth[index][1])
        tree.insert(id10, "end", text="", values=(sortedBestMonth[index][1]), tags=('black',))
        treeInsert(id10, bestOrgStInBestMonth)

    id11 = tree.insert("", 11, text="Best Dest Cities/Months")
    for index in range(3):
        del bestDestCityInBestMonth[:]
        findbestDestCityinMo(sortedBestMonth[index][1])
        tree.insert(id11, "end", text="", values=(sortedBestMonth[index][1]), tags=('black',))
        treeInsert(id11, bestDestCityInBestMonth)

    #uses the tags set in where the display functions are to make each row the correct color
    tree.tag_configure('green', foreground='green')
    tree.tag_configure('gold', foreground='gold')
    tree.tag_configure('red', foreground='red')
    tree.tag_configure('black',background='black', foreground='white')

    tree.pack(expand=True, fill='y')

#-------------------------------------------------------------#
#END auto mode functionality
#-------------------------------------------------------------#
#-------------------------------------------------------------#
#BEGIN user mode functionality
#-------------------------------------------------------------#

###WILL BE COMMENTING MORE BY THE DUE DATE FOR THIS PART...

#User mode functinoality...
def userMode():
    print ("User Mode.")
    userWindow = tk.Tk()
    userWindow.title("User Mode")

    #create dropwdown menus of choices for each available filter the user can pick from#

    #CARRIER DROPDOWN
    carrierSelect =  tk.StringVar(userWindow)
    carrierChoices = carrierList
    carrierSelect.set('--select--')
    dropDown1 = tk.OptionMenu(userWindow, carrierSelect, *carrierChoices)
    dropDown1.config(width = 10, bg = 'Green')
    tk.Label(userWindow, text="Carrier: ").grid(row=1, column=1, padx=10, pady=5)
    dropDown1.grid(row=2, column = 1, padx=10, pady=10)

    #ORIGIN CITY DROPDOWN
    originCitySelect =  tk.StringVar(userWindow)
    originCityChoices = originCityList
    originCitySelect.set('--select--')
    dropDown2 = tk.OptionMenu(userWindow, originCitySelect, *originCityChoices)
    dropDown2.config(width = 10, bg = 'Green')
    tk.Label(userWindow, text="Origin City: ").grid(row=1, column=2, padx=10, pady=5)
    dropDown2.grid(row=2, column = 2, padx=10, pady=10)

    #DEST CITY DROPDOWN
    destCitySelect =  tk.StringVar(userWindow)
    destCityChoices = destCityList
    destCitySelect.set('--select--')
    dropDown3 = tk.OptionMenu(userWindow, destCitySelect, *destCityChoices)
    dropDown3.config(width = 10, bg = 'Green')
    tk.Label(userWindow, text="Destination City: ").grid(row=1, column=3, padx=10, pady=5)
    dropDown3.grid(row=2, column = 3, padx=10, pady=10)

    #MONTH DROPDOWN
    monthSelect =  tk.StringVar(userWindow)
    monthChoices = monthList
    monthSelect.set('--select--')
    dropDown4 = tk.OptionMenu(userWindow, monthSelect, *monthChoices)
    dropDown4.config(width = 10, bg = 'Green')
    tk.Label(userWindow, text="Month: ").grid(row=1, column=4, padx=10, pady=5)
    dropDown4.grid(row=2, column = 4, padx=10, pady=10)

    #DISTANCE DROPDOWN
    distanceSelect =  tk.StringVar(userWindow)
    distanceChoices = distanceList
    distanceSelect.set('--select--')
    dropDown5 = tk.OptionMenu(userWindow, distanceSelect, *distanceChoices)
    dropDown5.config(width = 10, bg = 'Green')
    tk.Label(userWindow, text="Distance: ").grid(row=1, column=5, padx=10, pady=5)
    dropDown5.grid(row=2, column = 5, padx=10, pady=10)

    def noResultsDisplay(): #display none for each column when there are no results to show the user
        tk.Label(userWindow, fg="Red",text= "None").grid(row=7, column=1, padx=10, pady=10)
        tk.Label(userWindow, fg="Red", text= "None").grid(row=7, column=2, padx=10, pady=10)
        tk.Label(userWindow, fg="Red", text= "None").grid(row=7, column=3, padx=10, pady=10)
        tk.Label(userWindow, fg="Red", text= "None").grid(row=7, column=4, padx=10, pady=10)
        tk.Label(userWindow, fg="Red", text= "None").grid(row=7, column=5, padx=10, pady=10)
        tk.Label(userWindow, fg="Red", text= "None").grid(row=7, column=6, padx=10, pady=10)
        tk.Label(userWindow, fg="Red",text= "None").grid(row=7, column=7, padx=10, pady=10)
        return

    def displayTopLabels(): #display these at the top of the results for each criterion
        tk.Label(userWindow, bg="Alice Blue", text="CARRIER").grid(row=6, column=1, padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text="DEPT CITY").grid(row=6, column=2, padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text="DEST CITY").grid(row=6, column=3,  padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text="DIST").grid(row=6, column=4, padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text= "UNWEIGHTED PERF TO SCH %").grid(row=6, column=5, padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text="UNWEIGHTED # SEATS").grid(row=6, column=6, padx=10, pady=10)
        tk.Label(userWindow, bg="Alice Blue", text="WEIGHTED SCORE (weighted avg * weighted seats)").grid(row=6, column=7, padx=10, pady=10)
        return


    #resert user mode from scratch
    def resetOptions():
        userWindow.destroy()
        userMode()
    ###USER IS DONE... CLICKS OK
    def userOK():
        #get the values selected from each drop down by the user
        selectedCarrier = carrierSelect.get()
        selectedOrgCity = originCitySelect.get()
        selectedDestCity = destCitySelect.get()
        selectedMonth = monthSelect.get()
        selectedDistance = distanceSelect.get()

        def userModeDisplay(functionList = []):
            numFlights = len(functionList)
            if numFlights == 0:
                noResultsDisplay() #no results found for criteria

            #prints out results of query color-coded
            if numFlights >= 10:
                for i in range(10):

                    rowNum = i + 7
                    index1 = functionList[i][2]

                    if i < 4:

                        tk.Label(userWindow, fg="Green", text=df.iloc[index1]["CARRIER_NAME"]).grid(row=rowNum, column=1, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text=df.iloc[index1]["ORIGIN_CITY_NAME"]).grid(row=rowNum, column=2, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text=df.iloc[index1]["DEST_CITY_NAME"]).grid(row=rowNum, column=3, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text=df.iloc[index1]["DISTANCE"]).grid(row=rowNum, column=4, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text= functionList[i][1]).grid(row=rowNum, column=5, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text= functionList[i][3]).grid(row=rowNum, column=6, padx=10, pady=10)
                        tk.Label(userWindow, fg="Green", text= functionList[i][0]).grid(row=rowNum, column=7, padx=10, pady=10)
                    elif i >=4 and i<7:
                        tk.Label(userWindow, fg="Gold", text=df.iloc[index1]["CARRIER_NAME"]).grid(row=rowNum, column=1, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text=df.iloc[index1]["ORIGIN_CITY_NAME"]).grid(row=rowNum, column=2, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text=df.iloc[index1]["DEST_CITY_NAME"]).grid(row=rowNum, column=3, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text=df.iloc[index1]["DISTANCE"]).grid(row=rowNum, column=4, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text= functionList[i][1]).grid(row=rowNum, column=5, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text= functionList[i][3]).grid(row=rowNum, column=6, padx=10, pady=10)
                        tk.Label(userWindow, fg="Gold", text= functionList[i][0]).grid(row=rowNum, column=7, padx=10, pady=10)
                    else:
                        tk.Label(userWindow, fg="Red", text=df.iloc[index1]["CARRIER_NAME"]).grid(row=rowNum, column=1, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text=df.iloc[index1]["ORIGIN_CITY_NAME"]).grid(row=rowNum, column=2, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text=df.iloc[index1]["DEST_CITY_NAME"]).grid(row=rowNum, column=3, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text=df.iloc[index1]["DISTANCE"]).grid(row=rowNum, column=4, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text= functionList[i][1]).grid(row=rowNum, column=5, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text= functionList[i][3]).grid(row=rowNum, column=6, padx=10, pady=10)
                        tk.Label(userWindow, fg="Red", text= functionList[i][0]).grid(row=rowNum, column=7, padx=10, pady=10)

            else:
                for i in range(numFlights):
                    rowNum = i + 7
                    index1 = functionList[i][2]

                    tk.Label(userWindow, fg="Green", text=df.iloc[index1]["CARRIER_NAME"]).grid(row=rowNum, column=1, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text=df.iloc[index1]["ORIGIN_CITY_NAME"]).grid(row=rowNum, column=2, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text=df.iloc[index1]["DEST_CITY_NAME"]).grid(row=rowNum, column=3, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text=df.iloc[index1]["DISTANCE"]).grid(row=rowNum, column=4, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text= functionList[i][1]).grid(row=rowNum, column=5, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text= functionList[i][3]).grid(row=rowNum, column=6, padx=10, pady=10)
                    tk.Label(userWindow, fg="Green", text= functionList[i][0]).grid(row=rowNum, column=7, padx=10, pady=10)

            del functionList[:]

##USER PICKED ONLY A MONTH
        if selectedMonth != "--select--" and selectedCarrier == "--select--" and selectedDestCity == "--select--" and selectedOrgCity == "--select--" and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            intMonth = int(selectedMonth) #converts the string to an int to search by in the df
            #create new dataframe to hold rows for correct month
            dfMonth = df.loc[df['MONTH'] == intMonth]
            ##loops through the list created for the correct month and evaluates data

            for index in dfMonth.index:

                deptSch = dfMonth['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfMonth['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfMonth['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)

            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED ONLY A CARRIER
        elif selectedMonth == "--select--" and selectedCarrier != "--select--" and selectedDestCity == "--select--" and selectedOrgCity == "--select--" and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
                #create new dataframe to hold rows for correct month

            dfCarrier = df.loc[df['CARRIER_NAME'] == selectedCarrier]

            ##loops through the list created for the correct month and evaluates data
            for index in dfCarrier.index:

                deptSch = dfCarrier['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfCarrier['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfCarrier['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                deptCityName = dfCarrier['ORIGIN_CITY_NAME'][index]
                destCityName = dfCarrier['DEST_CITY_NAME'][index]
                dist = dfCarrier['DISTANCE'][index]

                resultsLofL.append((Score, avgPerc, index, Seats, deptCityName, destCityName, dist))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]

            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED ONLY AN ORIGIN CITY
        elif selectedMonth == "--select--" and selectedCarrier == "--select--" and selectedDestCity == "--select--" and selectedOrgCity != "--select--"  and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            #create new dataframe to hold rows for correct month
            dfOrgCity = df.loc[df['ORIGIN_CITY_NAME'] == selectedOrgCity]
            ##loops through the list created for the correct month and evaluates data
            for index in dfOrgCity.index:

                deptSch = dfOrgCity['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfOrgCity['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfOrgCity['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED ONLY A DESTINATION CITY
        elif selectedMonth == "--select--" and selectedCarrier == "--select--" and selectedDestCity != "--select--" and selectedOrgCity == "--select--" and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            #create new dataframe to hold rows for correct month
            dfDestCity = df.loc[df['DEST_CITY_NAME'] == selectedDestCity]
            ##loops through the list created for the correct month and evaluates data
            for index in dfDestCity.index:

                deptSch = dfDestCity['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfDestCity['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfDestCity['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED ONLY A DISTANCE
        elif selectedMonth == "--select--" and selectedCarrier == "--select--" and selectedDestCity == "--select--" and selectedOrgCity == "--select--" and selectedDistance != "--select--":
            displayTopLabels()
            def bestFlightsinDist(passedList = []):
                for index in passedList.index:

                    deptSch = passedList['DEPARTURES_SCHEDULED'][index]
                    deptPerf = passedList['DEPARTURES_PERFORMED'][index]

                    if deptPerf > deptSch:
                        originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                    else: #there were not more flights that took off than were scheduled
                        originalAvg = deptPerf/deptSch

                    newdeptPerf = deptPerf/divider
                    newAvg = newdeptPerf/deptSch

                    avgPerc = originalAvg * 100

                    Seats = passedList['SEATS'][index]
                    newSeats = Seats/divider
                    Score = newAvg * newSeats

                    resultsLofL.append((Score, avgPerc, index, Seats))

                sortedResults  = sorted(resultsLofL, reverse=True)
                userModeDisplay(sortedResults)
                del sortedResults[:]
                del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quittingfor index in dfDestCity.index:


            if selectedDistance == "0-99":
                min=0
                max=99
                dfDistance = df[(df['DISTANCE'] > 0) & (df['DISTANCE'] <= 99)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "100-199":
                min=100
                max=199
                dfDistance = df[(df['DISTANCE'] > 99) & (df['DISTANCE'] <= 199)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "200-299":
                min=200
                max=299
                dfDistance = df[(df['DISTANCE'] > 199) & (df['DISTANCE'] <= 299)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "300-399":
                min=300
                max=399
                dfDistance = df[(df['DISTANCE'] > 299) & (df['DISTANCE'] <= 399)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "400-499":
                min=400
                max=499
                dfDistance = df[(df['DISTANCE'] > 399) & (df['DISTANCE'] <= 499)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "500-999":
                min=500
                max=999
                dfDistance = df[(df['DISTANCE'] > 499) & (df['DISTANCE'] <= 999)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "1000-1499":
                min=1000
                max=1499
                dfDistance = df[(df['DISTANCE'] > 999) & (df['DISTANCE'] <= 1499)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "1500-1999":
                min=1500
                max=1999
                dfDistance = df[(df['DISTANCE'] > 1499) & (df['DISTANCE'] <= 1999)]
                bestFlightsinDist(dfDistance)
            elif selectedDistance == "2000-2499":
                min=2000
                max=2499
                dfDistance = df[(df['DISTANCE'] > 1999) & (df['DISTANCE'] <= 2499)]
                bestFlightsinDist(dfDistance)
            else:
                min=2500
                max=2999
                dfDistance = df[(df['DISTANCE'] > 2499) & (df['DISTANCE'] <= 2999)]
                bestFlightsinDist(dfDistance)

##USER PICKED A MONTH AND A CARRIER
        elif selectedMonth != "--select--" and selectedCarrier != "--select--" and selectedDestCity == "--select--" and selectedOrgCity == "--select--"  and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            intMonth = int(selectedMonth) #converts the string to an int to search by in the df
            #create new dataframe to hold rows for correct month
            dfMonthCarrier = df[(df['MONTH'] == intMonth) & (df['CARRIER_NAME'] == selectedCarrier)]
            ##loops through the list created for the correct month and evaluates data
            for index in dfMonthCarrier.index:

                deptSch = dfMonthCarrier['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfMonthCarrier['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfMonthCarrier['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED A MONTH AND A CARRIER AND A DESTINATION  CITY

        elif selectedMonth != "--select--" and selectedCarrier != "--select--" and selectedDestCity != "--select--" and selectedOrgCity == "--select--"  and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            intMonth = int(selectedMonth) #converts the string to an int to search by in the df
            #create new dataframe to hold rows for correct month
            dfMonthCarrierDest = df[(df['MONTH'] == intMonth) & (df['CARRIER_NAME'] == selectedCarrier) & (df['DEST_CITY_NAME'] == selectedDestCity)]
            ##loops through the list created for the correct month and evaluates data
            for index in dfMonthCarrierDest.index:

                deptSch = dfMonthCarrierDest['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfMonthCarrierDest['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfMonthCarrierDest['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

##USER PICKED A MONTH AND A CARRIER AND A DESTINATION  CITY AND AN ORIGIN CITY

        elif selectedMonth != "--select--" and selectedCarrier != "--select--" and selectedDestCity != "--select--" and selectedOrgCity != "--select--"  and selectedDistance == "--select--":
            displayTopLabels()
            index = 0
            index1 = 0
            intMonth = int(selectedMonth) #converts the string to an int to search by in the df
            #create new dataframe to hold rows for correct month
            dfMonthCarrierDestOrg = df[(df['MONTH'] == intMonth) & (df['CARRIER_NAME'] == selectedCarrier) & (df['DEST_CITY_NAME'] == selectedDestCity) & (df['ORIGIN_CITY_NAME'] == selectedOrgCity)]
            ##loops through the list created for the correct month and evaluates data
            for index in dfMonthCarrierDestOrg.index:

                deptSch = dfMonthCarrierDestOrg['DEPARTURES_SCHEDULED'][index]
                deptPerf = dfMonthCarrierDestOrg['DEPARTURES_PERFORMED'][index]

                if deptPerf > deptSch:
                    originalAvg = 1 #sets departure percentage to 1 if it would have been greater than 1 because a user cannot book a flight that wasn't scheduled so the higher percentage doesn't matter
                else: #there were not more flights that took off than were scheduled
                    originalAvg = deptPerf/deptSch

                newdeptPerf = deptPerf/divider
                newAvg = newdeptPerf/deptSch

                avgPerc = originalAvg * 100

                Seats = dfMonthCarrierDestOrg['SEATS'][index]
                newSeats = Seats/divider
                Score = newAvg * newSeats

                resultsLofL.append((Score, avgPerc, index, Seats))

            sortedResults  = sorted(resultsLofL, reverse=True)
            userModeDisplay(sortedResults)
            del sortedResults[:]
            del resultsLofL[:] #clear resultsLoL so it doesnt get built on if user runs multiple times without quitting

        else:
            tk.Label(userWindow, fg="Red", text= "Can't perform that combination. Sorry!").grid(row=7, column=3, padx=10, pady=10)


    okayB = tk.Button(userWindow, text="FIND FLIGHTS", command=userOK)
    okayB.grid(row=4, column=3, padx=10, pady=20)

    resetB = tk.Button(userWindow, text="RESET OPTIONS", command=resetOptions)
    resetB.grid(row=4, column=4, padx=10, pady=20)

#-------------------------------------------------------------#
#END user mode functionality
#-------------------------------------------------------------#
#-------------------------------------------------------------#
#BEGIN main window
#-------------------------------------------------------------#

window = tk.Tk()

window.title("CSCI 431 - Project")

buttonFrame = tk.Frame(window)
buttonFrame.pack(expand=True, fill='y')

#ask user to select application mode (user or auto)
#auto mode (MODE 1)
autoModeB = tk.Button(buttonFrame, text="Auto Mode", fg="Black", command=autoMode)
autoModeB.config(width=10, height=5)
autoModeB.pack(padx=5, pady=10, side=tk.LEFT)

#user mode (MODE 2)
userModeB = tk.Button(buttonFrame, text="User Mode", fg="Black", command=userMode)
userModeB.config(width=10, height=5)
userModeB.pack(padx=5, pady=10, side=tk.LEFT)

#button to quit the application
quitB = tk.Button(buttonFrame, text="Quit", fg="red", command=quit)
quitB.config(width=10, height=5)
quitB.pack(padx=5, pady=10, side=tk.LEFT)

window.mainloop() #generates window

#-------------------------------------------------------------#
#END main window
#-------------------------------------------------------------#
