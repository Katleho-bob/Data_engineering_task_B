# ⏱️ Timestamp Difference Service (Task B)

This service calculates the **absolute difference in seconds** between two timestamps (with timezones) based on social media-style post visibility. You can POST multiple test cases as plain text, and receive the differences in a JSON array.

---

## 📦 Requirements

Ensure the following tools are installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) [Postman](https://www.postman.com/) or `curl` for testing

---

## 🧰 Setup Instructions

1. **Clone or download** this repository.

2. Navigate to the project folder:
   ```bash
   cd path/to/your/project
   ```

3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the App

Start the Flask service:

```bash
python app.py
```

The app will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📮 How to Use the API

### Endpoint

```
POST /timestamp-diff
Content-Type: text/plain
Body: Plain text input with timestamps (same format as sample input)
```

### Sample Input

```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

### Sample cURL Command

```bash
curl -X POST http://127.0.0.1:5000/timestamp-diff \
     -H "Content-Type: text/plain" \
     --data-binary @"sample_input.txt"
```

Or directly inline:
```bash
curl -X POST http://127.0.0.1:5000/timestamp-diff \
     -H "Content-Type: text/plain" \
     --data-binary "2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"
```

### Sample Response

```json
["25200", "88200"]
```

---

## 🧪 Testing Locally with Postman

1. Open Postman
2. Choose `POST` method and enter URL: `http://127.0.0.1:5000/timestamp-diff`
3. Go to **Body** → select `raw` → choose `Text`
4. Paste the same timestamp sample as above
5. Click **Send** to see the JSON result

---

## 🔧 Folder Structure

```
timestamp_service/
│
├── app.py                 # Flask app
├── requirements.txt       # Python dependencies
└── README.md              # Setup & usage guide
```
