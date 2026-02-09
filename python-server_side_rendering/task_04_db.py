#!/usr/bin/env python3
"""
Task 04: Extending Dynamic Data Display to Include SQLite in Flask
Route /products with source (json | csv | sql) and optional id.
"""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_products_json():
    """Read and parse products from products.json."""
    path = os.path.join(BASE_DIR, "products.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return data.get("products", data.get("items", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def load_products_csv():
    """Read and parse products from products.csv."""
    path = os.path.join(BASE_DIR, "products.csv")
    products = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    products.append({
                        "id": int(row.get("id", 0)),
                        "name": row.get("name", ""),
                        "category": row.get("category", ""),
                        "price": float(row.get("price", 0)),
                    })
                except (ValueError, KeyError):
                    continue
    except FileNotFoundError:
        pass
    return products


def load_products_sql():
    """
    Read products from SQLite products.db.
    Returns (list of dicts, None) on success or (None, error_message) on failure.
    """
    path = os.path.join(BASE_DIR, "products.db")
    if not os.path.exists(path):
        return None, "Database error"
    try:
        conn = sqlite3.connect(path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        products = [dict(row) for row in rows]
        return products, None
    except sqlite3.Error:
        return None, "Database error"


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
    """Items page."""
    return render_template("items.html", items=load_items())


def load_items():
    """Load items from items.json."""
    path = os.path.join(BASE_DIR, "items.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.route("/products")
def products():
    """
    Products page. Query params:
    - source: 'json', 'csv', or 'sql'. Else show 'Wrong source'.
    - id: optional. Filter by product id.
    """
    source = request.args.get("source", "").strip().lower()
    product_id = request.args.get("id")

    if source not in ("json", "csv", "sql"):
        return render_template(
            "product_display.html",
            error="Wrong source",
        )

    if source == "json":
        products_list = load_products_json()
    elif source == "csv":
        products_list = load_products_csv()
    else:
        products_list, db_error = load_products_sql()
        if db_error is not None:
            return render_template(
                "product_display.html",
                error=db_error,
            )

    if product_id is not None and product_id != "":
        try:
            pid = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
            )
        filtered = [p for p in products_list if p.get("id") == pid]
        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found",
            )
        products_list = filtered

    return render_template(
        "product_display.html",
        products=products_list,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
