# An API returns nested JSON records, and you need to flatten them into a single-level dict 
# before loading into a table. Write a function flatten(d, sep=".") that turns nested dicts into one level, 
# joining keys with sep.

record = {
    "id": 101,
    "user": {
        "name": "Asha",
        "address": {"city": "Pune", "pin": "411001"},
    },
    "tags": ["a", "b"],
    "meta": {},
    "score": None,
}

{
    "id": 101,
    "user.name": "Asha",
    "user.address.city": "Pune",
    "user.address.pin": "411001",
    "tags": ["a", "b"],
    "score": None,
}

def flatten(record):
    final = {}
    # unsolved !! 
