# Importing the packages used in the program
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd

cart = []

#######-------Make the window-------#######
# main_skaker_window is the main window function of the application which contains all other functions
def main_skaker_window():
    main_window = Tk()
    main_window.title("Skaker Application")
    main_window.geometry("900x700")
    candy_icon = PhotoImage(file="Candy.png")
    main_window.iconphoto(True, candy_icon)
    main_window.configure(bg="#fad7da")

    #######-------Name-------#######
    name = Label(main_window, text="Skaker Application", font=("Times New Roman",50,"bold"), fg="#6d4180", bg="#fad7da")
    name.pack()

# Placing icons in the background
    #######-------Cupcakes icons-------#######
    background = Image.open("cupcake.png")
    cup_image = background.resize((75, 75), Image.Resampling.LANCZOS)
    cup = ImageTk.PhotoImage(cup_image)
    cupcake1 = Label(main_window, image=cup, bg="#fad7da")
    cupcake1.place(x=10, y=100)
    cupcake2 = Label(main_window, image=cup, bg="#fad7da")
    cupcake2.place(x=810, y=500)
    cupcake3 = Label(main_window, image=cup, bg="#fad7da")
    cupcake3.place(x=10, y=400)
    cupcake4 = Label(main_window, image=cup, bg="#fad7da")
    cupcake4.place(x=810, y=0)

    #######-------candy icons-------#######
    candy_bg = Image.open("Candy.png")
    candy_image = candy_bg.resize((75, 75), Image.Resampling.LANCZOS)
    candy = ImageTk.PhotoImage(candy_image)
    candy1 = Label(main_window, image=candy, bg="#fad7da")
    candy1.place(x=10, y=500)
    candy3 = Label(main_window, image=candy, bg="#fad7da")
    candy3.place(x=810, y=200)

    #######-------cotton candy icons-------#######
    cotton_bg = Image.open("cotton_candy.png")
    cotton_image = cotton_bg.resize((75, 75), Image.Resampling.LANCZOS)
    cotton = ImageTk.PhotoImage(cotton_image)
    cotton1 = Label(main_window, image=cotton, bg="#fad7da")
    cotton1.place(x=10, y=0)
    cotton2 = Label(main_window, image=cotton, bg="#fad7da")
    cotton2.place(x=810, y=400)
    cotton3 = Label(main_window, image=cotton, bg="#fad7da")
    cotton3.place(x=10, y=300)

    #######-------Donut icons-------#######
    donut_bg = Image.open("donut.png")
    donut_image = donut_bg.resize((75, 75), Image.Resampling.LANCZOS)
    donut = ImageTk.PhotoImage(donut_image)
    donut1 = Label(main_window, image=donut, bg="#fad7da")
    donut1.place(x=10, y=600)
    donut3 = Label(main_window, image=donut, bg="#fad7da")
    donut3.place(x=810, y=300)

    #######-------Ice Cream icons-------#######
    ice_bg = Image.open("icecream.png")
    ice_image = ice_bg.resize((75, 75), Image.Resampling.LANCZOS)
    ice = ImageTk.PhotoImage(ice_image)
    ice1 = Label(main_window, image=ice, bg="#fad7da")
    ice1.place(x=10, y=200)
    ice2 = Label(main_window, image=ice, bg="#fad7da")
    ice2.place(x=810, y=100)
    ice3 = Label(main_window, image=ice, bg="#fad7da")
    ice3.place(x=810, y=600)

    #######-------Welcome picture-------#######
    welcome_bg = Image.open("welcome1.png")
    welcome_image = welcome_bg.resize((600, 420), Image.Resampling.LANCZOS)
    welcome = ImageTk.PhotoImage(welcome_image)
    welcome_in = Label(main_window, image=welcome, bg="#fad7da")
    welcome_in.place(x=160, y=80)

    #Using pandas package to view the menu
    def view_menu():
        menu = pd.read_excel("Menu.xlsx")
        menu_window = Tk()
        menu_window.title("Our Menu")
        menu_window.geometry("800x700")
        menu_window.configure(bg="#fad7da")
        # Create a scrollable frame with a vertical scrollbar
        canvas = Canvas(menu_window, bg="#fad7da")
        scrollbar = Scrollbar(menu_window, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#fad7da")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        grouped_menu = menu.groupby("category")
        row = 0
        col = 0

        # Grouping menu items by category in the window
        for category, items in grouped_menu:
            category_frame = Frame(scrollable_frame, bg="#fad7da", relief=RIDGE, borderwidth=2)
            category_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nw")
            category_label = Label(category_frame, text=category, bg="#fad7da", font=("Helvetica", 16, "bold"), anchor="w")
            category_label.pack(fill="x", padx=10, pady=5)

            # Adjusting each item and adding spinbox
            for _, item in items.iterrows():
                item_frame = Frame(category_frame, bg="#fad7da")
                item_frame.pack(fill="x", padx=10, pady=5)
                name_label = Label(item_frame, text=f"{item['Dish']}  L.E{item['Price']}",
                                   bg="#fad7da", font=("Helvetica", 14))
                name_label.pack(side="left", padx=10)
                quantity_selector = ttk.Spinbox(item_frame, from_=1, to=20, width=3)
                quantity_selector.pack(side="right")

                # This function allow the user to add order to the cart with the quantity the customer wants.
                def order_item(order=item["Dish"], price=item["Price"], selector=quantity_selector):
                    quantity = int(selector.get())
                    cart.append({"Dish": order, "Quantity": quantity, "Price": price * quantity})
                    print("Ordered",quantity, order,"!")

                # Add to cart button
                order_button = Button(item_frame, text="Add to cart", command=order_item)
                order_button.pack(side="right", padx=10)
            col += 1
            if col > 1:
                col = 0
                row += 1
        # Back to Home button
        back_button = Button(menu_window, text="Back to Home", font=("Helvetica", 14),
                             bg="#6d4180", fg="white", width=17, command=lambda: back_to_home(menu_window))
        back_button.place(x=300, y=500)
        # Checkout button
        checkout = Button(menu_window, text="Proceed to checkout", font=("Helvetica", 14),
                          fg="white", bg="#6d4180", width=17, command=lambda: checkout(menu_window))
        checkout.place(x=300, y=600)

        # Navigate to bill window and close the current one
        def checkout(current_window):
            current_window.destroy()
            view_bill()

        main_window.destroy()
        menu_window.mainloop()

    # Calculate the total price of the ordered items
    def calculate_bill(order):
        total_amount = 0
        bill_details = []

        for dish_name, quantity, price in order:
            bill_details.append(f"{dish_name:<20}{quantity:<10}${price:<10}")
            total_amount += price
        bill_details.append(f"{'Total Amount':<20}${total_amount:<10}")
        return bill_details

    # Creating the bill window
    def view_bill():
        bill_window = Tk()
        bill_window.title("Your Cart")
        bill_window.geometry("600x500")
        bill_window.configure(bg="#fad7da")
        items_frame = Frame(bill_window, bg="#fad7da")
        items_frame.pack(padx=60, pady=30)
        Label(items_frame, text="--- Bill Details ---", font=("Times New Roman", 30), bg="#fad7da").pack(pady=50)

        # Display Bill Details
        bill_items = [(item["Dish"], item["Quantity"], item["Price"]) for item in cart]
        bill_text = calculate_bill(bill_items)
        for line in bill_text:
            Label(items_frame, text=line, font=("Times New Roman", 20), bg="#fad7da").pack(anchor="w")

        # Back to Home button
        back_button = Button(bill_window, text="Back to Home", font=("Times New Roman", 20),
                             bg="#6d4180", fg="white", command=lambda: back_to_home(bill_window))
        back_button.pack(pady=20)
        bill_window.mainloop()

    # View menu button
    menu_view = Button(main_window, text="Show Menu", font=("Times New Roman", 30, "bold"), fg="white",
                       bg="#6d4180", width=17, height=1, command=view_menu)
    menu_view.place(x=250, y=500)

    # view bill button
    bill = Button(main_window, text="Your Cart",  font=("Times New Roman", 30, "bold"), fg="white", bg="#6d4180",
                  width=17, height=1, command=view_bill)
    bill.place(x=250, y=600)
    main_window.mainloop()

# Back to home and close the current window
def back_to_home(current_window):
    current_window.destroy()
    main_skaker_window()

main_skaker_window()

