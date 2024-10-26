import tkinter as tk

def afficher_message():
    nom = entree_nom.get()
    message_label.config(text=f"Bonjour, {nom} !")

root = tk.Tk()
root.title("Bienvenue")

# Champ de saisie
entree_nom = tk.Entry(root)
entree_nom.pack()

# Bouton
bouton_valider = tk.Button(root, text="Valider", command=afficher_message)
bouton_valider.pack()

# Label pour afficher le message
message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
