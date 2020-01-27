sl = (("sketch_2020_01_27a", ".gif"),
      ("sketch_2020_01_26a", ".gif"),
      ("sketch_2020_01_25a", ".gif"),
      ("sketch_2020_01_24a", ".gif"),
      ("sketch_2020_01_23a", ".gif"),
      ("sketch_2020_01_22a", ".gif"),
      ("sketch_2020_01_21a", ".png"),
      ("sketch_2020_01_20a", ".png"),
      ("sketch_2020_01_19a", ".gif"),
      ("sketch_2020_01_18c", ".png"),
      ("sketch_2020_01_17b", ".png"),
      ("sketch_2020_01_16b", ".png"),
      ("sketch_2020_01_15a", ".png"),
      ("sketch_2020_01_14a", ".png"),
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
