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
            choice = input("1. Add to a list , 2. Return the value at an index position! 3. Quit    ")
            if choice == "1":
                    addToList()
            elif choice == "2":
                    indexValues()
            elif choice == "3":
                randomSearch()
            else:
                break
        except:
            print("Oopsy Daisy! You made a mistake. Try Again?  ")
            #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition

def addToList():
    print("Adding to a list, Great Choice!")
    newItem = input("Type an integer here    ")
    myList.append(int(newItem))

def indexValues():
    print("Oooooh! I heard you need a particular piece of data")
    inputPos = input("What index position are you curious about?   ")
    myList[int(indexPos)]



if __name__ == "__main__":
    mainProgram()
