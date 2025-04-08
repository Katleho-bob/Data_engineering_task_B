from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%a %d %b %Y %H:%M:%S %z")

def calculate_difference(t1, t2):
    dt1 = parse_datetime(t1)
    dt2 = parse_datetime(t2)
    return str(abs(int((dt1 - dt2).total_seconds())))

@app.route('/timestamp-diff', methods=['POST'])
def timestamp_diff():
    data = request.get_data(as_text=True)
    lines = data.strip().splitlines()
    
    if not lines:
        return jsonify({"error": "Input is empty"}), 400

    try:
        T = int(lines[0])
        results = []
        for i in range(T):
            t1 = lines[1 + i * 2].strip()
            t2 = lines[2 + i * 2].strip()
            results.append(calculate_difference(t1, t2))
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
