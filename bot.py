import os
import logging
import uvicorn
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "9205714747:AAGOJSOSb5NMYVIsxiknin0SPgdVFeMC50A"
)
PUBLIC_URL = os.getenv(
    "PUBLIC_URL",
    "https://bot-1793357431-8359-personawoodoo.bothost.tech"
)
ADMIN_ID = 8959461245

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN не найден! Добавь его в переменные окружения."
    )

if not PUBLIC_URL:
    raise RuntimeError(
        "PUBLIC_URL не найден! Укажи HTTPS-адрес сервера."
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))

    logging.info("Запуск DocuFlow AI...")
    logging.info("Admin ID: %s", ADMIN_ID)

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        workers=1
    )
