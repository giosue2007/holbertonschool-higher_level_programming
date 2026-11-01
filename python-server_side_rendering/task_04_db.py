#!/usr/bin/python3
"""Flask application that displays products from JSON, CSV or SQLite."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read the products from a JSON file and return them as a list."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename):
    """Read the products from a CSV file and return them as a list."""
    products = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename):
    """Read the products from a SQLite database and return them as a list."""
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
    finally:
        connection.close()

    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/products')
def products():
    """Display the products from the source chosen in the URL."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql('products.db')
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error='Database error')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        found = []
        for product in data:
            if str(product['id']) == product_id:
                found.append(product)
        if len(found) == 0:
            return render_template('product_display.html',
                                   error='Product not found')
        data = found

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
