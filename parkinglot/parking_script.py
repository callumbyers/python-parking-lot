import math
import random
import sys
sys.path.append("/Users/callumbyers/Desktop/DigitalCrafts/python-exercises-feb-fullstack/py_wk_2_fr/parkinglot/")
import parkinglot as pl
import json
import pickle

#Functions
def space_numbers(num_spaces):
    available_spaces = []
    for i in range(1, num_spaces + 1):
        available_spaces.append(i)
    return available_spaces

parkingAlot = pl.parking_lot(300, "OPEN")
available_spaces = space_numbers(parkingAlot.num_spaces)
random.shuffle(available_spaces)
small_spaces = available_spaces[0:100]
medium_spaces = available_spaces[100:200]
large_spaces = available_spaces[200:300]

space_s = "small"
space_m = "medium"
space_l = "large"

veh_s = "small"
veh_m = 'medium'
veh_l = 'large'

open_tickets = {"Small Spaces":[], "Medium Spaces":[], "Large Spaces":[]}
small_tickets = {"Small Spot Ticket Numbers": small_spaces}
medium_tickets = {"Medium Spot Ticket Numbers": medium_spaces}
large_tickets = {"Large Spot Ticket Numbers": large_spaces}

with open('open_tickets.json', 'r') as ot:
    open_tickets = json.load(ot)
with open('small_tickets.json', 'r') as st:
    small_tickets = json.load(st)
with open('medium_tickets.json', 'r') as mt:
    medium_tickets = json.load(mt)
with open('large_tickets.json', 'r') as lt:
    large_tickets = json.load(lt)

ticket = pl.ticket(0, 'none assigned', 'Closed')

#while parkingAlot.status == "OPEN":
main = True
ans_1 = input("Would you like to run the program?: [Y/N]")
if ans_1.upper() == "Y":
    while main == True:
        print("\nWelcome")
        print("\nPlease select an option: ")
        print("************************")
        print("1. Vehicle Entry\n2. Close Ticket\n3. View Number of Open Spaces\n4. View Open Tickets\n5. Close Program")
        user_in = input("-->: ")
        prog = True
        if user_in == "1":
            while prog == True:
                car_size = str(input("\nInput Vehicle Size\n1. Small\n2. Medium\n3. Large\n-->"))
                if car_size == "1" or car_size.lower() == "small":
                    car_size = "Small"
                elif car_size == "2" or car_size.lower() == "medium":
                    car_size = "Medium"
                elif car_size == "3" or car_size.lower() == "large":
                    car_size = "Large"
                car = pl.vehicle(car_size, ticket.ticket_number, ticket.status)
                #car.parking_options(small_spaces, medium_spaces, large_spaces)
                ticket.generate_ticket(car, small_tickets["Small Spot Ticket Numbers"], medium_tickets["Medium Spot Ticket Numbers"], large_tickets["Large Spot Ticket Numbers"], open_tickets)
                print("Ticket Information\n******************\nVehicle Size: {}\nParking Space Size: {}\nTicket Number: {}\nTicket Status: {}".format(car.size, ticket.spot_size, car.ticket_number, car.ticket_status))

                with open('open_tickets.json', 'w') as ot:
                    json.dump(open_tickets, ot)
                with open('small_tickets.json', 'w') as st:
                    json.dump(small_tickets, st)
                with open('medium_tickets.json', 'w') as mt:
                    json.dump(medium_tickets, mt)
                with open('large_tickets.json', 'w') as lt:
                    json.dump(large_tickets, lt)

                print("\nEnter another vehicle?: [Y/N]")
                ans2 = input("-->: ")
                if ans2.upper() == "Y":
                    main = True
                    prog = True
                elif ans2.upper() == "N":
                    print("\nGoodbye")
                    main = True
                    prog = False
        elif user_in == "2":
            close = True
            while close == True:
                ticket.close_ticket(open_tickets, small_tickets, medium_tickets, large_tickets)
                print("\nClose another ticket?: [Y/N]")
                ans3 = str(input("-->: "))
                if ans3.upper() == "Y":
                    close = True
                    main = True
                    prog = True
                elif ans3.upper() == "N":
                    print("\nGoodbye")
                    with open('open_tickets.json', 'w') as ot:
                        json.dump(open_tickets, ot)
                    with open('small_tickets.json', 'w') as st:
                        json.dump(small_tickets, st)
                    with open('medium_tickets.json', 'w') as mt:
                        json.dump(medium_tickets, mt)
                    with open('large_tickets.json', 'w') as lt:
                        json.dump(large_tickets, lt)
                    close = False
                    main = True
                    prog = False
        elif user_in == "3":
            print("\nNumber of small spaces available: {}".format(len(small_tickets['Small Spot Ticket Numbers'])))
            print("Number of medium spaces available: {}".format(len(medium_tickets["Medium Spot Ticket Numbers"])))
            print("Number of large spaces available: {}".format(len(large_tickets["Large Spot Ticket Numbers"])))
            print("\nSelect an Option:")
            print("\n1. Main Menu\n2. Close Program")
            user_3 = input("-->")
            if user_3 == "1":
                prog = True
                main = True
            else:
                print("\nGoodbye")
                prog = False
                main = False
        elif user_in == "4":
            print("{}".format(open_tickets["Small Spaces"]))
            print("{}".format(open_tickets["Medium Spaces"]))
            print("{}".format(open_tickets["Large Spaces"]))
            print("\nPlease select an option")
            print("\n1. Main Menu\n2. Close Program")
            user_in2 = input("-->: ")
            if user_in2 == "1":
                main = True
                prog = False
            else:
                print("\nGoodbye")
                prog = False
                main = False
        else:
            print("Goodbye")
            with open('open_tickets.json', 'w') as ot:
                json.dump(open_tickets, ot)
            with open('small_tickets.json', 'w') as st:
                json.dump(small_tickets, st)
            with open('medium_tickets.json', 'w') as mt:
                json.dump(medium_tickets, mt)
            with open('large_tickets.json', 'w') as lt:
                json.dump(large_tickets, lt)
            prog = False
            main = False
elif ans_1.upper() == "N":
    with open('open_tickets.json', 'w') as ot:
        json.dump(open_tickets, ot)
    with open('small_tickets.json', 'w') as st:
        json.dump(small_tickets, st)
    with open('medium_tickets.json', 'w') as mt:
        json.dump(medium_tickets, mt)
    with open('large_tickets.json', 'w') as lt:
        json.dump(large_tickets, lt)
    print("Goodbye")
    main = False