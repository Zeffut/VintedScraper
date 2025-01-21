import requests
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from io import BytesIO

# Charger le modèle et le processeur
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def trouver_couleur(image_urls):
    couleurs = []
    for image_url in image_urls:
        # Télécharger l'image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Définir des descriptions potentielles
        texts = ["Rouge", "Noir", "Bleu", "Vert", "Jaune", "Marron", "Rose", "Violet", "Gris", "Orange"]

        # Préparer les entrées
        inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

        # Calculer les similarités
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)

        # Trouver la couleur avec la plus grande probabilité
        max_prob, max_index = probs[0].max(dim=0)
        couleurs.append(texts[max_index])

    # Retourner la couleur la plus fréquente
    return max(set(couleurs), key=couleurs.count)

def trouver_type(image_urls):
    types = []
    for image_url in image_urls:
        # Télécharger l'image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Définir des descriptions potentielles
        texts = ["Têtes", "Pulls / Vestes", "T-Shirts", "Chaussures", "Pantalon"]

        # Préparer les entrées
        inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

        # Calculer les similarités
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)

        # Trouver le type avec la plus grande probabilité
        max_prob, max_index = probs[0].max(dim=0)
        types.append(texts[max_index])

    # Retourner le type le plus fréquent
    return max(set(types), key=types.count)
