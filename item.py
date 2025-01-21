import requests
from bs4 import BeautifulSoup

def scrape_vinted(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.vinted.fr/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers"
    }

    # Envoyer une requête GET à la page Vinted avec des en-têtes
    response = requests.get(link, headers=headers)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Vérifier que l'URL n'a pas été redirigée vers une page d'erreur
    if response.url != link:
        raise requests.exceptions.HTTPError(f"Redirection vers une page d'erreur: {response.url}")

    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrapper les images dans la div avec la classe 'item-photos'
    item_photos_div = soup.find('div', class_='item-photos')
    images = item_photos_div.find_all('img', class_='web_ui__Image__content')
    image_urls = [img['src'] for img in images]

    # Trouver et afficher le prix
    price_button = soup.select_one('button[aria-label*="€"]')
    price = price_button['aria-label'].split(' ')[0] if price_button else "Non trouvé"
    if price != "Non trouvé":
        price = float(price.replace("\xa0€", "").replace(",", "."))
    
    # Trouver et afficher le nom de l'article
    item_name = soup.select_one('span.web_ui__Text__title')
    item_name = item_name.text if item_name else "Non trouvé"

    # Trouver et afficher la marque
    brand_element = soup.select_one('a[href*="brand_ids"] span.web_ui__Text__body')
    brand = brand_element.text if brand_element else "Non trouvé"

    # Trouver et afficher la taille
    size_element = soup.select_one('div[data-testid="item-attributes-size"] span.web_ui__Text__bold')
    size = size_element.text if size_element else "Non trouvé"

    # Trouver et afficher l'état de l'objet
    condition_element = soup.select_one('div[data-testid="item-attributes-status"] span.web_ui__Text__bold')
    condition = condition_element.text if condition_element else "Non trouvé"

    # Trouver et afficher la localisation de l'article
    location_element = soup.select_one('div[data-testid="item-attributes-location"] span.web_ui__Text__bold')
    location = location_element.text if location_element else "Non trouvé"

    # Trouver et afficher le nombre de vues de l'article
    view_count_element = soup.select_one('div[data-testid="item-attributes-view_count"] span.web_ui__Text__bold')
    view_count = view_count_element.text if view_count_element else "Non trouvé"

    # Trouver et afficher la date d'ajout de l'article
    upload_date_element = soup.select_one('div[data-testid="item-attributes-upload_date"] span.web_ui__Text__bold')
    upload_date = upload_date_element.text if upload_date_element else "Non trouvé"

    # Trouver et afficher le statut de l'article
    status_element = soup.select_one('div[data-testid="item-status"] div[data-testid="item-status--content"]')
    status = status_element.text if status_element else "Non Vendu"
    
    return {
        "price": price,
        "item_name": item_name,
        "brand": brand,
        "size": size,
        "condition": condition,
        "location": location,
        "view_count": view_count,
        "upload_date": upload_date,
        "status": status,
        "image_urls": image_urls
    }

if __name__ == "__main__":
    link = 'https://www.vinted.fr/items/5685691380-nike-t-shirt'
    data = scrape_vinted(link)
    
    price = data["price"]
    item_name = data["item_name"]
    brand = data["brand"]
    size = data["size"]
    condition = data["condition"]
    location = data["location"]
    view_count = data["view_count"]
    upload_date = data["upload_date"]
    status = data["status"]
    image_urls = data["image_urls"]

    print(f"Nom de l'article: {item_name}")
    print(f"Marque: {brand}")
    print(f"Taille: {size}")
    print(f"Condition: {condition}")
    print(f"Localisation: {location}")
    print(f"Nombre de vues: {view_count}")
    print(f"Date d'ajout: {upload_date}")
    print(f"Prix: {price}")
    print(f"Statut: {status}")
    print("URLs des images:")
    for idx, url in enumerate(image_urls):
        print(f"  Image {idx + 1}: {url}")
