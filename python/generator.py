# ============================================================
# PYTHON GENERATORS - REVISION NOTES
# ============================================================

# WHAT:
# A function that uses `yield` instead of `return`.
# It produces values ONE AT A TIME (lazily) and pauses after each yield,
# resuming from the same point on the next call.

# EXAMPLE:
def read_numbers(n):
    for i in range(n):
        yield i * 2

gen = read_numbers(3)
print(next(gen))  # 0
print(next(gen))  # 2
print(next(gen))  # 4
# next(gen)       # raises StopIteration (generator exhausted)

# GENERATOR EXPRESSION (round brackets, not square):
gen_exp = (x * 2 for x in range(1000000))

# WHY USE:
# - Memory efficient: holds one item at a time, not the full result
# - Lazy evaluation: computes values only when requested
# - Data engineering use: read big files line by line, stream Kafka/API
#   records, chunked processing

# GENERATOR vs LIST:
# | Feature  | List             | Generator          |
# | Memory   | Stores all items | One item at a time |
# | Reuse    | Many iterations  | ONE pass only      |
# | Indexing | lst[0] works     | Not supported      |

# INTERVIEW ONE-LINER:
# "A generator is a function using `yield` that returns an iterator
#  and produces values lazily, so it saves memory on large datasets."