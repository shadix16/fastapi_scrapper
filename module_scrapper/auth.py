from fastapi import Header, HTTPException
from module_scrapper.settings import TOKEN


def check_auth(Authorization: str = Header(...)):
    """check authorization"""
    if Authorization != TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
