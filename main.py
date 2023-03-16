import time

def afficher_heures():
    # Définir l'heure de départ à 16h30
    heure_depart = (16, 30, 00)
    heure_alarme = (16, 31, 00)
   
    while True:
        # Afficher l'heure
        heures, minutes, secondes = heure_depart
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

        if heure_depart == heure_alarme:
            print("C'est l'heure")
            break
        heures, minutes, secondes = heure_depart
        secondes += 1

        # Si les secondes atteignent 60, incrémenter les minutes et réinitialiser les secondes
        if secondes == 60:
            secondes = 0
            minutes += 1

            # Si les minutes atteignent 60, incrémenter les heures et réinitialiser les minutes
            if minutes == 60:
                minutes = 0
                heures += 1

                # Si les heures atteignent 24, réinitialiser les heures à 0
                if heures == 24:
                    heures = 0

                heure_depart = (heures, minutes, secondes)
      
        time.sleep(1)

# Appel de la fonction pour afficher l'heure à partir de 16h30
afficher_heures()


