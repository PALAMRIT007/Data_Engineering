# ============================================================
# PYTHON DECORATORS - REVISION NOTES
# ============================================================

# WHAT:
# A function that takes another function, adds extra behavior around it,
# and returns the modified function, WITHOUT changing the original code.
# `@decorator` is just shorthand for: func = decorator(func)

# EXAMPLE:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()
# before
# hello
# after
# (@my_decorator == say_hello = my_decorator(say_hello))

# PRACTICAL EXAMPLE (timing):
import time
from functools import wraps

def timer(func):
    @wraps(func)  # keeps original function name and docstring
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def load_data():
    time.sleep(1)

# WHY USE:
# - Add logging, timing, retry, caching, authentication without
#   touching the function body
# - Reusable across many functions
# - Data engineering use: retry failed API/DB calls, time a pipeline
#   step, log job runs

# BUILT-IN DECORATORS:
# @staticmethod, @classmethod, @property, functools.lru_cache

# INTERVIEW ONE-LINER:
# "A decorator is a higher-order function that wraps another function
#  to extend its behavior without modifying its code."