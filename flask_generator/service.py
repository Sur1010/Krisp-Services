from flask import request, jsonify
import random


def generate_recommendation():
    data = request.json
    model_name = data.get('model_name')
    viewer_id = data.get('viewer_id')

    random_number = random.randint(1, 100)

    response = {
        'reason': model_name,
        'result': random_number
    }

    return jsonify(response)
