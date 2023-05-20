# Bootcamp-Project-1-Python

#### Based on what you’ve learned until now, create a project of your choosing (impress us with your imagination). This project must at least satisfy the following minimum requirements:

- Use at least 3 different data types.
- Use lists or dictionaries or tuples or sets.
- Use loops.
- Use functions that return an output.
- Use conditions.
- Use a Lambda function.


### Example: Riyadh Season Reservations

#### Overview: An online website that shows different events. The visitor should be able to do the following tasks for the store to function properly. As a visitor, I should be able to do the following:

- Browse Events.
- View the event info (summary, time, price, place, etc.)
- Search for an Event.
- Get recommendations for my next visit based on my ticket purchase history.
- Add tickets to the shopping cart.
- Remove a ticket from the shopping cart.
- List the tickets in my shopping cart.
- Modify the number of the ticket (by default one ticket).
- Continue to checkout.
- Get a QR code for my ticket.
- Review my coming events.

#### Final Deliverables:
- Notebook file(.ipynb).
- README.md file.
- Due Date: Sat, 20, at 09:00 p.m.
- The Final presentation will be on Sunday (5 min for each one).

# Bootcamp project 1 python
## Game: Rock, Paper, Scissors!

### References used :
- [Dataquest.](https://www.dataquest.io/blog/python-projects-for-beginners/)
- [PYnative.](https://pynative.com/python-random-choice/)
- [Geeksforgeeks.](https://www.geeksforgeeks.org/how-to-use-if-else-elif-in-python-lambda-functions/)
- [Stackoverflow.](https://stackoverflow.com/questions/9264763/why-does-this-unboundlocalerror-occur-closure)

``` python 
import random
#number of attempts
count=0
#number of Scores for computer and user
Uscore=0
Cscore=0
#while loop 3 attempts 
while(count<3):
#while loop if user and computer have same input
    compare=True
    while (compare==True): 
        user = input("User : Enter (Rock or Paper or Scissors) :" )
        game =["Rock","Paper","Scissors"]
        computer = random.choice(game)
        print ("Computer : Enter (Rock or Paper or Scissors) :{}".format(computer))
        compare = (computer==user)
        if (compare==True):
            print("Same input!")



    def RPSGame(u,c):
        global Uscore
        global Cscore
        if u=="Rock" and c=="Paper":
            Cscore+=1
            print ("computer is winner")
        elif u=="Paper" and c=="Rock":
            Uscore+=1
            print ("user is winner")
        elif u=="Paper" and c=="Scissors":
            Cscore+=1
            print ("computer is winner")
        elif u=="Scissors" and c=="Paper":
            Uscore+=1
            print ("user is winner")
        elif u=="Rock" and c=="Scissors":
            Uscore+=1
            print ("user is winner")
        elif u=="Scissors" and c=="Rock":
            Cscore+=1
            print ("computer is winner")

    RPSGame(user,computer)
    count+=1
    
result = lambda c,u : "The final winner is User" if c < u else "The final winner is Computer" 

print(result(Cscore, Uscore))

```