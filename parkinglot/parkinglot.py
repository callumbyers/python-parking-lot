import random
import math

class parking_lot:
    def __init__(self, num_spaces, status):
        self.num_spaces = num_spaces
        self.status = status

    def open_spaces(self, free_spaces):
        free_spaces = self.num_spaces
    #def check_status(self):

class vehicle:
    def __init__(self, size, ticket_number, ticket_status):
        self.size = size
        self.ticket_number = ticket_number
        self.ticket_status = ticket_status

    def parking_options(self, small_tickets, medium_tickets, large_tickets):
        if self.size == "Small":
            print("You can park in a small space, a medium spot, or a large space ")
            print("There are {} small spots available, {} medium spots available, and {} large spots available.".format(len(small_tickets), len(medium_tickets), len(large_tickets)))
            space_selection = str(input("Enter space size:\n1. Small\n2. Medium\n3. Large\n-->"))
            if space_selection == "1" or space_selection.lower() == "small":
                ticket_number = random.choice(small_tickets)
                return ticket_number, "Small"
            elif space_selection == "2" or space_selection.lower() == "medium":
                ticket_number = random.choice(medium_tickets)
                return ticket_number, "Medium"
            elif space_selection == "3" or space_selection.lower() == "large":
                ticket_number = random.choice(large_tickets)
                return ticket_number, "Large"
            else:
                print("Invalid input")

        elif self.size == "Medium":
            print("You can park in a medium space or a large space")
            print("There are {} medium spaces available and {} large spaces available.". format(len(medium_tickets), len(large_tickets)))
            space_selection = input("Enter space size:\n1. Medium\n2. Large\n-->")
            if space_selection == "1" or space_selection.lower() == "medium":
                ticket_number = random.choice(medium_tickets)
                return ticket_number, "Medium"
            elif space_selection == "2" or space_selection.lower() == "large":
                ticket_number = random.choice(large_tickets)
                return ticket_number, "Large"

        elif self.size == "Large":
            print("You can park in a large space")
            print("There are {} large spaces available.".format(len(large_tickets)))
            space_selection = input("Enter space size:\n1. Large\n-->")
            ticket_number = random.choice(large_tickets)
            return ticket_number, "Large"
    
class parking_space:
    def __init__(self, size, status):
        self.size = size
        self.status = status

class ticket:
    def __init__(self, ticket_number, spot_size, status):
        self.ticket_number = ticket_number
        self.status = status
        self.spot_size = spot_size

    def generate_ticket(self, car, small_sel, med_sel, large_sel, open_tickets):
        car.ticket_number, self.spot_size = car.parking_options(small_sel, med_sel, large_sel)
        if self.spot_size == "Small":
            small_sel.remove(car.ticket_number)
            open_tickets["Small Spaces"].append(car.ticket_number)
        elif self.spot_size == "Medium":
            med_sel.remove(car.ticket_number)
            open_tickets["Medium Spaces"].append(car.ticket_number)
        elif self.spot_size == "Large":
            large_sel.remove(car.ticket_number)
            open_tickets["Large Spaces"].append(car.ticket_number)
        self.status= "Open"
        car.ticket_status = "Open"
        self.ticket_number = car.ticket_number

    def close_ticket(self, open_tickets, small_sel, med_sel, large_sel):
        print("Open Tickets:")
        print("*************")
        print("Small Spaces: {}\nMedium Spaces: {}\nLarge Spaces: {}".format(open_tickets["Small Spaces"], open_tickets["Medium Spaces"], open_tickets["Large Spaces"]))
        entry = 0
        while entry < 3:
            tick_cl = int(input("Enter ticket to close: "))
            if open_tickets["Small Spaces"].count(tick_cl) == 1:
                small_sel["Small Spot Ticket Numbers"].append(tick_cl)
                open_tickets["Small Spaces"].remove(tick_cl)
                print("Ticket number {} is now closed.".format(tick_cl))
                entry = 4
            elif open_tickets["Medium Spaces"].count(tick_cl) == 1:
                med_sel["Medium Spot Ticket Numbers"].append(tick_cl)
                open_tickets["Medium Spaces"].remove(tick_cl)
                print("Ticket number {} is now closed.".format(tick_cl))
                entry = 4
            elif open_tickets["Large Spaces"].count(tick_cl) == 1:
                    large_sel["Large Spot Ticket Numbers"].append(tick_cl)
                    open_tickets["Large Spaces"].remove(tick_cl)
                    print("Ticket number {} is now closed.".format(tick_cl))
                    entry = 4
            else:
                print("Must enter a vald ticket number")
                entry += 1
        if entry == 4:
            pass
        else:
            print("Too many invalid attempts")









