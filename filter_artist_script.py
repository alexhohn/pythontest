import sqlite3
con = sqlite3.connect("C:\\Users\\alexa\\Documents\\DocumentsAHN\\02_Etudes\\01_HEIG-VD\\03_2324\\Branches 2324\\ProjDec1\\Exo\\Exo1_Filter_Artists\\filter_artist") #Connection à la base de donnée
cur = con.cursor()                     #Création d'un curseur pour récupérer les données

cur.execute("SELECT stage_name FROM artist")
results = cur.fetchall()  # Récupérer tous les résultats

# Affichage de tous les résultats
for res in results:
    print("Stage Name:", res[0])
else:
    print("Aucun résultat trouvé.")