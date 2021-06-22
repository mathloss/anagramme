from tkinter import *
from random import choice
from random import shuffle 

root = Tk()
root.title("Anagramme")
root.configure(background='black')
root.geometry("400x600")
root.iconbitmap("C:/Users/eriol/Desktop/anagramme/alphabet.ico")



def melange(): 
    # On efface le entry box et resultat label 
    entry_reponse.delete(0,END)  
    label_reponse.config(text="")
    

    # On crée la liste de mots de 5 lettres a partir u fichier tetxe
    with open("C:/Users/eriol/Desktop/anagramme/liste5.txt") as file:
        lines = file.readlines()  
    # on transforme en liste :
    liste_5m = []
    for line in map(str.rstrip, lines):
        if len(line) == 5:
            liste_5m.append(line)
    
        # on choisit un mot de la liste -> variable global car utilise ailleurs
        global mot_a_trouver
        mot_a_trouver = choice(liste_5m)
        mot_a_trouver = mot_a_trouver.lower()
        

        # on va casser le mot pour en faire une liste de lettres
        mot_casse = list(mot_a_trouver)
        # on melange le lettres
        shuffle(mot_casse)
        # on fait des lettres melangees un mot -> variable globale cau utilise ailleurs
        global mot_melange
        mot_melange = ""
        for lettre in mot_casse:
            mot_melange += lettre 
        # on affiche le mot melange
        my_label.config(text=mot_melange)

def verifier():
    
    if mot_a_trouver == entry_reponse.get():
        resultat_label.config(text="Gagné!!!", font=("Arial",32), bg="black",fg="green")
        mot_label.config(text="Tu as trouvé le bon mot!")

    else:        
        resultat_label.config(text="Perdu...", font=("Arial",32), bg="black",fg="red")
        mot_label.config(text="La réponse était : " + mot_a_trouver)


my_label = Label(root, text = "", font=("Arial", 32), bg="black", fg="white")
my_label.pack()

my_button = Button(root, text="Nouveau mot", bg="black", fg="white", font=("Arial", 20), command=melange)    
my_button.pack(pady=10)

label_reponse = Label(root, text="Ta réponse :", bg="black", fg="white", font=("Arial", 20))
label_reponse.pack(pady=5)

entry_reponse = Entry(root, font=("Arial", 32), bg="black", fg="white", justify="center", width=10)
entry_reponse.pack(pady=10)

verifier_button = Button(root, text="Vérifier", bg="black", fg="white", font=("Arial", 20), command=verifier) 
verifier_button.pack(pady=10)

resultat_label = Label(root, text=" ", bg="black")
resultat_label.pack(pady=10)

mot_label = Label(root, text="", bg="black", fg="white", font=("Arial", 20))
mot_label.pack(pady=10)

melange()

root.mainloop()
    