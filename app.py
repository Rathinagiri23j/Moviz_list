from flask import Flask, render_template, redirect, request, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from helpers import login_required, lookup_movie, apology
from models import db, User, Movie
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    movies = Movie.query.filter_by(user_id=session["user_id"]).all()
    return render_template("index.html", movies=movies)


@app.route("/update_movie", methods=["POST"])
def update_movie():
    movie_id = request.form.get("movie_id")
    status = request.form.get("status")
    review = request.form.get("review")

    movie = Movie.query.get(movie_id)
    if movie and movie.user_id == session["user_id"]:
        movie.status = status
        movie.review = review
        db.session.commit()
        flash("Movie updated successfully!", "success")
    return redirect(url_for("index"))


@app.route("/delete_movie/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie and movie.user_id == session["user_id"]:
        db.session.delete(movie)
        db.session.commit()
        flash("Movie deleted from watchlist.", "info")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cnf_password = request.form.get("confirmation")
        if not username or not password:
            flash("Must provide username and password")
            return redirect("/register")
        if password != cnf_password:
            flash("password and confirm password mismatch!")
        hash_pw = generate_password_hash(password)
        user = User(username=username, hash=hash_pw)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            flash("Username already exists")
            return redirect("/register")
        session["user_id"] = user.id
        return redirect("/")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user and check_password_hash(user.hash, request.form.get("password")):
            session["user_id"] = user.id
            return redirect("/")
        else:
            return apology("Invalid username or password", code=400)
    return render_template(f"login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        search_title = request.form.get("search")
        if not search_title:
            flash("Please enter a movie title to search.")
            return redirect("/add")

        movies = lookup_movie(search_title)
        if not movies:
            flash("No results found.")
            return render_template("add.html", movies=None)

        return render_template("add.html", movies=movies)

    return render_template("add.html", movies=None)


@app.route("/add_show", methods=["POST"])
@login_required
def add_show():
    if request.method == "POST":
        title = request.form.get("title")
        poster = request.form.get("poster")
        category = request.form.get("type")
        status = request.form.get("status")
        review = request.form.get("review")

        movie = Movie(
            user_id=session["user_id"],
            title=title,
            poster=poster,
            category=category,
            status=status,
            review=review,

        )
        db.session.add(movie)
        db.session.commit()
        flash(f"{title} added to your watchlist")
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
