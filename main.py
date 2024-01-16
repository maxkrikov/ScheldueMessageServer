from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI

from cron import cros
from messages import send_message

app = FastAPI()


@app.get("/send_message")
async def send(id: str):
    await send_message(id)
    return True


@app.get("/create_message")
async def cr(id: str):
    await cros(id)
    return True


if __name__ == "__main__":
    try:
        uvicorn.run(
            app=app,
            host='0.0.0.0',
            port=8000
        )
    except Exception:
        print('❌ FastAPI start filed: {e}')
