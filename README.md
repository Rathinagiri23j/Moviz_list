# Moviz List:

#### Video Demo:  <URL HERE>

#### Description:

Moviz List is a personal project that I built to create a simple yet functional movie watchlist application.
The idea is straightforward: users can log in, search for movies using the IMDB API, and add them to their personal watchlists categorized under "To Watch", "Watching", or "Watched".
I wanted something lightweight, easy to maintain, but still structured enough to feel like a real product.
Thus, Moviz List was born.

Why Flask and Jinja?
I chose Flask because it’s lightweight, beginner-friendly, and doesn't come with a lot of baggage compared to full-fledged frameworks like Django.
For this project, I didn’t need an admin dashboard, ORM-heavy models, or massive built-in features. I needed speed, flexibility, and simplicity — exactly what Flask provides.

For the frontend, I went with Jinja2 templating.
Since Flask integrates Jinja natively, it made sense to use it.
Also, Jinja allows embedding Python-like expressions directly into HTML, which makes rendering dynamic data (like search results or user-specific watchlists) super intuitive and clean.

File Structure Breakdown
Here’s what each file and folder does:

app.py
This is the main driver of the application.
It handles the routing (login, register, search, adding movies, displaying the watchlist), connects the pieces together, and initiates the Flask app.

config.py
Basic configuration for the app goes here.
For now, it mostly handles setup tasks like setting secret keys, API keys (IMDB API), and other environment-related constants.

helpers.py
This file contains small utility functions.
Example: making a request to the IMDB API to fetch movie details, formatting results if needed, and possibly some session management shortcuts.

models.py
It handles the data models.
Since this project is relatively small, I didn’t go full ORM.
Instead, this file might hold basic structures like how a movie or a watchlist entry is modeled inside the app.

Templates Folder (Frontend Views)
This is where all the Jinja HTML templates are:

layout.html: The base layout that other pages extend.
It holds common things like the header, footer, basic structure, and includes stylesheets.

index.html: The homepage where users are greeted.
If logged in, it might show quick actions like "Search for a Movie" or "View your Watchlist".

login.html: The login page.
Handles user authentication input.

register.html: The signup page for new users.
Just a simple form asking for username, password, and password confirmation.

add.html: Page for adding a movie to a particular watchlist category after searching.

apology.html: A small but important page.
It displays user-friendly error messages only on login this is the trial one.

Static Folder
This contains all static resources like CSS, images, etc.

styles.css: Custom styling for the app.
Since I didn’t want to overcomplicate it with Bootstrap or Tailwind, I wrote minimal CSS myself to keep the UI clean, simple, and readable.

Images:

courage.png, movie.webp, New_Courage.webp — are decorative images used across the site, mainly for making the homepage or error pages look friendlier and less empty this is the trial one.

Environment and External Files
.env:
Holds sensitive environment variables, mainly the IMDB API Key, Flask secret key, and possibly database URIs if expanded later.

.gitignore:
Tells Git what files/folders to ignore (like the .env, __pycache__, and .venv folders).

requirements.txt:
List of Python dependencies (Flask, requests, etc.).
Anyone who wants to run the project just needs to install these via pip install -r requirements.txt.

Design Choices and Thoughts
When designing Moviz List, I consciously decided to:

Keep user flow simple (login -> search -> add movie)

Not over-engineer (no unnecessary backend complexity)

Keep templates minimalistic but structured

Avoid JavaScript unless absolutely needed (not needed for MVP)

Stick to server-side rendering (Jinja) rather than making it a full SPA (Single Page Application)

I debated at first whether I should use a lightweight database like SQLite or just use session storage for user data.
For now, since this project is personal and not production-level, session storage is enough.
If I decide to expand it later (multi-user support, persistent user data), I’ll add a proper database layer.

Future Improvements
Add persistent database support (SQLite/PostgreSQL)

Better authentication (hashed passwords, Flask-Login integration)

Add a "recommendations" feature based on watch history

Responsive mobile-first design improvements

Allow users to rate/review movies within their watchlist

Final Thoughts
Moviz List is simple but full of love.
It’s built with the idea that small projects can teach a lot, and good structure from the beginning makes scaling easier later.
Flask and Jinja were perfect choices for getting something solid off the ground without feeling overwhelming.

If you find this project interesting or useful, feel free to fork it, play around with it, and make your own awesome version!




--------------------
setup:
1. clone the repo
2. installing dependencies >> pip install -r requirements.txt
3. setting api key for imdb 
4. setting secret key
5. flask run
