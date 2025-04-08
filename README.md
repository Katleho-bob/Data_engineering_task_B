# Data_engineering_task_B
---

# Timestamp Difference API

This is a simple Flask-based REST API that calculates the absolute time difference between two timestamps in seconds. The API accepts a POST request with multiple test cases and returns the calculated differences for each pair of timestamps.

## Features

- Accepts multiple test cases in a single request
- Returns the absolute difference between pairs of timestamps in seconds
- Responds with error messages for invalid inputs

## Requirements

- Python 3.x
- Flask

## Installation

1. Ensure that Python 3.x is installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install Flask
   ```

3. Clone or download this repository to your local machine.

## Usage

1. Start the Flask server by running the following command:
   ```bash
   python app.py
   ```

2. The application will be hosted at `http://localhost:5000`.

### API Endpoint

- **POST /timestamp-diff**

    Accepts a JSON request body with multiple timestamp pairs, where each pair contains two timestamps. It will return a JSON response with the absolute differences in seconds for each pair.

    **Request Example** (raw POST request body):
    ```txt
    2
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    ```

    **Response Example**:
    ```json
    [25200, 88200]
    ```

    **Error Responses**:
    - If the input is empty:
      ```json
      { "error": "Input is empty" }
      ```
    - If there is a malformed request:
      ```json
      { "error": "Invalid input format" }
      ```
---

##  Testing Locally with Postman

1. Open Postman
2. Choose `POST` method and enter URL: `http://127.0.0.1:5000/timestamp-diff`
3. Go to **Body** → select `raw` → choose `Text`
4. Paste the same timestamp sample as above
5. Click **Send** to see the JSON result

```
## Functions

- **`parse_datetime(dt_str)`**: Parses the input timestamp string into a `datetime` object using the format `"%a %d %b %Y %H:%M:%S %z"`.
  
- **`calculate_difference(t1, t2)`**: Calculates the absolute difference between two timestamps in seconds.

## Example

### Request

POST to `http://127.0.0.1:5000/timestamp-diff` with the following body:

```txt
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

### Response

```json
[25200, 88200]
```

