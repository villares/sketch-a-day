"""
Clock
https://rosettacode.org/wiki/Draw_a_clock#Processing
Processing 3.4
2019-12-19 Jeremy Douglass
2020-03-15 Alexandre Villares (Python Mode)

Task: Draw a clock.
"""
# This simple example of an analog wall clock uses the Processing built-in
# time functions second(), minute(), and hour(). For each hand it rotates the
# sketch canvas and then draws a straight line.

last_sec = second()

def draw():
    global last_sec
    if last_sec != second():
        drawClock()
        last_sec = second()

def drawClock():
    background(192)
    translate(width / 2, height / 2)
    s = second() * TWO_PI / 60.0
    m = minute() * TWO_PI / 60.0
    h = hour() * TWO_PI / 12.0
    rotate(s)
    strokeWeight(1)
    line(0, 0, 0, -width * 0.5)
    rotate(-s + m)
    strokeWeight(2)
    line(0, 0, 0, -width * 0.4)
    rotate(-m + h)
    strokeWeight(4)
    line(0, 0, 0, -width * 0.2)

# One of the official Processing language examples is a more graphically
# detailed Clock example: https://processing.org/examples/clock.html
