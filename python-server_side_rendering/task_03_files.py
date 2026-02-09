#!/usr/bin/env python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
Route /products with source (json|csv) and optional id query params.
"""

import csv
import json
import os

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
    - source: 'json' or 'csv' (required). Else show 'Wrong source'.
    - id: optional. Filter by product id. If not found, show 'Product not found'.
    """
    source = request.args.get("source", "").strip().lower()
    product_id = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template(
            "product_display.html",
            error="Wrong source",
        )

    if source == "json":
        products_list = load_products_json()
    else:
        products_list = load_products_csv()

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
