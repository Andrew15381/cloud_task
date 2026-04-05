import os
import redis
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='.')

redis_host = 'redis-service'
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/', methods=['POST', 'GET'])
def index():
    message = None
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key and value:
            r.set(key, value)
            message = f'Записано: {key} = {value}'
        else:
            message = 'Оба поля обязательны'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
