# Prime Number API

This API is made using [FastAPI](https://fastapi.tiangolo.com) in Python.

### How to start local server
```python
1. pip install -r requirements.txt
2. unicorn main:app --reload
```

### Usage
1. `/prime/<num>` : *num* is prime or not
- Request: `/prime/101`
- Response:
```json
{
  "Number": 101,
  "Prime": true
}
```

2. `/prime/<num1>/<num2>` : Get all primes between *num1* and *num2*, both numbers included
- Request: `/prime/101/119`
- Response:
```json
{
  "Start": 101,
  "End": 119,
  "Prime Count": 5,
  "Primes": [
    101,
    103,
    107,
    109,
    113
  ]
} 
```

3. `/prime/<num1>/<num2>/false` : Get prime numbers count between *num1* and *num2*, both numbers included
- Request: `/prime/101/119/false`
- Response: 
```json
{
  "Start": 101,
  "End": 119,
  "Prime Count": 5
}
```

4. `/docs` : Get API Docs `FastAPI - Swagger UI`
<img src="https://user-images.githubusercontent.com/30416024/107880540-6aaa5700-6f05-11eb-8ae3-cccbd19e9376.png" width="742" /> 
