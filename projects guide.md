# Bird Hangout Project

## Project Idea
My project is a bird hangout application where you book a session to spend time with our lovely birds.

### Welcome Page:
when the application starts, the client will be met with the "Welcome" page and three options to choose from:

1. **view available sessions.** 


 *Where all the available birds will be shown to the client with general information about them.*
 ![image](https://github.com/Nier1419/Bootcamp-Project-1-Python/assets/85634276/1d22baec-4c42-48de-b1d7-c0f3fadeab13)

 
  
2. **book a session.** 


*Where the client will book a session with a bird of their choice.*
 ![image](https://github.com/Nier1419/Bootcamp-Project-1-Python/assets/85634276/72db04e7-1755-4bce-8f73-83a7ef1a36c8)
 
3. **Exit.** 


*To exit the application.*

### Booking a Session:
When booking a session, the client needs to type the birds name. If the bird is availabe, the client will get a confirmation message  with a picture
of the bird they booked. Else, the system will inform the client that the name they typed is either not found or busy with other clients.




# Meeting Python Project 1 Requirements

- Use at least 3 different data types:
```python
"bird1":{"Name":"Coco","Image":img("coco.jpg"), "Breed":"Cockatiel", 
             "age":age(relativedelta(date.today(), date(2021, 1, 15))), 
             "AlreadyBooked": False, "Amount Per Session": 20.0}
```

- Use lists or dictionaries or tuples or sets.
```python
"bird1":{"Name":"Coco","Image":img("coco.jpg"), "Breed":"Cockatiel", 
             "age":age(relativedelta(date.today(), date(2021, 1, 15))), 
             "AlreadyBooked": False, "Amount Per Session": 20.0}
```

- Use loops
```python
   for birds in pets:
            if pets[birds]["AlreadyBooked"]==False:
                print("------------\nBird Name: ",pets[birds]["Name"], "\n")
                display(pets[birds]["Image"])
                print("\nBreed:",pets[birds]["Breed"],"\nAge:",pets[birds]["age"],
                      "\nAmount Per Session:",pets[birds]["Amount Per Session"])
```

- Use functions that return an output.
```python
  def birdAge():
    #used the lambda to deal with unknown arguments in this case each birds age where
    #lambda returns the exact age including months and days
    return lambda age:" %d years, %d months, and %d days." % (age.years, age.months, age.days)
```

- Use conditions.
 ```python
   if len(userInput)!=1:
        print("please only enter one of the specified numbers.")
```

- Use a Lambda function.
 ```python
  img = lambda image: Image.open(image).resize((400,500 ), Image.ANTIALIAS)
```
