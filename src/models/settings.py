from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    site_url: str = "https://apidash.dev"
    site_api: str = "https://api.apidash.dev"
    site_swagger_docs: str = f"{site_api}/docs"
    site_redoc_docs: str = f"{site_api}/redoc"
    msg_welcome: str = f"Check out {site_swagger_docs} to get started."


settings = Settings()
