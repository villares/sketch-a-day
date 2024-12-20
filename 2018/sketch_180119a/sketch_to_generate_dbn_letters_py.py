"""
s18019 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

This script generates code on console for dbn_letters.py

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""
 

def setup():
    noLoop()
    println('''"""
s18019 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

This code was generated by sketch_to_generate_dbn_letters_py.py

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing        
"""''')
    println("dbn_letter = {}  # Dict of functions")
    println("")
    convert_dbn_source("data/dbnletters.dbn")

def convert_dbn_source(file_path):
    with open(file_path, "r") as f:
        dbn_source = f.readlines()
    inside_block = False
    command_name = ""
    command_block = []
    for ln in dbn_source:
        if ln.count("command"):
            command_name = ln[14:15]
        elif ln.count("{"):
            inside_block = True
        elif ln.count("}"):
            if command_name in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                def_dbn_letter(command_block, command_name)
            command_block = []  # empty block
            inside_block = False
        elif inside_block:
            command_block.append(ln.lstrip())


def def_dbn_letter(dbn_block, func_key):
    p_block = []
    println("# " + func_key)
    println("def dbn_letter" + func_key + "(h, v):")
    println("    pushMatrix()")
    println("    scale(1, -1)")
    for dbn_line in dbn_block:
        if dbn_line:
            p_block.append("    " + dbn_line
                           .replace("line ", "line(")
                           .replace(" ", ",")
                           .replace("//", "#")
                           .strip()
                           + ")")
    for py_processing_line in p_block:
            println(py_processing_line)
    println("    popMatrix()")
    println("dbn_letter['"+ func_key +"'] = dbn_letter" + func_key)
    println("dbn_letter["+ str(ord(func_key)-64) +"] = dbn_letter" + func_key)
    println("")
