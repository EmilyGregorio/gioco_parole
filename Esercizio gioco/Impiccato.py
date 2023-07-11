
#Parola:_ _ _ _ _ _ 
#Inserisci una lettera: a
#se c'è la lettera giusta allora la posiziona al posto giusto se non è presente dice che non è presente 
#e tutto ciò non deve superare un numero massimo di tentativi
import random

#lista di parole predefinite
parole=["casa","albero","tavolo","macchina","salmone"]


#Funzione che restituisce il numero di tentativi in base al livello scelto dall'utente
def livello():
    x=int(input("Scegli il livello del gioco:  Basso=0, Medio=1, Alto=2"))
    if x==0: 
        return 10
    elif x==1:
        return 5
    else: 
        return 3


num_tentativi=livello()

#Funzione per verificare se la parola è giusta
def verifica_parola(parola_gioco,num_tentativi):
   
   while num_tentativi>0:

    
    if parola_utente == parola_nascosta:
      print("Hai indovinato la parola correttamente! Hai vinto 🕺🕺🕺 ")
      break
    else:
      tentativi = tentativi - 1
      print(f"Tentativi residui: {tentativi} \n")
      for lettera, carattere in zip(parola_nascosta, parola_utente):
            
            
            
            
            if 
            elif carattere in parola_nascosta:
                print(carattere + " ➕ ")
            else:
                print(carattere + " ❌ ")
      if tentativi == 0:
        print(" Hai perso  parola_nascosta = "amico"
  tentativi = 6
  while tentativi > 0:
    parola_utente = str(input("Indovina la parola: "))
    if parola_utente == parola_nascosta:
      print("Hai indovinato la parola correttamente! Hai vinto 🕺🕺🕺 ")
      break
    else:
      tentativi = tentativi - 1
      print(f"Tentativi residui: {tentativi} \n")
      for lettera, carattere in zip(parola_nascosta, parola_utente):
            if carattere in parola_nascosta and carattere in lettera:
                print(carattere + " ✅ ")
            elif carattere in parola_nascosta:
                print(carattere + " ➕ ")
            else:
                print(carattere + " ❌ ")
      if tentativi == 0:
        print(" Hai perso 🙁 ")












#Generiamo una parola random da una lista predefinita
parola_gioco=random.choice(parole)







    