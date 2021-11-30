# In addition to the main function, your code must include the following functions:
# Function 1 - displayTitle
# A function that displays the title - "Air Conditioning Window Unit Cooling Capacity"
# Function 2 – calculateArea
# A function that accepts the length and width of a room as arguments, and calculates and returns the area of the room
# Function 3 – translateShadeChoiceToString
# A function that accepts an integer value (1, 2, or 3) that denotes the amount of shade.  The function should return the appropriate String representation of the shade.
# For example, if the function is passed an integer value of 1, it should return a String with a value of “Little”.
# Function 4 - calculateBTUsPerHour
# A function that accepts the area of a room and the amount of shade a room gets and returns the BTUs per Hour that are needed to adequately cool that room.
# Function 5 - displayRoomInformation
# A function that prints out the information for a single room.  The output should look exactly the same as the output for Project 2.  
# The function should accept only the arguments necessary to print out the information.
# All functions should be written as described above.  
# At the end of the output, in the main function, the program should display the number of rooms that have been entered.

# main function keeps the program running and display the number of rooms that have been entered.
def main():
    # prompt the user to enter the name of the room that they are entering information for.    
    choice = "Y"
    count = 0
    # while loop to keep track of number of rooms
    displayRoomInformation()
    while choice == "y" or choice == "Y":  
        count += 1   
        choice = input(
            "\nWould you like to enter information for another room (Y/N)? ")
        if choice == "y" or choice == "Y":
            displayRoomInformation()
            continue
        else:
            choice = "n"
            print("\nThe total number of rooms processed was: ", count)
            input('Press ENTER to exit')
            break  
    
# This function displays the title
def displayTitle():
    print("Air Conditioning Window Unit Cooling Capacity")
    
# Function accepts the length and width of a room and calculates and returns the area of the room
def calculateArea():   
    # Ask the user to enter the length of their room (in feet).
    length = float(input("Enter the length of the room (in feet) "))
    while length < 5:
        print("The length of the room cannot be less than 5 feet")
        length = float(input("Enter the length of the room (in feet) "))
    # Ask the user to enter the width of their room (in feet).
    width = float(input("Enter the width of the room (in feet) "))
    while width < 5:
        print("The width of the room cannot be less than 5 feet")
        width = float(input("Enter the width of the room (in feet) "))
    # Calculate the area (in square feet) of the room by multiplying the length and the width of the room
    roomArea = length * width        
    return roomArea

# accepts an integer value (1, 2, or 3) that denotes the amount of shade. Return the appropriate String representation of the shade.
def translateShadeChoiceToString():
    print("\nWhat is the amount of shade that this room receives?")
    print("1.Little Shade")
    print("2.Moderate Shade")
    print("3.Abundant Shade")
    # While loop to validate the input on shade option
    while True:
        try:
            shade = int(input("Please select the options from above: "))
        except ValueError:
            print("Your choice must be an integer")
            continue
        if shade not in (1, 2, 3):
            print(
                "The user's menu selection for the amount of shade should be 1, 2, or 3")
        if shade == 1:
            shade = "Little"            
        elif shade == 2:
            shade = "Moderate"            
        elif shade == 3:
            shade = "Abundant"            
        else:
            continue                  
        return shade

# Accepts the area of a room and the amount of shade a room gets and returns the BTUs per Hour that are needed to adequately cool that room.
def calculateBTUsPerHour(shade, roomArea):
    print()   
    displayTitle()
    if shade == "Moderate":  # Determine the capacity of the air conditioning unit that is needed for a Moderate shaded room       
        if roomArea < 250:
            capacity = 5500            
        elif roomArea < 501:
            capacity = 10000            
        elif roomArea <= 1000:
            capacity = 17500            
        else:
            capacity = 24000            
    elif shade == "Little":  # Determine the capacity of the air conditioning unit that is needed for a Little shaded room        
        if roomArea < 250:
            capacity = 5500 * 0.15 + 5500            
        elif roomArea < 501:
            capacity = 10000 * 0.15 + 10000            
        elif roomArea <= 1000:
            capacity = 17500 * 0.15 + 17500            
        else:
            capacity = 24000 * 0.15 + 24000            
    elif shade == "Abundant":  # Determine the capacity of the air conditioning unit that is needed for a Abundant shaded room        
        if roomArea < 250:
            capacity = 5500 - (0.10 * 5500)            
        elif roomArea < 501:
            capacity = 10000 - (0.10 * 10000)            
        elif roomArea <= 1000:
            capacity = 17500 - (0.10 * 17500)            
        else:
            capacity = 24000 - (0.10 * 24000)
    return capacity

# Prints out the information for a single room. 
def displayRoomInformation():    
    name = (input("Please enter the name of the room: "))
    roomArea = calculateArea()
    shade = translateShadeChoiceToString()
    capacity = calculateBTUsPerHour(shade, roomArea)
    print("\nRoom Name: ", name)
    print("Room Area (in square feet):", roomArea)
    print("Amount of Shade: ", shade)
    print("BTU's Per Hour needed:", "{:,}".format(capacity))

if __name__ == "__main__":
    main()
