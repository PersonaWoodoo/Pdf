import os
import asyncio
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


async def main():
    token = os.environ["BOT_TOKEN"].strip()
    secret = os.environ["WEBHOOK_SECRET"].strip()
    base = os.environ["PUBLIC_URL"].strip().rstrip("/")
    url = f"{base}/telegram/webhook"

    payload = {
        "url": url,
        "secret_token": secret,
        "allowed_updates": ["message", "pre_checkout_query"],
        "drop_pending_updates": True,
    }

    async with httpx.AsyncClient(timeout=20) as c:
        r = await c.post(
            f"https://api.telegram.org/bot{token}/setWebhook",
            json=payload,
        )
        data = r.json()
        print(data)
        if not data.get("ok"):
            raise SystemExit(f"setWebhook failed: {data}")


if __name__ == "__main__":
    asyncio.run(main())
