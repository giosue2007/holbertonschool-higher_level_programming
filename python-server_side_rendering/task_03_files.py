import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r", encoding="utf-8") as f:
        da_data = json.load(f)
    return render_template('items.html', items=da_data.get("items", []))

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return "Wrong source"
    
    if source == 'json':
        with open("products.json", "r", encoding="utf-8") as f:
            products_list = json.load(f)
    else:
        with open("products.csv", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products_list = [
                {**row, 'id': int(row['id']), 'price': float(row['price'])}
                for row in reader
            ]

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return "Invalid product ID"
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return "Product not found"

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
