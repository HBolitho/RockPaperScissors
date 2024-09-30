import random
import tkinter as tk


root = tk.Tk()
root.title("Rock,Paper,Scissors")
root.geometry('800x600')


     
          
def on_button_click():

    buttontext = "rock"
    
    def rockPaperGame():
         
         playerinput = buttontext
         computerinput = random.choice(["rock","paper","scissors"])
         label3.config(text=f"Player Chose: {playerinput} ")
         label4.config(text=f"Computer Chose: {computerinput} ")
        ## Player Wins ##
         if playerinput == "rock" and computerinput == "scissors": 
             label2.config(text=f"Result: Rock smashes scissors. You Win")
         elif playerinput == "paper" and computerinput == "rock":
             label2.config(text=f"Result: Paper covers rock. You Win")
         elif playerinput == "scissors" and computerinput == "paper":
             label2.config(text=f"Result: Scissors cut paper. You Win")
  
        ## Computer Wins ##
         elif playerinput == "rock" and computerinput == "paper": 
             label2.config(text=f"Result: Paper covers rock. You Lose")
         elif playerinput == "paper" and computerinput == "scissors":
             label2.config(text=f"Result: Paper cuts scissors. You Lose")
         elif playerinput == "scissors" and computerinput == "rock":
             label2.config(text=f"Result: Rock smashes scissors. You Lose")
        ## Draws ##
         if playerinput == computerinput:
             label2.config(text=f"Result: Its a draw, go again")

    rockPaperGame()


    

def on_button_click_1():

    buttontext = "paper"
    
    def rockPaperGame():
         playerinput = buttontext
         computerinput = random.choice(["rock","paper","scissors"])
         label3.config(text=f"Player Chose: {playerinput} ")
         label4.config(text=f"Computer Chose: {computerinput} ")
         ## Player Wins ##
         if playerinput == "rock" and computerinput == "scissors": 
             label2.config(text=f"Result: Rock smashes scissors. You Win")
         elif playerinput == "paper" and computerinput == "rock":
             label2.config(text=f"Result: Paper covers rock. You Win")
         elif playerinput == "scissors" and computerinput == "paper":
             label2.config(text=f"Result: Scissors cut paper. You Win")
        ## Computer Wins ##
         elif playerinput == "rock" and computerinput == "paper": 
             label2.config(text=f"Result: Paper covers rock. You Lose")
         elif playerinput == "paper" and computerinput == "scissors":
             label2.config(text=f"Result: Paper cuts scissors. You Lose")
         elif playerinput == "scissors" and computerinput == "rock":
             label2.config(text=f"Result: Rock smashes scissors. You Lose")
        ## Draws ##
         if playerinput == computerinput:
             label2.config(text=f"Result: Its a draw, go again")
         
    rockPaperGame()



def on_button_click_2():
    buttontext = "scissors"
   
    def rockPaperGame():
         playerinput = buttontext
         computerinput = random.choice(["rock","paper","scissors"])
         label3.config(text=f"Player Chose: {playerinput} ")
         label4.config(text=f"Computer Chose: {computerinput} ")
        ## Player Wins ##
         if playerinput == "rock" and computerinput == "scissors": 
             label2.config(text=f"Result: Rock smashes scissors. You Win")
         elif playerinput == "paper" and computerinput == "rock":
             label2.config(text=f"Result: Paper covers rock. You Win")
         elif playerinput == "scissors" and computerinput == "paper":
             label2.config(text=f"Result: Scissors cut paper. You Win")
        ## Computer Wins ##
         elif playerinput == "rock" and computerinput == "paper": 
             label2.config(text=f"Result: Paper covers rock. You Lose")
         elif playerinput == "paper" and computerinput == "scissors":
             label2.config(text=f"Result: Paper cuts scissors. You Lose")
         elif playerinput == "scissors" and computerinput == "rock":
             label2.config(text=f"Result: Rock smashes scissors. You Lose")

        ## Draws ##
         if playerinput == computerinput:
             label2.config(text=f"Result: Its a draw, go again")
    rockPaperGame()



   

#buttons

button = tk.Button(root, text = "Rock" , command=on_button_click)
button.pack()

button = tk.Button(root, text = "Paper" , command=on_button_click_1)
button.pack()

button = tk.Button(root, text = "Scissors" , command=on_button_click_2)
button.pack()


#labels

label = tk.Label(root, text=("Click one of the following buttons to start the game"))
label.pack()

label3 = tk.Label(root, text=("You chose: "))
label3.pack()

label4 = tk.Label(root, text=("Computer chose: "))
label4.pack()

label2 = tk.Label(root, text=("Result: "))
label2.pack()



root.mainloop()
