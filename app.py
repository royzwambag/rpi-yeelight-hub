from yeelight import discover_bulbs, Bulb
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    bulbs = discover_bulbs()
    bulbs = sorted(bulbs, key=lambda k: k["ip"])
    return render_template('index.html', bulbs=bulbs)


@app.route('/toggle')
def toggle():
    bulb_ip = request.args.get('bulb_ip')
    bulb = Bulb(bulb_ip)
    if bulb:
        bulb.toggle()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
