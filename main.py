from notation import calculer_points

# Programme principal avec un exemple
# Vous êtes libres de le modifier si ça vous aide à tester et à déboguer,
# mais normalement il n'y a rien à corriger ici.

if __name__ == "__main__":
    noms = ["Alex", "Marie", "Paul", "Zoé"]
    vbases = [3.2, 4.0, 2.5, 3.0]
    notes_2d = [
        [3, 2, 1, 2, 3, 3, 2, 2, 3],
        [1, 1, 2, 0, 1, 2, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 2, 1, 0, 2, 3, 2, 2, 3]
    ]




    print("=== Résultats de la compétition ===")
    for i in range(len(noms)):
        try:
            total = calculer_points(vbases[i], notes_2d[i])
            print(noms[i], ":", total, "points", vbases[i])
        except:
            print(noms[i], ": erreur")