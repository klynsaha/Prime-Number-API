from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Optional
import math

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse('/docs')


@app.get("/prime/{number}")
def prime(number: int):
    response = {
        "Number": number,
        "Prime": is_prime(number)
    }
    return response


@app.get("/prime/{start_no}/{end_no}/")
def is_prime(start_no: int, end_no: int, show: bool = False):
    response = {
        "Start": start_no,
        "End": end_no,
    }
    r = get_primes(start_no, end_no)
    if show:
        response.update(r)
    else:
        response["Prime Count"] = r["Prime Count"]
    return response


def is_prime(number: int):
    if(number <= 1):
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i == 0):
            return False
    return True


def get_primes(start_no: int, end_no: int):
    primes = []
    start_no = 2 if start_no < 1 else start_no
    for i in range(start_no, end_no+1):
        if(is_prime(i)):
            primes.append(i)
    return {"Prime Count": len(primes), "Primes": primes}
