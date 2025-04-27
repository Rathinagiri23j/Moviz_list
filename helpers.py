import requests
from flask import session, redirect, render_template
from functools import wraps
from config import Config


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup_movie(search):
    api_key = Config.OMDB_API_KEY
    response = requests.get(f"http://www.omdbapi.com/?s={search}&apikey={api_key}")
    data = response.json()

    if data.get("Response") == "True":
        results = []

        for item in data["Search"]:
            print(item)
            results.append({
                "title": item["Title"],
                "poster": item["Poster"],
                "type": item["Type"],
            })
        return results
    return None


def apology(message, code=400):
    return render_template("apology.html", top=code, bottom=message), code
