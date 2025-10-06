from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.settings import settings
from models.responses import ok_200
from routes.geo.country import country_router
from routes.text.humanize import humanize_router
from routes.text.case_convert import case_convert_router
from routes.text.convert import text_conversion_router

from routes.io.io import io_router
from routes.user.auth import auth_router
from routes.user.user_data import user_data_router
from routes.finance.currency import router as currency_router

app = FastAPI(title="API Dash APIs",
              description="Open Source APIs for all!",
              version="0.0.3",
              contact={
                  "name": "Know more about API Dash",
                  "url": settings.site_url,
              },)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(country_router, prefix="/country")
app.include_router(humanize_router, prefix="/humanize")
app.include_router(text_conversion_router, prefix="/convert")
app.include_router(case_convert_router, prefix="/case")
app.include_router(io_router, prefix="/io")
app.include_router(auth_router, prefix="/auth") 
app.include_router(user_data_router, prefix="")
app.include_router(currency_router, prefix="/currency")

@app.get("/")
async def welcome():
    return ok_200(settings.msg_welcome)
