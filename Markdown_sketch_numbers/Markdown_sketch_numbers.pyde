sl = (
    "sketch_191111c",
    "sketch_191112c",
    "sketch_191113a",
    "sketch_191114b",
    "sketch_191115a",
)
OUTPUT = ".png"
for s in sl:
    SKETCH_NAME = s
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
