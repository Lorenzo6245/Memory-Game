import os
import random
import time
import ast
from time import perf_counter
import saverecord

letterEasy = "abcd"
letterNormal = "abcdefg"
letterDif = "abcdefghijklmno"
numberEasy = "1234"
numberNormal = "0123456"
numberDif = "0123456789"
sequenza = ""
punteggio = 0
tempodigioco = 0
Newrecord = saverecord.record
end = 0

# prende l'orario di inizio
start = perf_counter()

print("Welcome to the 🄼․🄴․🄼․🄾․🅁․🅈․🄶․🄰․🄼․🄴")

f = open("GiochinoMemory/saverecord.py", "w")
# apre il file saverecord.py dove viene salvato il punteggio più alto

f.write("record = " + str(Newrecord))
# scrive la variabile record nel file

f.close()    
# chiude il file

time.sleep(1)

def menu(punteggio, record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord):
    
    os.system("clear")
    print("███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗")
    time.sleep(0.25)
    print("████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝")
    time.sleep(0.25)
    print("██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝ ╚████╔╝     ██║  ███╗███████║██╔████╔██║█████╗  ")
    time.sleep(0.25)
    print("██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗  ╚██╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ")
    time.sleep(0.25)
    print("██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║   ██║       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗")
    time.sleep(0.25)
    print("╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    time.sleep(0.5)
    gamemode = input("select the game mode (write letter for letter mode write, number for number mode or exit to quit the game) :) --->")
    if gamemode == "exit":
        exit()
    difficult = input("select difficult(write easy, normal, difficult or exit to quit the game) --->")
    #in base alle scelte del giocatore verranno proposte le diverse modalità
    if difficult == "exit":
        exit()
    
    if gamemode == "letter" and difficult == "easy":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(letterEasy)

            for letterE in sequenza:
                print(letterE)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)            
    if gamemode == "letter" and difficult == "normal":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(letterNormal)

            for letterN in sequenza:
                print(letterN)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)
    if gamemode == "letter" and difficult == "difficult":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(letterDif)

            for letterD in sequenza:
                print(letterD)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)
    if gamemode == "number" and difficult == "easy":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(numberEasy)

            for numE in sequenza:
                print(numE)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)
    if gamemode == "number" and difficult == "normal":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(numberNormal)

            for numN in sequenza:
                print(numN)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)
    if gamemode == "number" and difficult == "normal":
        while True:

            #se il punteggio è maggiore del record cambia il valore del record
            if punteggio > saverecord.record:
                Newrecord = punteggio
            else:
                Newrecord = saverecord.record

            os.system("clear")
            
            sequenza += random.choice(numberDif)

            for numD in sequenza:
                print(numD)
                time.sleep(1)
                os.system("clear")
                time.sleep(0.2)

            risposta = input("Repeat ;) (write menu to save and go to the menu)---->")

            if risposta != sequenza:
                # pulisce lo schermo
                os.system("clear")
                # prende l'orario di fine e calcola il tempo di gioco
                end = perf_counter()
                tempodigioco = end - start
                # controlla se c'è un nuovo record e salva
                if punteggio > saverecord.record:
                    Newrecord = punteggio
                else:
                    Newrecord = saverecord.record

                f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                f.close()    
                    # chiude il file
                print("game saved")
                # scrive i risultati
                print("Game Over, your actual score:", punteggio)
                print("you played for", tempodigioco,"second")
                print("your record:", Newrecord)
                break
                
            else:
                if risposta != "menu":
                    # aggiunge un punto
                    punteggio += 1
                    # hai vinto passi al prossimo livello e ricomincia ma con un numero/lettera in più
                    print("Good job, your actual score is", punteggio)
                    
                else:
                    # controlla se c'è un nuovo record e salva
                    if punteggio > saverecord.record:
                        Newrecord = punteggio
                    else:
                        Newrecord = saverecord.record

                    f = open("GiochinoMemory/saverecord.py", "w")
                    # apre il file saverecord.py dove viene salvato il punteggio più alto

                    f.write("record = " + str(Newrecord))
                    # scrive la variabile record nel file

                    f.close()    
                    # chiude il file
                    print("game saved")

                    os.system("clear")
                    menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

            
            time.sleep(1)
    #se il giocatore non scriverà bene la modalità di gioco o la difficoltà
    if gamemode != "number" or gamemode != "letter" or difficult != "easy" or difficult != "normal" or difficult != "difficult":
        print("sorry retry to select the gamemode and the difficult")
        time.sleep(2)
        menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)

menu(punteggio, saverecord.record, letterEasy,letterNormal, letterDif, numberEasy, numberNormal, numberDif, input, tempodigioco, start, end, sequenza, Newrecord)