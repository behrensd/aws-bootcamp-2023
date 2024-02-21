def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    computer_choice = "paper"
    choices = {"computer": computer_choice, "player": player_choice}
    return choices

choices = get_choices ()
print(choices)
