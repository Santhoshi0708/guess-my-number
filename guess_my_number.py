#game for Guessing the Number 
import random as r 
Easy_level_Attempts=10
Hard_level_Attempts=5
#To specify the number of attempts required to complete the game
def set_difficulty(level):
    if level=="Easy":
       return Easy_level_Attempts
    else:
       return Hard_level_Attempts     
    
#A function to check the guesses number
def check_guessed_Number(Guessed_number,Result,No_of_Attempts):
    if Guessed_number<Result:    
        print("your gussed number is low!")
        return No_of_Attempts - 1  
    elif Guessed_number > Result:
        print("Your gussed number is high!")
        return No_of_Attempts -1  
    else:
        print("Yes! Congratulations you Won.You guessed the correct Number ")  


initial_Range=int(input("Enter the starting Number Range: "))
Final_Range=int(input("Enter the Final Number Range: "))
print(f"The Number Range between {initial_Range} to {Final_Range}---->")
Result=r.randint(initial_Range,Final_Range)
#To select the level of the game
level=input("choose your selected level as 'Easy' or 'Difficulty':")
No_of_Attempts=set_difficulty(level)
Guessed_number=0
#To specify the number of attempts had left
while(Guessed_number != Result):
    print(f"you have {No_of_Attempts} attempts remaining for guessing the Number!")
    Guessed_number=int(input("Guess a Number:"))
    No_of_Attempts=check_guessed_Number(Guessed_number,Result,No_of_Attempts)
    if No_of_Attempts==0:
        print("You lost the game!")
        break
    else:
        print("Try Again!") 
#code Developed by
print("Developed by: https://github.com/Santhoshi0708")        
                       
                       



