#This is for importing tabulate module to create table.
from tabulate import tabulate

#This code is to create Vending Machine Menu using dictionary.
dict_Vendmac={
    "Snacks":{  #Category 1:Snacks.
        "S01":{"Name":"Herr's chips","Price $":1.00,"Stock":9},
        "S02":{"Name":"Terra","Price $":2.50,"Stock":11},
        "S03":{"Name":"popchips","Price $":2.00,"Stock":15},
        "S04":{"Name":"Doritos","Price $":2.25,"Stock":18},
        "S05":{"Name":"Ruffles","Price $":2.75,"Stock":30},
        "S06":{"Name":"Fritos","Price $":3.65,"Stock":13},
        "S07":{"Name":"Cheetos","Price $":3.00,"Stock":14},
    },
    "Drinks":{  #Category 2:Drinks.
        "D01":{"Name":"Sprite","Price $":1.75,"Stock":13},
        "D02":{"Name":"Mountain Dew","Price $":1.75,"Stock":12},
        "D03":{"Name":"Seven Up","Price $":2.25,"Stock":12},
        "D04":{"Name":"Cola Diet","Price $":2.50,"Stock":11},
        "D05":{"Name":"Cola Regular","Price $":1.75,"Stock":14},
        "D06":{"Name":"Fanta","Price $":3.75,"Stock":15},
        "D07":{"Name":"Frooti","Price $":4.55,"Stock":14},
        "D08":{"Name":"Water","Price $":1.75,"Stock":12}
    },
    "Chocolates":{ #Category 3:Chocolates.
        "C01":{"Name":"Dairy Milk","Price $":5.65,"Stock":11},
        "C02":{"Name":"Tobleron","Price $":4.75,"Stock":15},
        "C03":{"Name":"Kinder bars","Price $":1.50,"Stock":13},
        "C04":{"Name":"Dark Chocolate Bar","Price $":5.50,"Stock":19},
        "C05":{"Name":"Twix","Price $":1.75,"Stock":20},
        "C06":{"Name":"Sneakers","Price $":2.75,"Stock":11},
        "C07":{"Name":"Cadbury","Price $":5.75,"Stock":15},
        "C08":{"Name":"Godiva Chocolatier","Price $":6.75,"Stock":16}
    },
}

# Function to display the menu in a table format
def display_dict_Vendmac(category=None):
    Vendmac_table_data = []
    if category:
        items = dict_Vendmac.get(category, {})
        for code, item in items.items():
            stocksta = f"{item['Stock']}" if item['Stock'] > 0 else "Out of stock"
            Vendmac_table_data.append([code, item["Name"], f"${item['Price $']:.2f}", stocksta])
        return tabulate(Vendmac_table_data, headers=["Code", "Item", "Price", "Stock"], tablefmt="pretty")
    else:
        categories = list(dict_Vendmac.keys())
        Vendmac_table_data = [[i + 1, cat] for i, cat in enumerate(categories)]
        return tabulate(Vendmac_table_data, headers=["Code", "Category"], tablefmt="pretty")

# Main program
if _name_ == "_main_":
    print("Welcome to the Vending Machine!")
    total_cost = 0
    categories = list(dict_Vendmac.keys())
    while True:
        print("\nCategories ")
        print(display_dict_Vendmac())
        category_code = input("Choose a code (or type 'done' to finish): ").strip()
        if category_code.lower() == "done":
            break

        if not category_code.isdigit() or int(category_code) < 1 or int(category_code) > len(categories):
            print("The code entered is incorrect!. Please try again.")
            continue

        category = categories[int(category_code) - 1]
        print(f"\n--- {category} Menu ---")
        print(display_dict_Vendmac(category))
        code = input("Enter the code of the item that you want to purchase (or type 'go back' to go to the categories): ").strip().upper()
        if code.lower() == "back":
            continue

        item = dict_Vendmac[category].get(code)
        if not item:
            print("The code is incorrect!. Please try again.")
            continue

        if item["Stock"] <= 0:
            print(f"Sorry, the item: {item['Name']} is currently not available.")
            continue

        total_cost += item["Price $"]
        item["Stock"] -= 1
        print(f"Added the item: {item['Name']} to your cart. Total currently: ${total_cost:.2f}")

    if total_cost > 0:
        print(f"\nYour total amount is: ${total_cost:.2f}")
        while True:
            payment = float(input("Enter the total amount: $"))
            if payment >= total_cost:
                change = payment - total_cost
                print(f"Payment has been done successfully! Your balance: ${change:.2f}")
                break
            else:
                print(f"Insufficient payment. You still have to pay ${total_cost - payment:.2f}.")
    else:
        print("No items purchased.Thank you.")

    print("Thank you for visiting my Vending Machine")
