from tkinter import *
from random import choice
from random import shuffle 

root = Tk()
root.title("Petit jeu de lettres")
root.configure(background='black')
root.geometry("400x600")
root.iconbitmap("C:/Users/eriol/Desktop/programmation/anagramme/alphabet.ico")

# --------------------------------LES FONCTIONS---------------------------------------------------
def jeu_3_label():
    label_jeu = Label(lettres_3_frame, text="Anagramme : 3 lettres", bg="black", fg="white", font=("Arial", 30))
    label_jeu.pack(pady=5)

    global lettres_3_label
    lettres_3_label = Label(lettres_3_frame, text= "", font=("Arial",32), bg="black", fg="white")
    lettres_3_label.pack(pady=10)

    my_button = Button(lettres_3_frame, text="Nouveau mot", bg="black", fg="white", font=("Arial", 20), command=melange3)    
    my_button.pack(pady=10)
    
    label_reponse = Label(lettres_3_frame, text="Ta réponse :", bg="black", fg="white", font=("Arial", 20))
    label_reponse.pack(pady=5)

    global entry_reponse
    entry_reponse = Entry(lettres_3_frame, font=("Arial", 32), bg="black", fg="white", justify="center", width=10)
    entry_reponse.pack(pady=10)

    verifier_button = Button(lettres_3_frame, text="Vérifier", bg="black", fg="white", font=("Arial", 20), command=verifier) 
    verifier_button.pack(pady=10)

    global resultat_label
    resultat_label = Label(lettres_3_frame, text=" ", bg="black")
    resultat_label.pack(pady=10)

    global mot_label
    mot_label = Label(lettres_3_frame, text="", bg="black", fg="white", font=("Arial", 20))
    mot_label.pack(pady=10)

def jeu_4_label():
    label_jeu = Label(lettres_4_frame, text="Anagramme : 4 lettres", bg="black", fg="white", font=("Arial", 30))
    label_jeu.pack(pady=5)

    global lettres_4_label
    lettres_4_label = Label(lettres_4_frame, text= "", font=("Arial",32), bg="black", fg="white")
    lettres_4_label.pack(pady=10)

    my_button = Button(lettres_4_frame, text="Nouveau mot", bg="black", fg="white", font=("Arial", 20), command=melange4)    
    my_button.pack(pady=10)
    
    label_reponse = Label(lettres_4_frame, text="Ta réponse :", bg="black", fg="white", font=("Arial", 20))
    label_reponse.pack(pady=5)

    global entry_reponse
    entry_reponse = Entry(lettres_4_frame, font=("Arial", 32), bg="black", fg="white", justify="center", width=10)
    entry_reponse.pack(pady=10)

    verifier_button = Button(lettres_4_frame, text="Vérifier", bg="black", fg="white", font=("Arial", 20), command=verifier) 
    verifier_button.pack(pady=10)

    global resultat_label
    resultat_label = Label(lettres_4_frame, text=" ", bg="black")
    resultat_label.pack(pady=10)

    global mot_label
    mot_label = Label(lettres_4_frame, text="", bg="black", fg="white", font=("Arial", 20))
    mot_label.pack(pady=10)

def jeu_5_label():
    label_jeu = Label(lettres_5_frame, text="Anagramme : 5 lettres", bg="black", fg="white", font=("Arial", 30))
    label_jeu.pack(pady=5)

    global lettres_5_label
    lettres_5_label = Label(lettres_5_frame, text= "", font=("Arial",32), bg="black", fg="white")
    lettres_5_label.pack(pady=10)

    my_button = Button(lettres_5_frame, text="Nouveau mot", bg="black", fg="white", font=("Arial", 20), command=melange5)    
    my_button.pack(pady=10)
    
    label_reponse = Label(lettres_5_frame, text="Ta réponse :", bg="black", fg="white", font=("Arial", 20))
    label_reponse.pack(pady=5)

    global entry_reponse
    entry_reponse = Entry(lettres_5_frame, font=("Arial", 32), bg="black", fg="white", justify="center", width=10)
    entry_reponse.pack(pady=10)

    verifier_button = Button(lettres_5_frame, text="Vérifier", bg="black", fg="white", font=("Arial", 20), command=verifier) 
    verifier_button.pack(pady=10)

    global resultat_label
    resultat_label = Label(lettres_5_frame, text=" ", bg="black")
    resultat_label.pack(pady=10)

    global mot_label
    mot_label = Label(lettres_5_frame, text="", bg="black", fg="white", font=("Arial", 20))
    mot_label.pack(pady=10)

