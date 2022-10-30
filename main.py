from tkinter import *
import requests

# Barvy
main_color = "#14085f"

# Okno
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.title("Převod měn verze 2.0")
window.config(bg=main_color)


# Funkce
def count():
    try:
        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = int(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
          "apikey": "4WMAzvOMkubfITAPtvBZrQRYkFuhZY4m"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.config(text=round(data_result["result"], 2))
        notification_label.config(text="")
    except:
        notification_label.config(text="Zadejte prosím částku")


# Uživatelský vstup
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Roletka - z jaké měny
drop_down_from = StringVar(window)
drop_down_from.set("CZK")  # výchozí hodnota
drop_down_from_options = OptionMenu(window, drop_down_from, "CZK", "EUR", "USD")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

# Roletka - na jakou měnu
drop_down_to = StringVar(window)
drop_down_to.set("CZK")
drop_down_to_options = OptionMenu(window, drop_down_to, "CZK", "EUR", "USD")
drop_down_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# Tlačítko přepočtu
count_button = Button(text="Přepočítat", font=("Arial", 12), command=count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Label pro zobrazení výsledku převodu
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0)

# Upozorňující label
notification_label = Label(bg=main_color, fg="white", font=("Arial", 12))
notification_label.grid(row=2, column=0)

# Hlavní cyklus
window.mainloop()
