# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) < 9:
        return False

    for n in notes:
        if n > 3:
            return False
    else:
        return True



def calculer_points(vbase: float, notes: list[int]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    #pour la fonction de calculer les points la list note est un nombre entier pas de nombre decimal
    try:
        valider_notes(notes)

        note_max = max(notes)
        note_min = min(notes)


        for i in range(len(notes)):
            if notes[i] == note_max and note_min:
                notes.remove(notes[i])
        #il faut enlever les deux notes

        moyenne = sum(notes) / 7
        # il y a maintenant seulement seulement 7 notes
        total = vbase + moyenne
        return total

    except ValueError:
        print("Erreur")
        return 0



