import random

def fibo(n):
    n = int(n)
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n-1)+ fibo(n-2)

def fib(n):
    return str(fibo(n))

def sayHello(name):
    return "Hello " + name + "!"


def firstLast(first, last):
    return first + " " + last

def prequel():
    quotes = [
        "Don’t try it, Anakin. I have the high ground!", 
        "There’s always a bigger fish.", 
        "I don’t like sand. It’s coarse and rough and irritating and it gets everywhere.", 
        "I’ve been wondering… what are midi-chlorians?", 
        "I have the POWER! UNLIMITED… POWER!",
        "I’ll try spinning. That’s a good trick. Whoa-ah!"]
    return random.choice(quotes)

print(fib(10))