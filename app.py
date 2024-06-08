from flask import Flask, render_template, jsonify

app = Flask(__name__)

historical_sites = [
    {"id": 1, "lat": 40.7275, "lng": 19.5696, "name": "Butrint National Park", "info": "A national park and an archaeological site in Vlorë County."},
    {"id": 2, "lat": 40.4833, "lng": 19.4747, "name": "Apollonia", "info": "An ancient Greek city in Fier County."},
    {"id": 3, "lat": 41.1533, "lng": 20.3389, "name": "Berat Castle", "info": "A historic castle in Berat."}
]

beaches = [
    {"id": 4, "lat": 40.4462, "lng": 19.4884, "name": "Ksamil Beach", "info": "A popular beach destination in Ksamil."},
    {"id": 5, "lat": 40.1022, "lng": 19.7444, "name": "Dhermi Beach", "info": "A beautiful beach in Dhermi."},
    {"id": 6, "lat": 41.0833, "lng": 20.0167, "name": "Velipoja Beach", "info": "A wide sandy beach in Velipoja."}
]

mountain_routes = [
    {"id": 7, "lat": 42.4666, "lng": 19.5863, "name": "Valbona Valley", "info": "A stunning valley in northern Albania."},
    {"id": 8, "lat": 42.5433, "lng": 19.7355, "name": "Theth National Park", "info": "A national park in the Albanian Alps."},
    {"id": 9, "lat": 40.0431, "lng": 20.0968, "name": "Llogara Pass", "info": "A mountain pass that offers scenic views."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sites/<site_type>')
def get_sites(site_type):
    if site_type == 'historical':
        return jsonify(historical_sites)
    elif site_type == 'beaches':
        return jsonify(beaches)
    elif site_type == 'mountains':
        return jsonify(mountain_routes)
    else:
        return jsonify([])

@app.route('/site/<int:site_id>')
def site_info(site_id):
    all_sites = historical_sites + beaches + mountain_routes
    site = next((s for s in all_sites if s['id'] == site_id), None)
    return render_template('site_info.html', site=site)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
