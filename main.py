from notion import ajouter_article
from item import scrape_vinted
from ai import trouver_couleur, trouver_type
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler
import os, logging
import uuid

logging.basicConfig()

# Dictionnaire global pour stocker les liens
links_dict = {}

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Envoyez-moi un lien Vinted pour commencer.')

async def handle_link(update: Update, context: CallbackContext) -> None:
    link = update.message.text
    print(f"Lien reçu: {link}")
    if 'vinted' in link:
        # Générer un identifiant unique pour le lien
        link_id = str(uuid.uuid4())
        links_dict[link_id] = link

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
        couleur = trouver_couleur(image_urls)
        type_article = trouver_type(image_urls)

        message = (
            f"🛍️ *Nom de l'article:* {item_name}\n"
            f"🏷️ *Marque:* {brand}\n"
            f"📏 *Taille:* {size}\n"
            f"✨ *État:* {condition}\n"
            f"🎨 *Couleur:* {couleur}\n"
            f"🗂️ *Type:* {type_article}\n"
            f"📍 *Localisation:* {location}\n"
            f"💶 *Prix:* {price}\n"
            f"👀 *Nombre de vues:* {view_count}\n"
            f"📅 *Date de mise en ligne:* {upload_date}\n"
            f"📦 *Statut:* {status}\n"
        )

        keyboard = [
            [InlineKeyboardButton("Importer sur Notion", callback_data=f"import_{link_id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_photo(photo=image_urls[0], caption=message, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await update.message.reply_text('Veuillez envoyer un lien Vinted valide.')

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    if query.data.startswith("import_"):
        link_id = query.data.split("import_")[1]
        link = links_dict.get(link_id)
        if link:
            data = scrape_vinted(link)
            price = data["price"]
            item_name = data["item_name"]
            image_urls = data["image_urls"]
            couleur = trouver_couleur(image_urls)
            type_article = trouver_type(image_urls)

            ajouter_article(
                produit=item_name,
                statut="Acquisition",
                prix_vendeur=price,
                photos=[{"name": f"image_{idx + 1}.jpeg", "url": url} for idx, url in enumerate(image_urls)],
                couleur=couleur,
                type_article=type_article
            )
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(text="Article ajouté avec succès sur Notion.")
        else:
            await query.message.reply_text(text="Erreur: lien non trouvé.")

def main() -> None:
    # Remplacez par votre propre token Telegram
    application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    # Ajouter les gestionnaires de commandes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot démarré.")

    application.run_polling()

if __name__ == '__main__':
    main()
