import os
from notion_client import Client

# Initialisation du client avec ton token secret
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# ID de ta base de données
database_id = os.getenv("NOTION_DATABASE_ID")

# Fonction pour récupérer les données du tableau
def recuperer_donnees():
    try:
        response = notion.databases.query(database_id=database_id)
    except Exception as e:
        print("Erreur lors de la récupération des données :", e)

# Fonction pour ajouter une nouvelle entrée
def ajouter_article(produit, statut, couleur=None, prix_vendeur=None, prix_achat=None, type_article=None, photos=None):
    recuperer_donnees()
    try:
        # Ici, nous n'avons pas besoin de convertir les prix en nombres car ils sont déjà fournis comme tels
        properties = {
            "Product": {"title": [{"text": {"content": produit}}]},
            "Status": {"select": {"name": statut}},
        }
        if couleur:
            properties["Couleur"] = {"select": {"name": couleur}}
        if prix_vendeur is not None:
            properties["Prix vendeur"] = {"number": prix_vendeur}
        if prix_achat is not None:
            properties["Prix d'achat"] = {"number": prix_achat}
        if type_article:
            properties["Type"] = {"select": {"name": type_article}}
        if photos:
            properties["Pictures"] = {"files": [{"name": photo["name"], "type": "external", "external": {"url": photo["url"]}} for photo in photos]}

        # Ajout de la page à la base de données
        notion.pages.create(
            parent={"database_id": database_id},
            properties=properties,
        )
    except Exception as e:
        print("Erreur lors de l'ajout d'une ligne :", e)

# Exemple d'utilisation
if __name__ == "__main__":
    recuperer_donnees()
    # Ajouter un article fictif
    ajouter_article(
        produit="T-shirt Test",
        statut="Acquisition",
        couleur="Bleu",
        prix_vendeur=5.95,  # Le prix est déjà un nombre
        prix_achat=15,
        type_article=["T-shirt"],  # Assurez-vous que c'est une liste pour multi_select
        photos=[{"name": "tshirt_test.jpeg", "url": "https://images1.vinted.net/t/04_022cb_nCZGSGxcVLsDi8yNY7oE444W/f800/1737395645.jpeg?s=2fcd20ae1a7d2b226a18b27ea2408e1a87e665f7"}]
    )
