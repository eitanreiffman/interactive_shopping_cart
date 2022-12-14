# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The User can also clear the current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

# I would also like to give the user limited options.
# If they don't add an item that's on the list, the item won't get added

# So basically there should be 2 separate dictionaries.
# One that shows the user's shopping cart, and another that shows the available items in the store

# How can we set up a scenario in which the user is constantly going back to the cart?
# Perhaps this can work by using a While Loop all the way at the top - as a 'base' of sorts
# Whenever the user makes a purchase, or finishes searching for an item, they'll end up getting rerouted back to the cart at the top
# This While loop will only end when the user dictates that they're done shopping - perhaps by typing in the word 'done' or 'checkout'

# Available Store Items:
available_items = {
    "Baked Goods" : {
            "Bread" : {
            "White Bread" : 2.50,
            "Rye" : 2.75,
            "Sourdough" : 2.75,
            "Whole Wheat Bread" : 2.75
        },
        "Croissant" : {
            "Butter Croissant" : 3.00,
            "Chocolate Croissant" : 3.50 
        },
        "Danish" : {
            "Cheese Danish" : 3.50,
            "Chocolate Danish" : 3.50,
        },
    },
    "Produce" : {
        "Apple" : {
            "Granny Smith Apple" : 1.00,
            "Pink Lady Apple" : 1.25,
            "Gala Apple" : 1.25 
        },
        "Orange" : {
            "Blood Orange" : 1.25,
            "Navel Orange" : 1.25
        },
        "Nectarine" : 1.35,
        "Peach" : 1.35,
        "Mango" : 1.75
    },
    "Drinks" : {
        "Soda" : {
            "Coke" : 2.00,
            "Sprite" : 2.00,
            "Root Beer" : 2.00
        },
        "Juice" : {
            "Orange Juice" : 3.00,
            "Apple Juice" : 3.50,
            "V8 Juice" : 4.50
        },
        "Milk" : {
            "Non-Fat Milk" : 1.50,
            "Low-Fat Milk" : 1.75,
            "Whole Milk" : 2.00 
        },
        "Water" : {
            "Poland Spring" : 1.50,
            "Dasani" : 1.75,
            "Sparkletts" : 1.50
        }
    },
    "Meat Counter" : {
        "Steak" : {
            "T-Bone Steak" : 10.00,
            "Rib-Eye Steak" : 9.50,
            "Skirt Steak" : 9.00
        },
        "Hamburger" : {
            "Regular Hamburger" : 6.00,
            "Veggie Burger" : 6.50,
            "Turkey Burger" : 6.25
        },
        "Sausage" : {
            "Polish Sausage" : 6.00,
            "Bratwurst" : 6.50,
            "Knackwurst" : 6.50,
            "Chorizo" : 6.50
        } 
    },
    "Cheese Counter" : {
        "Mozzarella" : {
            "Shredded Mozzarella" : 4.25,
            "Mozzarella Block" : 4.00
        },
        "Cheddar" : {
            "Shredded Cheddar" : 4.25,
            "Cheddar Block" : 4.00
        },
        "Muenster" : {
            "Sliced Muenster" : 4.50,
            "Muenster Block" : 4.25
        },
        "Gouda" : 4.50,
        "Brie" : 5.00,
        "Provolone" : 5.00,
        "Camembert" : 5.00 
    },
}

# The available items in the store are part of a global dictionary outside of this function

class Cart:
    def __init__(self, user_cart={}, total_price=0):
        self.user_cart = user_cart
        self.total_price = total_price

    def add_item(self, item, quantity, price):
        self.user_cart.update({ item : [price, quantity] })
        self.total_price += price

    def remove_item(self, item):
        self.total_price -= self.user_cart[item][0]
        del self.user_cart[item]
        print(f"{item} has been removed.")

    def clear_cart(self):
        self.user_cart = {}
        self.total_price = 0
        print("\nYour cart has been cleared.\n\n")

    def show_cart(self, item, quantity, price):
        print("Food Item\t\t\tPrice\n")
        for item, price in self.user_cart.items():
            if len(item) < 8:
                print(f"{price[1]} {item.title()}\t\t\t\t${price[0]:.2f}")
            elif len(item) > 14:
                print(f"{price[1]} {item.title()}\t\t${price[0]:.2f}")
            else:
                print(f"{price[1]} {item.title()}\t\t\t${price[0]:.2f}")
                
        print(f"\n\t\t\t\tTotal Price:\t${self.total_price:.2f}")        

new_cart = Cart()

