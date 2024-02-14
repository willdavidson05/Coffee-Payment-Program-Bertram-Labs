class Coworker:
    def __init__(self, name, drink, price):
        """
        Initialize a Coworker object.

        Parameters:
        - name (str): The name of the coworker.
        - drink (str): The preferred coffee drink of the coworker.
        - price (float): The price of the coworker's preferred coffee drink.
        """
        self.name = name
        self.drink = drink
        self.price = price
        self.paid = False  

def determine_payment(coworkers, last_payer_index):
    """
    Determine the next coworker that should pay for coffee.

    Parameters:
    - coworkers (list): A list of Coworker objects.
    - last_payer_index (int): The index of the last coworker who paid.

    Returns:
    - payer (Coworker): The coworker who is going to pay.
    - last_payer_index (int): The updated index of the last coworker who paid.
    """
    # Find the next coworker who has yet to pay
    while True:
        # Rotate through the list
        last_payer_index = (last_payer_index + 1) % len(coworkers)
        coworker = coworkers[last_payer_index]
        if not coworker.paid:
            coworker.paid = True
            return coworker, last_payer_index

def get_coworker_details():
    """
    Get details of new coworkers from the user.

    Returns:
    - coworkers (list): A list of Coworker objects.
    """
    # Provided co-workers
    coworkers = [
        Coworker("Bob", "cappuccino", 3.5),
        Coworker("Jeremy", "black coffee", 2.5)
    ]
    # Find remaining coworkers
    for i in range(3):
        name = input(f"Enter coworker {i+3}'s name: ")
        drink = input(f"Enter coworker {i+3}'s preferred coffee drink: ")
        while True:
            try:
                price = float(input(f"Enter the price of {name}'s preferred coffee drink: "))
                if price <= 0:
                    raise ValueError("Price must be a positive number")
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid price.")
        coworkers.append(Coworker(name, drink, price))
    return coworkers

def display_menu():
    """
    Display the menu options.
    """
    print()
    print("Menu:")
    print("1. View who should pay")
    print("2. Quit")

def main():
    """
    Main function to run the coffee payment program.
    """
    coworkers = get_coworker_details()

    # Keep track of the index of the last person to pay
    last_payer_index = -1  # Start from the end of the list 

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Determine who is gonna pay for coffee 
            payer, last_payer_index = determine_payment(coworkers, last_payer_index)
            print(f"It's {payer.name}'s turn to pay ${payer.price} for {payer.drink} today!")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
