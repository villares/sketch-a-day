sl = (
    "sketch_191204a",
    "sketch_191203a",
    "sketch_191202a",
    "sketch_191201a",
)
OUTPUT = ".gif"
for s in sl:
    SKETCH_NAME = s
    println(
        """
---

![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
