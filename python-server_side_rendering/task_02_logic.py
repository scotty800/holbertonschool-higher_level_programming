from flask import Flask, render_template
import json

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
    # Read and parse the JSON data from items.json
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items = data.get('items', [])
    except Exception as e:
        print(f"Error reading items.json: {e}")
        items = []

    # Pass the items list to the template
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)