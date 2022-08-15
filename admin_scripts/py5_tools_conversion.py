import py5_tools

pp2i = py5_tools.translators.processingpy2imported

#source_dir = '/home/villares/GitHub/processing-python/'
#target_dir = '/home/villares/GitHub/processing-python/'
source_dir = '/home/villares/GitHub/py.processing-play/'
target_dir = '/home/villares/GitHub/processing-python/play/'
result = pp2i.translate_dir(source_dir, target_dir, ext='.py')
print(result) 

# Material aulas
#source_dir = '/home/villares/GitHub/material-aulas/Processing-Python'
#target_dir = '/home/villares/GitHub/material-aulas/Processing-Python-py5'
# Rosetta examples repo
#source_dir = '/home/villares/GitHub/rosetta_examples_p5/examples/Python/'
#target_dir = '/home/villares/GitHub/rosetta_examples_p5/examples/py5/'
# Python mode examples
#source_dir = '/home/villares/sketchbook/modes/PythonMode/examples/'
#target_dir = '/home/villares/GitHub/py5examples/examples-from-Processing-Python-mode/'

# source = """
# def setup():
#     size(400, 400)
#     
# def draw():
#     noStroke()
#     rect(200, 200, 100, 100)
#     m = MyClass()
# 
# class MyClass:
#     pass
# 
# """
# result = pp2i.translate_code(1)
# print(result)
