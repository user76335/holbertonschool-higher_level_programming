#!/usr/bin/env python3
"""
Flask application for server-side rendering.
Serves pages with data from items.json, products.csv, and SQLite.
"""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def get_items():
    """Load items from items.json."""
    json_path = os.path.join(os.path.dirname(__file__), "items.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_products():
    """Load products from SQLite (products.db) or fallback to products.csv."""
    db_path = os.path.join(os.path.dirname(__file__), "products.db")
    csv_path = os.path.join(os.path.dirname(__file__), "products.csv")

    # Try SQLite first
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT name, category, price FROM Products")
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except sqlite3.Error:
            pass

    # Fallback to CSV
    if os.path.exists(csv_path):
        try:
            products = []
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "name" in row and "category" in row and "price" in row:
                        products.append({
                            "name": row["name"],
                            "category": row["category"],
                            "price": float(row["price"]) if row["price"] else 0,
                        })
            return products
        except (IOError, ValueError):
            pass

    return None


@app.route("/")
def index():
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
    """Items page - data from items.json."""
    items_list = get_items()
    return render_template("items.html", items=items_list)


@app.route("/products")
def products():
    """Products page - data from DB or CSV."""
    products_list = get_products()
    if products_list is None:
        return render_template("product_display.html", error="Could not load products.")
    return render_template("product_display.html", products=products_list)


if __name__ == "__main__":
    app.run(debug=True)
