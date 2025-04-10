# the function import easygui allows the programer to use the module easygui to make the menu look nice and clean
import easygui

# This is a dictionary which stores all the monster cards and its trait and power
cards = {
    "Stoneling": {
        "strength": 7,
        "speed": 1,
        "stealth": 25,
        "cunning": 15,
    },

    "Vexscream": {
        "strength": 1,
        "speed": 6,
        "stealth": 21,
        "cunning": 19,
    },

    "Dawnmirage": {
        "strength": 5,
        "speed": 6,
        "stealth": 18,
        "cunning": 22,
    },

    "Blazegolem": {
        "strength": 15,
        "speed": 20,
        "stealth": 23,
        "cunning": 6,
    },
    
    "Websnake": {
        "strength": 7,
        "speed": 15,
        "stealth": 10,
        "cunning": 5,
    },

    "Moldvine": {
        "strength": 21,
        "speed": 18,
        "stealth": 14,
        "cunning": 5,
    },

    "Vortexwing": {
        "strength": 19,
        "speed": 13,
        "stealth": 19,
        "cunning": 2,
    },

    "Rotthing": {
        "strength": 16,
        "speed": 7,
        "stealth": 4,
        "cunning": 12,
    },

    "Froststep": {
        "strength": 14,
        "speed": 14,
        "stealth": 17,
        "cunning": 4,
    },

    "Wisphoul": {
        "strength": 17,
        "speed": 19,
        "stealth": 3,
        "cunning": 2,
    },
}


# This will display the monster cards including any added ones and will not display any removed ones
def display_cards(cards):
    # [Message allows us to print mutiple messages at once]
    message = "===============================\n"
    message += "---------Cards display---------\n"
    message += "===============================\n"
    if cards:
        # Card_name is the monster card names such as stoneling, vexscreem, etc 
        # Card_name, details in cards.items() means that details are traits and power in cards_name and cards_name are moster names in in cards
        # then you simply pirnt card_name and and the details in the monster card name
        for cards_name, details in cards.items():
            message += f"\n{cards_name}\n"
            for trait, power in details.items():
                message += f"{trait}: {power}\n"

        message +="-------------------------------\n"
        message +="==============================="

        easygui.msgbox(message, title="Card Display")
    else:
        easygui.msgbox("there are no cards", title="Invaild")
    

# This function allows the user to add a new card to the dictionary if they want to 
def add_cards(cards):
    # This while true will loop if the user puts the wrong value
    while True:
        try:
            user_input = easygui.enterbox("Enter the name of the monster to add to the dictionary:", title="Monster name")
            # if user_input is not inside the dictionary then it will break and continue over
            if not user_input:
                easygui.msgbox("User_input cannot be empty", title="Blank input")
                continue 
            else:
                break
        except ValueError:
            easygui.msgbox("Invaild input! please try agian", title="Inccoret input")
        # To make sure that user_input is capitalized to see if it mactches with any of the combos in the dictionary  
        user_input = user_input.title().strip()


        
            
    # this will store all the detials inside of the new monster card 
    new_traits = {}

    # This function will allow the user to pick the power of strength


    while True:
        try:
            num1 = int(easygui.enterbox(f"Enter the power of strength {user_input} will have!", title="Strength"))
            if not num1:
                easygui.msgbox("User_input cannot be empty", title="Blank input")
                continue 

            if num1 > 25 or num1 < 1:
                easygui.msgbox("Not vaild! has to be less than 25 and more than 1!", title="Inavild input")
            else:
                break

        except ValueError:
            easygui.msgbox("Not Vaild! try again!", title="Invaild input")
            continue
     
    
    # This function will allow the user to pick the power of speed



    while True:
        try:
            num2 = int(easygui.enterbox(f"Enter the power for speed {user_input} will have!: ", title="Speed"))
            if not num2:
                easygui.msgbox("User_input cannot be empty", title="Blank input")
                continue 

            if num2 > 25 or num2 < 1:
                easygui.msgbox("Not vaild! has to be less than 25 and more than 1!", title="Inavild input")
            else:
                break
        except ValueError:
            easygui.msgbox("Not Vaild! try again!", title="Invaild input")
            continue

    # This function will allow the user to pick the power of stealth




    while True:
        try:
            num3 = int(easygui.enterbox(f"Enter the power for stealth {user_input} will have!: ", title="Stealth"))
            if not num3:
                easygui.msgbox("User_input cannot be empty", title="Blank input")
                continue 
            if num3 > 25 or num3 < 1:
                easygui.msgbox("Not vaild! has to be less than 25 and more than 1!", title="Inavild input")
            else:
                break
        except ValueError:
            easygui.msgbox("Not Vaild! try again!", title="Invaild input")


    # This function will allow the user to pick the power of cunning

    

    while True:
        try:
            num4 = int(easygui.enterbox(f"Enter the power for cunning {user_input} will have!:", title="Cunning"))
            if not num4:
                easygui.msgbox("User_input cannot be empty", title="Blank input")
                continue 
            if num4 > 25 or num4 < 1:
                easygui.msgbox("Not vaild! has to be less than 25 and more than 1!", title="Inavild input")
            else:
                break
        except ValueError:
            easygui.msgbox("Not Vaild! try again!", title="Invaild input")


    # in the dictionary inside the user_input the strength will be num1, speed will be num2, stealth will num3, cunning will be num4 
    # Adding all the things 

    cards[user_input]= {
        "Strength": num1,
        "Speed": num2,
        "Stealth": num3,
        "Cunning": num4
    }

    # this will print out a message saying your combo had been added
    easygui.msgbox("Your Monster is now inside the dictionary! Go to display to look at it!", title="COmbo added")


