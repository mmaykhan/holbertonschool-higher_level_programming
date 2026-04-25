import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except Exception:
        pass
    return products

def read_sql(p_id=None):
    products = []
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if p_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (p_id,))
        else:
            cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error:
        pass
    return products

@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql(product_id)
        if product_id and not products:
            error = "Product not found"
    else:
        error = "Wrong source"

    if not error and product_id and source in ["json", "csv"]:
        products = [p for p in products if str(p["id"]) == product_id]
        if not products:
            error = "Product not found"

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
