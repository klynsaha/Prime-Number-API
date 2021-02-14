# Prime Number API

This API is made using [FastAPI](https://fastapi.tiangolo.com) in Python.

### Usage
1. A *num* is prime or not
```
/prime/<num>
```
**Example**: <br />
Request: /prime/101 <br />
Response:
{
  "Number": 101,
  "Prime": true
} <br />

2. Get all primes between *num1* and *num2*, both numbers included
```
/prime/<num1>/<num2>
```
**Example**: <br />
Request: /prime/101/119 <br />
Response:
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
} <br />

3. Get prime numbers count between *num1* and *num2*, both numbers included
```
/prime/<num1>/<num2>/false
```
**Example**: <br />
Request: /prime/101/119/false <br />
Response: 
{
  "Start": 101,
  "End": 119,
  "Prime Count": 5
}

