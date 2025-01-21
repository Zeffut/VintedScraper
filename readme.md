# Notion Vinted Updater

This project is a Telegram bot that scrapes information from Vinted items and imports them into Notion.

## Prerequisites

- Python 3.7+
- A Telegram account and a Telegram bot
- A Notion account and a Notion integration

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Zeffut/VintedScraper.git
    cd VintedScraper
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the environment variables:
    - Create a `.env` file at the root of the project.
    - Add your Telegram token and Notion integration information:
        ```
        TELEGRAM_TOKEN=your_telegram_token
        NOTION_TOKEN=your_notion_token
        NOTION_DATABASE_ID=your_notion_database_id
        ```

## Usage

1. Start the bot:
    ```bash
    python main.py
    ```

2. Open Telegram and send a message to your bot with a Vinted link.

3. Follow the instructions to import the item into Notion.

## Project Structure

- `main.py`: The main file that contains the logic for the Telegram bot.
- `notion.py`: Contains the `add_item` function to add items to Notion.
- `item.py`: Contains the `scrape_vinted` function to scrape information from Vinted items.
- `ai.py`: Contains the `find_color` and `find_type` functions to determine the color and type of the item from images.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.