def jeu_6_label():
    label_jeu = Label(lettres_6_frame, text="Anagramme : 6 lettres", bg="black", fg="white", font=("Arial", 30))
    label_jeu.pack(pady=5)

    global lettres_6_label
    lettres_6_label = Label(lettres_6_frame, text= "", font=("Arial",32), bg="black", fg="white")
    lettres_6_label.pack(pady=10)

    my_button = Button(lettres_6_frame, text="Nouveau mot", bg="black", fg="white", font=("Arial", 20), command=melange6)    
    my_button.pack(pady=10)
    
    label_reponse = Label(lettres_6_frame, text="Ta réponse :", bg="black", fg="white", font=("Arial", 20))
    label_reponse.pack(pady=5)

    global entry_reponse
    entry_reponse = Entry(lettres_6_frame, font=("Arial", 32), bg="black", fg="white", justify="center", width=10)
    entry_reponse.pack(pady=10)

    verifier_button = Button(lettres_6_frame, text="Vérifier", bg="black", fg="white", font=("Arial", 20), command=verifier) 
    verifier_button.pack(pady=10)

    global resultat_label
    resultat_label = Label(lettres_6_frame, text=" ", bg="black")
    resultat_label.pack(pady=10)

    global mot_label
    mot_label = Label(lettres_6_frame, text="", bg="black", fg="white", font=("Arial", 20))
    mot_label.pack(pady=10)

def melange3():    
    # On crée la liste de mots de 3 lettres a partir u fichier tetxe
    with open("C:/Users/eriol/Desktop/programmation/anagramme/liste.txt") as file:
        lines = file.readlines()  
    # on transforme en liste :
    liste = []
    for line in map(str.rstrip, lines):
        if len(line) == 3:
            liste.append(line)
    
    # on choisit un mot de la liste -> variable global car utilise ailleurs
    global mot_a_trouver
    mot_a_trouver = choice(liste)
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
    
    lettres_3_label.config(text=mot_melange)
    resultat_label.config(text="")
    mot_label.config(text="")
    
def melange4():
    # On crée la liste de mots de 4 lettres a partir u fichier tetxe
    with open("C:/Users/eriol/Desktop/programmation/anagramme/liste.txt") as file:
        lines = file.readlines()  
    # on transforme en liste :
    liste = []
    for line in map(str.rstrip, lines):
        if len(line) == 4:
            liste.append(line)
    
    # on choisit un mot de la liste -> variable global car utilise ailleurs
    global mot_a_trouver
    mot_a_trouver = choice(liste)
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

    lettres_4_label.config(text=mot_melange)
    resultat_label.config(text="")
    mot_label.config(text="")
        
def melange5():
    # On crée la liste de mots de 5 lettres a partir u fichier tetxe
    with open("C:/Users/eriol/Desktop/programmation/anagramme/liste.txt") as file:
        lines = file.readlines()  
    # on transforme en liste :
    liste = []
    for line in map(str.rstrip, lines):
        if len(line) == 5:
            liste.append(line)
    
    # on choisit un mot de la liste -> variable global car utilise ailleurs
    global mot_a_trouver
    mot_a_trouver = choice(liste)
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

    lettres_5_label.config(text=mot_melange)
    resultat_label.config(text="")
    mot_label.config(text="")