# This will look for any of the cards that the user asked for
def search_cards(cards):
    # This ask for the card the user wants to search for
    user_input = easygui.enterbox("Enter the name of the monster you are looking for:")

    # This will make sure that user_input is capitalized and if the card does not exist it will print out the other message
    user_input = user_input.strip().title()

    # if card does it exsit it will find and print the card
    if user_input in cards:
        message = "=================\n"
        message += "-----------------\n"
        # user_input will be printed because thats the name of the monster card
        message += f"{user_input}\n"
        # details equals the details inside user_input and user_input = details inside of cards
        details = cards[user_input]
        for trait, power in details.items():
            message += f"{trait}: {power}\n"
        message += "-----------------\n"
        message += "=================\n"

        # prints the message above and the title
        easygui.msgbox(message, title="Search found")
    else:
        # prints monster card not found and title if monster is not inside of dictionary
        easygui.msgbox("Monster card not found!", title="Search not found")

# This will remove any exisiting card that user wants to remove
def remove_cards(cards):
    # this is asking for users input to remove the card they want
    user_input = easygui.enterbox("Enter the monster card you want to remove!")

    # capitalize the user_input to make sure that the monster card exists
    user_input = user_input.strip().title()

    # if monster card exist it will be remove it useing the unction del cards[user_input]
    if user_input in cards:
        del cards[user_input]
        # prints Monster card has been deleted
        easygui.msgbox("Monster card has been deleted")
        # if user_input not found it will print monster card not found
    else:
        easygui.msgbox("Monster card not found!")

# This will allow the user to edit the monster card
def edit_cards(cards):
    # This is asking the user for the moster card they want to edit and 
    # choices=list(cards.keys()) will ensure that only gives give you the option to click on monster cards that exist right now inside the dictionary
    user_input = easygui.buttonbox("What montser card would you like to edit?", choices=list(cards.keys()))

    # this will ask for for the trait they want to edit and choice=list(cards[user_input].keys()) will only give existing traits from the dictionary
    item_to_modify = easygui.buttonbox("What would you like to edit?", choices=list(cards[user_input].keys()))

    #   This will loop untill the user finally adds the right power for the trait they pick
    while True:
        try:
            new_price = int(easygui.enterbox(f"Enter the new power level for {item_to_modify}:"))
            if new_price < 0 or new_price > 25:
                easygui.msgbox("Not vaild! please try agian")
                continue
            else:
                break

        except ValueError:
            easygui.msgbox("Not vaild! please try again")
            continue
        

    # This will add the user_input inside the dicionary cards and will add the trait and new_price inside the user_input
    cards[user_input][item_to_modify] = new_price
    easygui.msgbox(f"{user_input} has been updated!")

# Main menu where the user can pick what to do
def main():
    # This will loop the whole thing even when the user goes to one of other funtion and comes back unless they click on leave
    while True:
        main = easygui.buttonbox(
            msg="======================================\n"
                "   --------------------------------\n"
                "       Display Monster cards\n"
                "       Add a Monster card\n"
                "       Search for Monster card\n"
                "       Remove Monster card\n"
                "       Edit Monster card\n"
                "       Exit/Leave\n"
                "   --------------------------------\n"
                "======================================",

                # these arethe choices that the user can pick
                choices=["Display", "Add", "Search", "Remove", "Edit", "Exit/Leave"],
                title="Main Menu"
        )
        # if the user presses on display then it will go to the display function
        if main == "Display":
            display_cards(cards)
        # if the user presses on add then it will go to the add function
        elif main == "Add":
            add_cards(cards)
        # if the user presses on search then it will go to the search function
        elif main == "Search":
            search_cards(cards)
        # if the user presses on remove then it will go to the remove function
        elif main == "Remove":
            remove_cards(cards)
        # if the user presses on edit then it will go to the edit function 
        elif main == "Edit":
            edit_cards(cards)
        # if the user presses on exit/leave then it exit
        elif main == "Exit/Leave":
            easygui.msgbox("Thanks for visiting!")
            break

# This will run the main function
main()

