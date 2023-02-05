from pydantic import BaseSettings

class Settings(BaseSettings):
    org_name: str = "foss42"
    site_foss42: str = "https://foss42.com"
    site_api: str = "https://localhost:8000"
    site_swagger_docs: str = f"{site_api}/docs"
    site_redoc_docs: str = f"{site_api}/redoc"
    site_gh: str = "https://github.com"
    site_gh_org: str = f"{site_gh}/{org_name}"
    repo_apis: str = f"{site_gh_org}/api"
    repo_corelib: str = f"{site_gh_org}/foss42"
    url_issue: str = f"{repo_apis}/issues"
    url_discussion: str = f"{repo_apis}/discussions"

    k_message: str = "message"
    k_data: str = "data"
    msg_welcome: str = f"Check out {site_foss42} for API docs to get started."
    msg_raise_issue: str = f"In case the error is unexpected, you can report or ask for support here - {url_issue}"
    msg_invalid_input: str = f"An error was caused for the input. Please check the docs. {msg_raise_issue}"

const = Settings()
