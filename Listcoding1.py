"""
Program Goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTS fro STRs
3: We need to provide choics to the user
    a. Add more values to the list
    b. Return a value at a specific index

"""
myList = []
def mainProgram():
    while True:
        try:
            print("Hello there! Let's work with lists")
            print("Choose from the follow options. Type a number below")
            choice = input("1. Add to a list , 2. Return the value at an index position! 3. Random Search , 4. Add a bunch of numbers , 5 linear search , 6.print my list , 7. quit  ")
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
                print(myList)
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

if __name__ == "__main__":
    mainProgram()
