#!/usr/bin/env python3
"""
Task 01: Creating a Basic HTML Template in Flask
Flask app with Jinja templates, shared header and footer.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """About page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Contact page."""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
