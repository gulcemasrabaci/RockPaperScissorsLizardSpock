import random

def name_to_number(name):
    """Assigns a number between 0-4 to each choice."""
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Error: invalid name! Game cannot be played."
        
def number_to_name(number):
    """Converts the given number between 0-4 to its matching string."""
   
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Error: invalid number! The number must be in the range [0, 4]"

def rpsls(player_choice): 
    """Randomly generates the computer's choice, 
    plays the game between player and computer, 
    prints the result."""
    
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    if 0 <= player_number <= 4: 
        difference = (comp_number - player_number) % 5
    
        if difference == 0:
            print "Player and computer tie!"
        elif difference <= 2:
            print "Computer wins!"
        else:
            print "Player wins!"
    print       
            
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




