import os
import logging
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
log = logging.getLogger("docuflow")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
PUBLIC_URL = os.getenv("PUBLIC_URL", "").strip().rstrip("/")
ADMIN_IDS = [x.strip() for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не найден. Добавь в .env или переменные окружения.")
if BOT_TOKEN.startswith("PASTE_"):
    raise RuntimeError("BOT_TOKEN выглядит как заглушка. Укажи реальный токен.")
if not PUBLIC_URL:
    raise RuntimeError("PUBLIC_URL не найден. Укажи HTTPS-адрес сервера.")
if not PUBLIC_URL.startswith("https://"):
    raise RuntimeError("PUBLIC_URL должен начинаться с https://")

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT", "8000"))
    except ValueError:
        raise RuntimeError("PORT должен быть числом")

    reload = os.getenv("RELOAD", "0") == "1"

    log.info("Запуск DocuFlow AI | port=%s reload=%s admins=%s", port, reload, ADMIN_IDS or "—")

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        workers=1,
        reload=reload,
    )
