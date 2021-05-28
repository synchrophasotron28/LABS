import json
from flask import Flask
import math
# h_a = 1740
# h_p = 350

# Новые данные для моделирования возмущения от луны
h_a = 170_000
h_p = 130_000

# h_a = h_p = 1400
OMEGA = math.radians(10)
U = math.radians(7)
Sa = 23
m = 1700
C_xa = 3.5
Fa = 125

flying_objects = {
	'object1':
	{
		'x': 0,
		'y': 0,
		'z': 0,
		'h_a': 1740,
		'h_p': 350,
		'OMEGA': math.radians(10),
		'U': math.radians(7),
		'm': 1700,
		'i': math.radians(20.8)
	}
}


app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps(flying_objects)

if __name__ == "__main__":
    app.run()
