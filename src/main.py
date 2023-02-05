from fastapi import FastAPI
from models.settings import const
from routes import *

app = FastAPI(title = "foss42 APIs",
              description= "Open Source APIs for all!",
              version= "0.0.1",
              contact = {
                "name": "Get Help with this API",
                "url": const.site_foss42,
              },)

app.include_router(humanize_router, prefix="/humanize")
app.include_router(text_conversion_router, prefix="/convert")
app.include_router(case_convert_router, prefix="/case")

@app.get("/")
async def welcome() -> dict:
    return {
        const.k_message: const.msg_welcome
    }
