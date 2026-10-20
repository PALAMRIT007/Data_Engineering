data = [("A", "M", 1),
    ("A", "N", 2),
    ("A", "J", 3),
    ("B", "M", 4),
    ("B", "N", 5),
    ("B", "J", 6),
    ("C", "M", 7),
    ("C", "N", 8),
    ("C", "J", 9)
]


output:

+-----+----+---+---+

|col1|  M|  N|  J|

+-----+----+---+---+

|     A|  1|  2|  3|

|     B|  4|  5|  6|

|     C|  7|  8|  9|

+----+---+---+---+

# spark code
df = spark.createDataFrame(data, ["col1","col2","val"])

result = df.groupBy("col1")
            .pivot("col2", ["M","N","J"])
            .agg(F.first("val"))

result.show()

