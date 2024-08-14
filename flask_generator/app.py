from flask import Flask
from service import generate_recommendation

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    return generate_recommendation()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
