# Zajecia3 zadanie 1

# Struktura skryptu
- `send_get_request(url)`: Wysyła żądanie GET do podanego URL przy użyciu curl.
- `check_response(response, expected_status, required_keys)`: Sprawdza status odpowiedzi i obecność kluczowych elementów.
- `run_tests()`: Wysyła żądania do kilku endpointów i sprawdza odpowiedzi.

## Testowane endpointy
1. `https://jsonplaceholder.typicode.com/posts/1`
2. `https://jsonplaceholder.typicode.com/comments/1`
3. `https://jsonplaceholder.typicode.com/albums/1`
