#Will Meyer
#Programing Project Design: Airline Flight
#Nov 16, 2018
#CSC 110

def getData():
    #Open file with error detection
    goodName= False
    while goodName== False:
        fname = input("enter file name: ")
        try:
            fileName=open(fname, "r")
            
            goodName = True
        except IOError:
            print("Invalid file name, Please try again...")

    #initialize lists for data (airlineList, flightNumList,departT, arivT, price )
    airlineList = []
    flightNumList = []
    departTimeList = []
    arrivalTimeList = []
    priceList = []
    
    #Read file line by line and append data to corrresponding list
    for line in fileName:
        line= line.strip()
        airline, flight, depart, arrival, price= line.split(',')
        price = price.strip('$')
        airlineList.append(str(airline))
        flightNumList.append(int(flight))
        departTimeList.append(depart)
        arrivalTimeList.append(str(arrival))
        priceList.append(int(price))


    fileName.close()
    
    #return lists
    return airlineList, flightNumList, departTimeList, arrivalTimeList, priceList
    
    
    
    


def findSpecF(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    #Ask the user to input airline and flight number
    flight = str(input("Enter Airline: "))
    number = int(input("Enter Flight Number: "))
    

    #If it is in the list print the remaining data stored on that flight
    for i in range(len(flightNumList)):
        if number == flightNumList[i] and flight == airlineList[i]:
            print ( airlineList[i])
            print (flightNumList[i])
            print (departTimeList[i])
            print (arrivalTimeList[i])
            print(priceList[i])
            return
    #if airline or flightN are not in corresponding lists try again     
    else:
            print("this flight does not exist try again")
                  
    

def findCheaperPrice(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    #ask user to enter a price threshold
    threshold = int(input("Enter a Price threshold: "))
    
                   
    #loop through price list and store index of prices cheaper
    for i in range(len(priceList)):      
        if threshold >= priceList[i]:
            #print remaining information of flights at the corresponding index
            print(airlineList[i],flightNumList[i],departTimeList[i],arrivalTimeList[i],priceList[i])       
            if i == len(priceList)-1:
              return
        
    else:
        print("No More flights cheaper than this price")
    
    

def findLongflight(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    #find difference between depart and arrival time for corresponding flights
    flights_T_List=[]
    for i in range(len(departTimeList)):
        hours, minutes =  departTimeList[i].split(':')
        time = (int(hours)*60) + (int(minutes))
        hours_2, minutes_2 = arrivalTimeList[i].split(':')
        time_2 = (int(hours_2)*60)+(int(minutes_2))
        flights_t = time_2 - time
        flights_T_List.append(flights_t)
   
    longFlightTime= flights_T_List[0]
    #Compare total time (minutes) and find the highest one
    for i in range(len(flights_T_List)):
        if flights_T_List[i] > longFlightTime:
            longFlightTime = flights_T_List[i]
            longFlightA = airlineList[i]
            longFlightNum = flightNumList[i]
            longFlightD = departTimeList[i]
            longFlightArr = arrivalTimeList[i]
            longFlightP = priceList[i]
    #print Corresponding information about longest flight        
    print("Longest Flight is :",longFlightA, longFlightNum, longFlightD,longFlightArr,longFlightP)  
                   
    

def findArrivT(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    arrivalTimes_M=[]
    for i in range(len(arrivalTimeList)):
        hours, minutes = arrivalTimeList[i].split(':')
        time = (int(hours)*60)+(int(minutes))
        arrivalTimes_M.append(time)
    earliestA = arrivalTimes_M[0]
    for i in range(len(arrivalTimes_M)):
        if earliestA > arrivalTimes_M[i]:
            earliestA= arrivalTimes_M[i]       

    #Ask user to enter a time they would like to arrive before
    
    userInput_M=[]
    flights_before=[]
    
    good = False
    while good == False:
        time_thres = input("Enter time you would like to arrive before in the following format HH:MM :")
        
        try:
            hours_I, minutes_I =  time_thres.split(':')
            time_I = (int(hours_I)*60) + (int(minutes_I))
                
            if time_I >= earliestA:
                for i in range(len(arrivalTimes_M)):
                    if time_I >= arrivalTimes_M[i]:
                        print(airlineList[i], flightNumList[i], departTimeList[i], arrivalTimeList[i], priceList[i])
                        good == True
                    if i == len(arrivalTimes_M)-1:
                        return
            else:
                print("NO flights arriving earlier than that time")
                        
        except ValueError:
            print("invalid Time try again")
                
                
def avgPricePerAirline(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    #Ask user to enter an airline
    user_airline = str(input("Enter the Airline you are looking for the average price of: "))
    #store all prices of flights from that airline into a variable
    counter= 0
    priceCounter = 0
    for i in range(len(airlineList)):
        if user_airline == airlineList[i]:
            counter +=1
            priceCounter = priceCounter + priceList[i]
    if user_airline not in airlineList:
        print("invalid Airline")
    if counter >= 1:
        print("The average price for that airline is", (priceCounter)/(counter))
    
    #divide by the number of flights
    #Return the average cost

def sortDepart(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList):
    #Set first depart time as earliest
    flights_T_List=[]

    for i in range(len(departTimeList)):
        hours, minutes =  departTimeList[i].split(':')
        time = (int(hours)*60) + (int(minutes))
        flights_T_List.append(time)
        
    for i in range(len(flights_T_List)):
        j = i
        for k in range(i + 1, len(flights_T_List)):
            # comparison
            if flights_T_List[k] < flights_T_List[j]:
                j = k
                
        flights_T_List[i], flights_T_List[j] = flights_T_List[j], flights_T_List[i]
        airlineList[i], airlineList[j] = airlineList[j], airlineList[i]
        flightNumList[i],flightNumList[j] = flightNumList[j],flightNumList[i]
        departTimeList[i],departTimeList[j] = departTimeList[j],departTimeList[i]
        arrivalTimeList[i],arrivalTimeList[j]=arrivalTimeList[j], arrivalTimeList[i]
        priceList[i],priceList[j] = priceList[j], priceList[i]
        
       
 
        
        
    
    fname = input("enter outfile name: ")

    fileName=open(fname, "w")
    for i in range(len(airlineList)):
        fileName.write(airlineList[i]+','+ str(flightNumList[i])+','+ departTimeList[i]+',' + arrivalTimeList[i] +','+ str(priceList[i])+'\n')
    #Loop through deaprt times
    #If depart time is earlier than previous ealiest time append it to the list
    #Returned ordered lists

def main():
    #call all functions
    airlineList, flightNumList, departTimeList, arrivalTimeList, priceList = getData()

    user_req = 0
    while user_req != 7:
        print("Please choose from the following options:")
        print("1-- Find Flight information by airline and flight number")
        print("2-- To find Flights Cheaper than a certain threshold: ")
        print("3-- To find Longest Flights")
        print("4-- To find A Flight arriving before a certain time")
        print("5-- To find the Average price per flight for a certain Airline")
        print("6-- To sort Flights by Departure time")
        print("7--Quit")
        user_req = int(input("Enter the number corresponding to the information your for: "))
                             
        #ask for all user inputed values to be used in functions
        if user_req == 1:
            findSpecF(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)
           
        elif user_req == 2:
            findCheaperPrice(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)
           
        elif user_req == 3:
            findLongflight(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)

        elif user_req == 4:
            findArrivT(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)
           
        elif user_req == 5:
            avgPricePerAirline(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)
            
        elif user_req == 6:
            sortDepart(airlineList, flightNumList, departTimeList, arrivalTimeList, priceList)
        
        elif user_req >7:
            print("Not a Valid option please try again")
        

    if user_req == 7:
        print("Thank you!")
        
        
                


    

    
