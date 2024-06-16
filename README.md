# Zajecia3
# zadanie 1
import subprocess
import json


def send_get_request(url):
    result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    return result


def check_response(response, expected_status, required_keys):
    try:
        json_data = json.loads(response.stdout)
    except json.JSONDecodeError:
        return False, "Invalid JSON"

    if response.returncode != 0:
        return False, "Curl command failed"

    if response.stdout == '':
        return False, "Empty response"

    if response.stderr != '':
        return False, "Curl error: " + response.stderr

    try:
        json_data = json.loads(response.stdout)
    except json.JSONDecodeError:
        return False, "Invalid JSON"

    for key in required_keys:
        if key not in json_data:
            return False, f"Missing key: {key}"

    return True, "Passed"


def run_tests():
    tests = [
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "status": 200, "keys": ["userId", "id", "title", "body"]},
        {"url": "https://jsonplaceholder.typicode.com/comments/1", "status": 200, "keys": ["postId", "id", "name", "email", "body"]},
        {"url": "https://jsonplaceholder.typicode.com/albums/1", "status": 200, "keys": ["userId", "id", "title"]}
    ]

    for i, test in enumerate(tests, 1):
        response = send_get_request(test["url"])
        passed, message = check_response(response, test["status"], test["keys"])
        print(f"Test {i}: {'PASSED' if passed else 'FAILED'} - {message}")

if __name__ == "__main__":
    run_tests()



# Struktura skryptu
- `send_get_request(url)`: Wysyła żądanie GET do podanego URL przy użyciu curl.
- `check_response(response, expected_status, required_keys)`: Sprawdza status odpowiedzi i obecność kluczowych elementów.
- `run_tests()`: Wysyła żądania do kilku endpointów i sprawdza odpowiedzi.

## Testowane endpointy
1. `https://jsonplaceholder.typicode.com/posts/1`
2. `https://jsonplaceholder.typicode.com/comments/1`
3. `https://jsonplaceholder.typicode.com/albums/1`



#Zadanie 2

#aplikacja

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#testy 
import unittest
from app.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()

# plik Makefile

.PHONY: install test run

install:
    pip install -r requirements.txt

test:
    python -m unittest discover -s tests

run:
    python -c "from app.calculator import add, subtract, multiply, divide; print('Add: ', add(1, 2)); print('Subtract: ', subtract(5, 3)); print('Multiply: ', multiply(4, 2)); print('Divide: ', divide(8, 2))"

# testowanie

w celu przetestowania Makefile trzeba użyc reguł make install make test i make run

