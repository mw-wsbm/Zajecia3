.PHONY: install test run

install:
    pip install -r requirements.txt

test:
    python -m unittest discover -s tests

run:
    python -c "from app.calculator import add, subtract, multiply, divide; print('Add: ', add(1, 2)); print('Subtract: ', subtract(5, 3)); print('Multiply: ', multiply(4, 2)); print('Divide: ', divide(8, 2))"
