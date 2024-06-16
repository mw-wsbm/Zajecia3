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



