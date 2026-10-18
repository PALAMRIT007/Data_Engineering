# Write a function error_summary(lines) that returns a dict mapping each service to the count of 
# lines where level == "ERROR". Services with zero errors should still appear with a count of 0.


lines = [
    "2026-03-01T10:00:01 | ingest  | INFO  | batch started",
    "2026-03-01T10:00:05 | ingest  | ERROR | schema mismatch",
    "2026-03-01T10:01:00 | loader  | ERROR | timeout",
    "2026-03-01T10:01:30 | loader  | ERROR | timeout",
    "2026-03-01T10:02:00 | api     | INFO  | request ok",
    "malformed line without separators",
    "",
]


# output: {"ingest": 1, "loader": 2, "api": 0}

def error_summary(lines):
    final = {}
    for line in lines:
        temp = line.split("|")
        if len(temp)>=4:
            if temp[1].strip() not in final and temp[2].strip() == "ERROR":
                final[temp[1].strip()] = 1
            elif temp[1].strip() not in final and temp[2].strip() != "ERROR":
                final[temp[1].strip()] = 0
            else:
                if temp[2].strip() == "ERROR":
                    final[temp[1].strip()] = final.get(temp[1].strip(),0)+1

    return final



# more readible format

def error_summary(lines):
    final = {}
    for line in lines:
        temp = line.split("|", 3)
        if len(temp) < 4:
            continue
        service = temp[1].strip()
        final.setdefault(service, 0)            #agar service hai to leave, nahi hai to add service as key and set value as defualt(0)
        if temp[2].strip() == "ERROR":
            final[service] += 1
    return final


# dict.setdefault(key, default) does two things in one call:

# If key is already in the dict, it leaves it alone and returns the existing value.
# If key is not in the dict, it inserts key with the value default and returns default.
                