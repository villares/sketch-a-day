sl = (
    ("sketch_2020_06_18a", ".gif"),
    ("sketch_2020_06_17a", ".png"),
    ("sketch_2020_06_16a", ".gif"),
    ("sketch_2020_06_15a", ".gif"),
 
)
for s, OUTPUT in sl:
    SKETCH_NAME = s
    println(
        """
---

![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
