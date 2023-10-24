import tkinter as tk


fenetre = tk.Tk()
fenetre.title("Interface d'inscription")


pseudo= tk.Label(fenetre, text="Pseudo:")
pseudo.pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()


motdepasse = tk.Label(fenetre, text="Mot de passe:")
motdepasse.pack()
motdepasse_entry = tk.Entry(fenetre, show="*")
motdepasse_entry.pack()


email = tk.Label(fenetre, text="Email:")
email.pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()


def confirmer_inscription():
    pseudo = pseudo_entry.get()
    motdepasse = motdepasse_entry.get()
    email = email_entry.get()

    if "@" not in email:
        print("e-mail invalide")
    else:
        print("Pseudo:", pseudo)
        print("Mot de passe:", motdepasse)
        print("Email:", email)

valider_button = tk.Button(fenetre, text="Valider l'inscription", command=confirmer_inscription)
valider_button.pack()


fenetre.geometry("400x300")
fenetre.mainloop()