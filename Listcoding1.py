"""
Program Goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTS fro STRs
3: We need to provide choics to the user
    a. Add more values to the list
    b. Return a value at a specific index

"""
myList = []
uniqueList =[]
def mainProgram():
    while True:
        try:
            print("Hello there! Let's work with lists")
            print("Choose from the follow options. Type a number below")
            choice = input("""1. Add to a list ,
2. Return the value at an index position!
3. Random Search ,
4. Add a bunch of numbers ,
5 linear search ,
6.print my list ,
7. quit  """)
            if choice == "1":
                    addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            elif choice == "4":
                addABunch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                searchItem = input("What are you looking for?  ")
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(searchItem))
            elif choice == "7":
                searchItem = input("What are you looking for?  ")
                result = iterativeBinarySearch(uniqueList, 0, len(uniqueList, int(searchItem))
                    if result != -1:
                        print("your number is at index {}".format(result))
                    else:
                        print("your number isnt here")
            elif choice == "8":
                sortList(myList)
            elif choice == "9":
                printLists()
            else:
                break
        except:
            print("Oopsy Daisy! You made a mistake. Try Again?  ")

def addToList():
    print("Adding to a list, Great Choice!")
    newItem = input("Type an integer here    ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here")
    numToAdd = input("How many integers would you like to add?    ")
    numRange = input("And how high would you like these integers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def sortList(myList):
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
        uniqueList.sort()
        showMe = input("Wanna see your new list?   ")
        if showMe.lower() == "y":
            print(uniqueList)
            
    
def indexValues():
    print("Oooooh! I heard you need a particular piece of data")
    inputPos = input("What index position are you curious about?   ")
    myList[int(indexPos)]

def linearSearch():
    print("We're gonna check out each item on at a time in your list! This sucks.")
    searchItem = input("What you lookin for?    ")
    for x in range (len(myList)):
        if myList [x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2
    else:
        print("Your number isnt here")

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("Would you like sorted or unsorted?  ")
        if whichOne.lower() == "sorted":
            print(uniqueList)

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if uniqueList[mid]< x:
            low = mid + 1

        elif uniqueList[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
    

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("You found it at index position {}".format(mid))
            return mid
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid -1, x)
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, mid, high, x)

    else:
        print("Your number isnt here")

if __name__ == "__main__":
    mainProgram()
