#!/usr/bin/env python3
"""
Task 02: Creating a Dynamic Template with Loops and Conditions in Flask
Flask app with Jinja loops/conditions; reads items from JSON.
"""

import json
import os

from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Read items list from items.json."""
    path = os.path.join(os.path.dirname(__file__), "items.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


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


@app.route("/items")
def items():
    """Items page: render items.html with list from items.json."""
    items_list = load_items()
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
