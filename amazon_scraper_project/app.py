from flask import Flask, render_template, request, jsonify
from scrape import scrape_amazon_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    title, price, discount, mrp = scrape_amazon_data(url)
    if title and price and discount:
        return jsonify({'success': True, 'title': title, 'price': price, 'discount': discount, 'mrp': mrp})
    else:
        return jsonify({'success': False})

if __name__ == "__main__":
    app.run(debug=True)
