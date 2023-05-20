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

------------------------------------------------------------------------------------------------------------------------------------------------------------
from tabulate import tabulate
Price1 = 50
Price2 = 50
Price3= 120

def EventSummary (EnteredAnswer2):
    if EnteredAnswer2 == 1 :
        print("Summary of Event: Riyadh hosts Winter Wonderland, the biggest theme park in its third season, combining rides & adventures in a unique experience for all ages. More than 80 different experiences including thrill, family, kids rides, and different characters & musical shows. ")
    elif EnteredAnswer2 == 2 : 
        print("Summary of Event: Riyadh Boulevard, where endless fun destinations can be found in one place. In addition to the luxury shopping places where you can obtain pieces from the finest stores of international brands to your own closet, along with dishes that amaze your senses with flavours of local and international cuisine. ")
    elif EnteredAnswer2 == 3 : 
        print("Summary of Event: AlMurabaa is one of the annual zones of the Riyadh Season entertainment festival held at the National Museum Park of King Abdulaziz Historical Center in the al-Murabba neighborhood of Riyadh,it features several seasonal restaurants and cafes with international cuisines. ")
    else : 
        print("Sorry, We couldn't find what you looking for! ")
        Starts()

        
        
        
def Checkout (EnteredAnswer4):
     pass         

        
        
def EventPrices (EnteredAnswer2):
    if EnteredAnswer2 == 1 :
        print(" --------------------- ")
        print("The prices for this event is 50 SR for all days. ")
    elif EnteredAnswer2 == 2 :
        print(" --------------------- ")
        print("The prices for this event is 50 SR for all days. ")
        
    elif EnteredAnswer2 == 3 :
        print(" --------------------- ")
        print("The prices for this event is 120 SR for all days.")
    else :
        return 0

def EventReservations (EnteredAnswer3) :
    if EnteredAnswer3 == 'yes' :
        TicketNumbers= int(input("How many tickets do you want reserve? "))
        if EnteredAnswer2 == 1 :
                TicketPrices = TicketNumbers * Price1
                print ("The prices of whole tickets is: " , TicketPrices)
                print("The Prices Added to your cart, you buied" , TicketNumbers , "Tickets for Winter Wonderland Event. ")
        
        elif EnteredAnswer2 == 2 : 
                TicketPrices = TicketNumbers * Price2
                print ("The prices of whole tickets is: " , TicketPrices)
                print("The Prices Added to your cart, you buied" , TicketNumbers , "Tickets for Riyadh Boulevard Event. ") 
            
        elif EnteredAnswer2 == 3 :
                TicketPrices = TicketNumbers * Price3
                print ("The prices of whole tickets is: " , TicketPrices)
                print("The Prices Added to your cart, you buied " , TicketNumbers ,"Tickets for AlMurabaa Event. " )

        else : 
                return 0
        
    else :
        return 0
    


def Starts ():   
    print("Welcome to Riyadh Season, Hope you find event suits you! ")
    print(" ")
    print("Here the table of events in Riyadh : ")
    Events =[["1.Winter Wonderland", "Riyadh", "4pm - 12am "],
         ["2.Riyadh boulevard", "Riyadh" , "4pm - 2am "],
         ["3.AlMurabaa", "Riyadh" , "4pm - 2am"]]

    ColumnNames = ["Event Name", "City of Event", "Openinig Time"]
    print(tabulate(Events, headers=ColumnNames))


while True : 
    Starts ()
    EnteredAnswer2 = int(input("Please the number of an event to view the details: " ))
    EventSummary(EnteredAnswer2)
    EventPrices(EnteredAnswer2)
    EnteredAnswer3 = input("Do you want to reverse this event? ")
    EventReservations(EnteredAnswer3) 

    

        