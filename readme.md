# Notion Vinted Updater

Ce projet est un bot Telegram qui permet de scraper des informations d'articles Vinted et de les importer dans Notion.

## Prérequis

- Python 3.7+
- Un compte Telegram et un bot Telegram
- Un compte Notion et une intégration Notion

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/Notion_Vinted_Updater.git
    cd Notion_Vinted_Updater
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :
    - Créez un fichier `.env` à la racine du projet.
    - Ajoutez votre token Telegram et les informations d'intégration Notion :
        ```
        TELEGRAM_TOKEN=your_telegram_token
        NOTION_TOKEN=your_notion_token
        NOTION_DATABASE_ID=your_notion_database_id
        ```

## Utilisation

1. Démarrez le bot :
    ```bash
    python main.py
    ```

2. Ouvrez Telegram et envoyez un message à votre bot avec un lien Vinted.

3. Suivez les instructions pour importer l'article dans Notion.

## Structure du projet

- `main.py` : Le fichier principal qui contient la logique du bot Telegram.
- `notion.py` : Contient la fonction `ajouter_article` pour ajouter des articles à Notion.
- `item.py` : Contient la fonction `scrape_vinted` pour scraper les informations des articles Vinted.
- `ai.py` : Contient les fonctions `trouver_couleur` et `trouver_type` pour déterminer la couleur et le type de l'article à partir des images.
- `requirements.txt` : Liste des dépendances Python.

## Contribuer

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour toute amélioration ou correction de bug.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.