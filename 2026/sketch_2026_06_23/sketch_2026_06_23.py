# py5 module mode, learn more at <py5coding.org>
# check https:#py5coding.org/how_tos/use_processing_libraries.html

"""ported from a Processing Sound library example
/**
 * Grab audio from the microphone snd_input and draw a circle whose size
 * is determined by how loud the audio snd_input is.
 */
"""

import py5

from processing.sound import AudioIn, Amplitude

def setup():
    global snd_input, loudness
    py5.size(640, 360)
    py5.background(255)
    this = py5.get_current_sketch()
    # Create an Audio snd_input and grab the 1st channel
    snd_input = AudioIn(this, 0)
    # Begin capturing the audio snd_input
    snd_input.start()
    # start() activates audio capture so that you can use it as
    # the snd_input to live sound analysis, but it does NOT cause the
    # captured audio to be played back to you. if you also want the
    # microphone snd_input to be played back to you, call
    #    snd_input.play()
    # instead (be careful with your speaker volume, you might produce
    # painful audio feedback. best to first try it out wearing headphones!)
    # Create a new Amplitude analyzer
    loudness = Amplitude(this)
    # Patch the snd_input to the volume analyzer
    loudness.input(snd_input)


def draw():
    # Adjust the volume of the audio snd_input based on mouse position
    snd_input_level = py5.remap(py5.mouse_y, 0, py5.height, 1.0, 0.0)
    snd_input.amp(snd_input_level)

    # loudness.analyze() return a value between 0 and 1. To adjust
    # the scaling and mapping of an ellipse we scale from 0 to 0.5
    volume = loudness.analyze()
    d = int(py5.remap(volume, 0, 0.5, 1, 350))

    py5.background(125, 255, 125)
    py5.no_stroke()
    py5.fill(255, 0, 150)
    # We draw a circle whose size is coupled to the audio analysis
    py5.circle(py5.width / 2, py5.height / 2, d)

py5.run_sketch(block=False)