def shopping_cart(user_cart):
    print("\nWelcome to Eitan's Very Limited Virtual Store!\n\n"
            "Feel free to browse the place and add anything you like to your shopping cart.\n\n"
            "Unfortunately, what you see is what there is.\n\n"
            "You can only add an item if it exists in the virtual store.\n")

    # Defining the customer's cart, which is empty for now
    # user_cart = {}

    username = input("Please enter your name: ").title()

    print(f"\n\nHi {username}!")

    x = ""
    z = ""
    
    # The while loop will continue to run as long as "x" doesn't equal "yes",
    # Which it won't until the user checks out and confirms they're done by entering "yes"
    while x != "yes":

        do_now = input("\nWhat would you like to do?\n\n"
                "Enter 'browse' to browse the store\n\n"
                "Enter 'remove' to remove an item from your cart\n\n"
                "Enter 'clear' to clear all items from your cart\n\n"
                "Enter 'checkout' to check out: ")
        
        # This is a while loop within a while loop that'll ensure the user can only move
        # forward with the shopping process if they enter one of the requested words
        while do_now.lower() != "browse" or "remove" or "clear" or "checkout":

            # BROWSE SECTION
            if do_now.lower() == "browse":
                print("\nThese are the different food sections:\n\n\t")
                for section in available_items:
                    print(section)

                choose_section = input("\nWhich food section would you like to browse? ").title()

                while choose_section.title() not in available_items:
                    print("\nThis food section doesn't exist.\n"
                        "\nPlease type in one of the following food sections:\n\n")
                    for section in available_items:
                        print(section)
                    choose_section = input("\n").title()

                print(f"\nYou've just entered the {choose_section} section.\n"
                        "\nIf anything interests you, type the item to see if there are different varieties."
                        "\nHere's what we have in that section:\n")
                for food_item in available_items[choose_section.title()]:
                    print(food_item)

                choose_food_type = input(f"\nPlease choose an item: ")

                while choose_food_type.title() not in available_items[choose_section.title()]:
                    print("\nSorry, you must enter an item that's in the section.")
                    print(f"\nThese are the available items.\n")
                    for food_item in available_items[choose_section.title()]:
                        print(food_item)
                    choose_food_type = input("\nPlease try again: ")

                # This is where we distinguish between food items that have variety and those that don't
                # The statement below sets aside all food items that have no variety, and immediately jumps to the purchasing stage
                # It does this by asking whether or not there's a 'float' in the item
                # Which will be true if the item is at its most specific stage, and thus has a set price, or a float)
                if isinstance(available_items[choose_section.title()][choose_food_type.title()], float) == True:
                    print(f"\nThe price of your item is ${available_items[choose_section.title()][choose_food_type.title()]:.2f}")
                    add_to_cart = input(f"\nWould you like to add it to your cart? Enter 'yes' or 'no': ")
                    if add_to_cart.lower() == "yes":
                        for item, price in available_items[choose_section.title()].items():
                            if item == choose_food_type.title():
                                quantity = int(input("\nHow many would you like? "))
                                price = price * quantity
                                new_cart.add_item(item, quantity, price)

                
                else:
                    print("Here are the kinds we have:\n\t")
                    for variety in available_items[choose_section.title()][choose_food_type.title()]:
                        print(variety)

                    choose_variety = input(f"\nChoose which variety of {choose_food_type} you want: ")

                    while choose_variety.title() not in available_items[choose_section.title()][choose_food_type.title()]:
                        choose_variety = input(f"\nThat variety isn't available. Please try again. ")
                    
                    print(f"\nThe price of this item is ${available_items[choose_section.title()][choose_food_type.title()][choose_variety.title()]:.2f}")
                    add_to_cart = input(f"\nWould you like to add it to your cart? Enter 'yes' or 'no': ")
                    if add_to_cart.lower() == "yes":
                        for item, price in available_items[choose_section.title()][choose_food_type.title()].items():
                            if item == choose_variety.title():
                                quantity = int(input("\nHow many would you like? "))
                                price = price * quantity
                                new_cart.add_item(item, quantity, price)


                # Break for "Browse" Section
                break
            
            # REMOVE SECTION
            if do_now.lower() == "remove":

                if len(new_cart.user_cart) == 0:
                    print("\nYou have nothing to remove from your shopping cart, because it's empty.")

                else:
                    for item, price in new_cart.user_cart.items():
                        if len(item) < 8:
                            print(f"{item.title()}\t\t\t\t${price[0]:.2f}")
                        elif len(item) > 12:
                            print(f"{item.title()}\t\t${price[0]:.2f}")
                        else:
                            print(f"{item.title()}\t\t\t${price[0]:.2f}")                
                    
                    remove_item = input(f"\n\nWhich item would you like to remove from your shopping cart? \n\n").title()

                    while remove_item not in new_cart.user_cart:
                        print("\nThat item doesn't exist in your cart.\n")

                        for item, price in new_cart.user_cart.items():
                            if len(item) < 8:
                                print(f"{item.title()}\t\t\t\t${price[0]:.2f}")
                            elif len(item) > 12:
                                print(f"{item.title()}\t\t${price[0]:.2f}")
                            else:
                                print(f"{item.title()}\t\t\t${price[0]:.2f}")
                        
                        remove_item = input("Which item would you like to remove? ").title()
                    
                    if remove_item in new_cart.user_cart:
                        new_cart.remove_item(item)

                        while z != "no":
                            z = input(f"\nWould you like to remove anything else? Enter 'yes' or 'no': \n\n").lower()
                            if z == "no":
                                break
                            remove_item = input(f"\nWhat else would you like to remove? \n\n").title()
                            if remove_item in new_cart.user_cart:
                                new_cart.remove_item(item)                               

                
                # Break for "Remove" Section            
                break

            # CLEAR SECTION
            if do_now.lower() == "clear":
                new_cart.clear_cart()
                break

            # CHECKOUT SECTION
            if do_now.lower() == "checkout":
                # Break for "Checkout" Section                       
                break
            
            # This statement will continue to run as long as the user didn't enter
            # 'browse', 'remove', 'clear', or 'checkout'
            else:
                do_now = input("\nSorry, your response didn't match.\n\n"
                            "You must enter either 'browse', 'remove', 'clear', or 'checkout': ")

        # This is the beginning of the checkout area.
        # Even though there is technically a "checkout" section above, it basically just skips to here:
        # SHOW CART
        if len(new_cart.user_cart) == 0:
            print("\nYour cart is currently empty")
        else:
            print("\nHere's a current overview of your shopping cart.\n\n")
            new_cart.show_cart(item, quantity, price)


        x = input(f"\nThe total price of your items is ${new_cart.total_price:.2f}. If you'd like to checkout, enter 'yes'.\n\n"
                    "To explore other options, enter any other key: ").lower()

    print(f"\nThank you {username} for shopping with us!\n")
    print(f"\nHere is your receipt:")
    new_cart.show_cart(item, quantity, price)

user_cart2 = {}
shopping_cart(user_cart2)