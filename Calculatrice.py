import tkinter as tk

def addition(n1, n2):
    return n1 + n2

def soustraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erreur : Division par zéro"

def calculer():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_choice.get()

    if operation == "Addition":
        result = addition(num1, num2)
    elif operation == "Soustraction":
        result = soustraction(num1, num2)
    elif operation == "Multiplication":
        result = multiplication(num1, num2)
    elif operation == "Division":
        result = division(num1, num2)
    else:
        result = "Opération non valide"

    result_label.config(text=f"Résultat : {result}")

app = tk.Tk()
app.title("Calculatrice")

label_num1 = tk.Label(app, text="Nombre 1:")
label_num1.pack()
entry_num1 = tk.Entry(app)
entry_num1.pack()

label_num2 = tk.Label(app, text="Nombre 2:")
label_num2.pack()
entry_num2 = tk.Entry(app)
entry_num2.pack()

operation_choice = tk.StringVar()
operation_choice.set("Addition")
operations = ["Addition", "Soustraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(app, operation_choice, *operations)
operation_menu.pack()
calculate_button = tk.Button(app, text="Calculer", command=calculer)
calculate_button.pack()

result_label = tk.Label(app, text="Résultat :")
result_label.pack()

app.mainloop()