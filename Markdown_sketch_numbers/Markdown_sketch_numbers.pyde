sl = (
    ("sketch_2020_02_23a", ".png"),
    ("sketch_2020_02_22a", ".png"),
    ("sketch_2020_02_21a", ".png"),
    ("sketch_2020_02_20a", ".png"),
    ("sketch_2020_02_19a", ".png"),
    ("sketch_2020_02_18a", ".png"),
    ("sketch_2020_02_17b", ".png"),
    ("sketch_2020_02_16b", ".png"),
    ("sketch_2020_02_15a", ".png"),
    ("sketch_2020_02_14a", ".png"),
    ("sketch_2020_02_13a", ".png"),
    ("sketch_2020_02_12a", ".png"),
    ("sketch_2020_02_11a", ".png"),
    ("sketch_2020_02_10a", ".png"),
    ("sketch_2020_02_09a", ".png"),
    ("sketch_2020_02_08a", ".png"),
    ("sketch_2020_02_07a", ".png"),
    ("sketch_2020_02_06a", ".png"),
    ("sketch_2020_02_05b", ".png"),
    ("sketch_2020_02_04c", ".png"),
    ("sketch_2020_02_03a", ".png"),
    ("sketch_2020_02_02a", ".png"),
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
