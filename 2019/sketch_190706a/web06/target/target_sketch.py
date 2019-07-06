import web06 as source_sketch
from pyp5js import *

event_functions = {
    "deviceMoved": source_sketch.deviceMoved,
    "deviceTurned": source_sketch.deviceTurned,
    "deviceShaken": source_sketch.deviceShaken,
    "keyPressed": source_sketch.keyPressed,
    "keyReleased": source_sketch.keyReleased,
    "keyTyped": source_sketch.keyTyped,
    "mouseMoved": source_sketch.mouseMoved,
    "mouseDragged": source_sketch.mouseDragged,
    "mousePressed": source_sketch.mousePressed,
    "mouseReleased": source_sketch.mouseReleased,
    "mouseClicked": source_sketch.mouseClicked,
    "doubleClicked": source_sketch.doubleClicked,
    "mouseWheel": source_sketch.mouseWheel,
    "touchStarted": source_sketch.touchStarted,
    "touchMoved": source_sketch.touchMoved,
    "touchEnded": source_sketch.touchEnded,
    "windowResized": source_sketch.windowResized,
}

start_p5(source_sketch.setup, source_sketch.draw, event_functions)