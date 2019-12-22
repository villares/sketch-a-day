sl = (
    "sketch_191222a",
    "sketch_191221a",
    "sketch_191220a",
    "sketch_191219a",
    "sketch_191218a",
    "sketch_191217a",
    "sketch_191216a",
    "sketch_191215b",
    "sketch_191214b",
    "sketch_191213b", 
    "sketch_191212b",
    "sketch_191211d",
    "sketch_191210a",
    "sketch_191209a",



)
OUTPUT = ".png"
for s in sl:
    SKETCH_NAME = s
    println(
        """
---

![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
