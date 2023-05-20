global f
f = 0
global place
global Trip
import time
from tkinter import messagebox


#this Visit function is used to select Trip name 
def Visit():
    global f
    f = f+1
    global place
    global Trip

    print("\n\nwhich Trip do you want to go?")

    if place ==1:
            
        print("1,Al-Bujairi ")
        print("2,Al-Diriyah ")
        print("3,U Walk ")
        print("4,back")

    elif place ==2:
             
         print("1,Water Front ")
         print("2,City Walk ")
         print("3,Redsea Mall")
         print("4,back")

    elif place ==3:
             
         print("1,Muraikabat Mountain ")
         print("2,Folk Village ")
         print("3,Mudon Lake ")
         print("4,back")
    Trip = int(input("choose your Trip: "))
    if Trip == 4:
      # from method it goes to Trip function 
      # and it comes back here and then go to method 
      main()
      return 0
    if f == 1:
      method()
      
      
# this method function used to select the transportation method
def method():
    global seats
    print("\n\nwhich transportation method do you want to use in your Trip: ")
    print("1,Taxi")
    print("2,Train")
    print("3,Car")
    print("4,Bus")
    print("5,Walk")
    a = int(input("choose your method: "))
    seats = int(input("\n\nnumber of seats do you want?: "))
    timing(a)
# this timing function used to select timing for the trip 
def timing(a):
    global seats

    time1 = { # every place have its own time guidelines 
        "1": "2:30",
        "2": "4:30",
        "3": "5:30",
        "4": "8:30"
    }
    time2 = {
        "1": "3:30",
        "2": "4:30",
        "3": "6:30",
        "4": "7:30"
    }
    time3 = {
        "1": "4:30",
        "2": "8:30",
        "3": "12:30",
        "4": "2:30"
    }
    time4 = {
        "1": "7:30",
        "2": "8:30",
        "3": "9:30",
        "4": "10:30"
    }
    time5 = {
        "1": "1:30",
        "2": "2:30",
        "3": "3:30",
        "4": "4:30"
    }
    date1 = {
        "1": "21/5/2023",
        "2": "22/5/2023",
        "3": "23/5/2023",
        "4": "24/5/2023"
    }
    date2 = {
        "1": "21/5/2023",
        "2": "22/5/2023",
        "3": "23/5/2023",
        "4": "24/5/2023"
    }
    date3 = {
        "1": "21/5/2023",
        "2": "22/5/2023",
        "3": "23/5/2023",
        "4": "24/5/2023"
    }
    date4 = {
        "1": "21/5/2023",
        "2": "22/5/2023",
        "3": "23/5/2023",
        "4": "24/5/2023"
    }
    date5 = {
        "1": "21/5/2023",
        "2": "22/5/2023",
        "3": "23/5/2023",
        "4": "24/5/2023"
    }
 
      
      
    if a == 1:
        print("\n\nchoose time & date:")
        print(time1)

        t = input("\n\nselect time of the above:")
        print(date1)

        d = input("\n\nselect date of the above:")
        x = time1[t]
        z=date1[d]
        print("\n\nsuccessful!, enjoy your trip at "+x+" on "+z+" for "+str(seats)+" persons")
        
        messagebox.showinfo('Info', 'Booking completed!')

    elif a == 2:
        print("\n\nchoose time & date:")
        print(time2)
        t = input("\n\nselect time of the above:")
        print(date2)
        d = input("\n\nselect date of the above:")
        x = time2[t]
        z=date2[d]

        print("\n\nsuccessful!, enjoy your trip at "+x+" on "+z+" for "+str(seats)+" persons")
        messagebox.showinfo('Info', 'Booking completed!')

    elif a == 3:
        print("\n\nchoose time & date:")
        print(time3)
        t = input("\n\nselect time of the above:")
        print(date3)
        d = input("\n\nselect date of the above:")
        x = time3[t]
        z=date3[d]

        print("\n\nsuccessful!, enjoy your trip at "+x+" on "+z+" for "+str(seats)+" persons")
        messagebox.showinfo('Info', 'Booking completed!')

    elif a == 4:
        print("\n\nchoose time & date:")
        print(time4)
        t = input("\n\nselect time of the above:")
        print(date4)
        d = input("\n\nselect date of the above:")
        x = time4[t]
        z=date4[d]

        print("\n\nsuccessful!, enjoy your trip at "+x+" on "+z+" for "+str(seats)+" persons")
        messagebox.showinfo('Info', 'Booking completed!')

    elif a == 5:
        print("\n\nchoose time & date:")
        print(time5)
        t = input("\n\nselect time of the above:")
        print(date5)
        d = input("\n\nselect date of the above:")
        x = time5[t]
        z=date5[d]

        print("\n\nsuccessful!, enjoy your trip at "+x+" on "+z+" for "+str(seats)+" persons")
        messagebox.showinfo('Info', 'Booking completed!')

          
    return 0




def Trip(method):
    if method == 1:
        Visit()
    elif method == 2:
        Visit()
    elif method == 3:
        Visit()
    elif method == 4:
        main()
    else:
        print("wrong choice")


def main():
    global place
    print("\n\nhi welcome to Trip seats booking: ")
    # lambda that accepts one argument
    greet_user = lambda name : print('Hey there,', name)

    # lambda call
    greet_user(str(input('What is your name? ')))
    time.sleep(2)

    print("\n\nwhere you want to make a Trip?:")
    print("1,Riyadh")
    print("2,Jeddah")
    print("3,Dammam")
    place = int(input("choose your option: "))

    while place != 1 and place != 2 and place != 3: 

          print("wrong choice")
          place = int(input("choose your option: "))
    else:      
        if place == 1:
          Trip(place)
        elif place == 2:
          Trip(place)
        elif place == 3:
          Trip(place)
    return place
main() # the magic will beggin

