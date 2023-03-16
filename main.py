import time

def afficher_heures():
    # Définir l'heure de départ à 16h30
    heure_depart = (16, 30, 0)

    while True:
        # Afficher l'heure
        heures, minutes, secondes = heure_depart
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

        # Augmenter les secondes
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

        # Mettre à jour l'heure de départ
        heure_depart = (heures, minutes, secondes)

        # Attendre une seconde avant la prochaine mise à jour
        time.sleep(1)

# Appel de la fonction pour afficher l'heure à partir de 16h30
afficher_heures()