def melange6():
    # On crée la liste de mots de 5 lettres a partir u fichier tetxe
    with open("C:/Users/eriol/Desktop/programmation/anagramme/liste.txt") as file:
        lines = file.readlines()  
    # on transforme en liste :
    liste = []
    for line in map(str.rstrip, lines):
        if len(line) == 6:
            liste.append(line)
    
    # on choisit un mot de la liste -> variable global car utilise ailleurs
    global mot_a_trouver
    mot_a_trouver = choice(liste)
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

    lettres_6_label.config(text=mot_melange)
    resultat_label.config(text="")
    mot_label.config(text="")



# fonctions des lettres
def lettres_3():
    hide_menu_frame()
    lettres_3_frame.pack(fill="both",expand=1)
    jeu_3_label()
    melange3()


def lettres_4():
    hide_menu_frame()
    lettres_4_frame.pack(fill="both",expand=1)
    jeu_4_label()
    melange4()
    

def lettres_5():    
    hide_menu_frame()
    lettres_5_frame.pack(fill="both",expand=1)
    jeu_5_label()
    melange5()

def lettres_6():
    hide_menu_frame()
    lettres_6_frame.pack(fill="both",expand=1)
    jeu_6_label()
    melange6()

# fonction effacer frame
def hide_menu_frame():
    lettres_3_frame.pack_forget()
    lettres_4_frame.pack_forget()
    lettres_5_frame.pack_forget()
    lettres_6_frame.pack_forget()
    choix_frame.pack_forget()


def verifier():    
    if mot_a_trouver == entry_reponse.get():
        resultat_label.config(text="Gagné!!!", font=("Arial",32), bg="black",fg="green")
        mot_label.config(text="Tu as trouvé le bon mot!")

    else:        
        resultat_label.config(text="Perdu...", font=("Arial",32), bg="black",fg="red")
        mot_label.config(text="La réponse était : " + mot_a_trouver)
    
    entry_reponse.delete(0, "end")
    


# on crée le menu principal
mon_menu = Menu(root)
root.config(menu=mon_menu)

def choix():
    hide_menu_frame()
    choix_frame.pack(fill="both", expand=1)
    choix_label = Label(choix_frame, text=" Bienvenu(e) dans le jeu", font=("Arial",20), bg="black",fg="white")    
    choix_label.pack(pady=20)
    choix_label2 = Label(choix_frame, text=" de l'anagramme", font=("Arial",20), bg="black",fg="white")    
    choix_label2.pack(pady=20)
    l3_button = Button(choix_frame, text="Mots de 3 lettres", font=("Arial",20), bg="black",fg="white", command=lettres_3) 
    l3_button.pack(pady=5)
    l4_button = Button(choix_frame, text="Mots de 4 lettres", font=("Arial",20), bg="black",fg="white", command=lettres_4) 
    l4_button.pack(pady=5)
    l5_button = Button(choix_frame, text="Mots de 5 lettres", font=("Arial",20), bg="black",fg="white", command=lettres_5) 
    l5_button.pack(pady=5)
    l6_button = Button(choix_frame, text="Mots de 6 lettres", font=("Arial",20), bg="black",fg="white", command=lettres_6) 
    l6_button.pack(pady=5)




# les items du menu
anagramme_menu = Menu(mon_menu)
mon_menu.add_cascade(label="Anagrammes", menu=anagramme_menu)
anagramme_menu.add_command(label="3 lettres", command=lettres_3)
anagramme_menu.add_command(label="4 lettres", command=lettres_4)
anagramme_menu.add_command(label="5 lettres", command=lettres_5)
anagramme_menu.add_command(label="6 lettres", command=lettres_6)
anagramme_menu.add_separator()
anagramme_menu.add_command(label="Quitter", command=root.quit)

# on crée les frames
lettres_3_frame = Frame(root, width=400, height=600, bg="black")
lettres_4_frame = Frame(root, width=400, height=600, bg="black")
lettres_5_frame = Frame(root, width=400, height=600, bg="black")
lettres_6_frame = Frame(root, width=400, height=600, bg="black")
choix_frame = Frame(root, width=400, height=600, bg="black")

choix()

root.mainloop()
    