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


# Project: MeshMaker

#### Overview: A MeshMaker program will receives customers' orders for custom 3D models and animation. The customers should be able to do the following tasks in the program to function properly. As a customer, I should be able to do the following:

- Browse 3D models.
- View each model's info (image, description, price)
- Order my own custom model.
- Get an estimated price for my order.
- Cancel my order.
- Contact the MeshMaker team.
- Get a QR code for my order summary.

### Main fuctions

- **menu():** it used to print the program options menu and take the user choice
- **modelsExamples():** it used to display models examples for the user
- **orderCustomModel(ordersDict):** it used to take new custom model order from the user and add it to orders dictionary for later use by meshMakers team.
- **estimatePrice():** it used to ask the user for some details about his order to give an estimate price for it.
- **contactTeam():** it used to show a QR code for the support team email.
- **main():** it used to start the main logic of the program.

####The Bootcamp-Project-1-Python_Zainab.ipynb file contains my project code, there are some pieces of code that I used by searching through other websites and I have listed them below:

**1- For the QR code generation:**

```python
img = qrcode.make('Contact the MeshMaker team: zainabmel1421@gmail.com') # type is (qrcode.image.pil.PilImage)
#save the generated QR code image and display it for the user
img.save("QR_code\contact_QR_code.png")
display(Image.open("QR_code\contact_QR_code.png").resize((200, 200)))
```
[QR code](https://pypi.org/project/qrcode/)

**2- For the current date and time retrieve:**

```python
#save current date and time
now = datetime.now() #datetime object containing current date and time
#save order info in the orders dictionary for later use by meshMaker team
ordersDict["description"].append(orderDetails)
ordersDict["time"].append(now)
```
[Date and Time](https://www.programiz.com/python-programming/datetime/current-datetime)

**3- For using the lambda function:**

```python
#use lambda that accepts one argument to greet user
greetUser = lambda name : print('\nHey,', name,"\n")

#call lambda function with user name
greetUser(userName)
```
[Lambda function](https://www.programiz.com/python-programming/anonymous-function)