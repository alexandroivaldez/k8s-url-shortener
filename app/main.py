from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import string
import random

app = FastAPI()

# temporary storage
url_db = {}

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten")
def shorten_url(original_url: str):
    code = generate_code()
    url_db[code] = original_url
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    if code not in url_db:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url_db[code])