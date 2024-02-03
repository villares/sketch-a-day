# Inspired by talk at:
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361

import py5

# ["name", hint_enabled, hint_disable_constant, hint_enable_constant]
hints=(["DEPTH_TEST", False,
          py5.DISABLE_DEPTH_TEST, py5.ENABLE_DEPTH_TEST],
         ["DEPTH_SORT", False,
          py5.DISABLE_DEPTH_SORT, py5.ENABLE_DEPTH_SORT],
         ["DEPTH_MASK", False,
          py5.DISABLE_DEPTH_MASK, py5.ENABLE_DEPTH_MASK],
         ["OPTIMIZED_STROKE", True,
          py5.DISABLE_OPTIMIZED_STROKE, py5.ENABLE_OPTIMIZED_STROKE],
         ["STROKE_PERSPECTIVE", False,
          py5.DISABLE_STROKE_PERSPECTIVE, py5.ENABLE_STROKE_PERSPECTIVE],
         )
use_sphere = False

def setup():
    py5.size(800, 600, py5.P3D)
    py5.sphere_detail(12)
    py5.text_font(py5.create_font('Inconsolata Bold', 12))
    apply_hints()

def draw():
    py5.window_title('FPS: {}'.format(round(py5.get_frame_rate())))
    py5.background(255)

    py5.fill(0)
    for i, (name, status, _, _) in enumerate(hints):
        py5.text("{} {}".format(name, str(status)), 20, 20 + i * 20)
    py5.text("<- use the mouse to toggle settings", 200, 40)
    py5.text("click here to toggle shape (box / sphere)", 300, 580)

    py5.fill(255, 40, 20, 100)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.frame_count * 0.005)
    for x in range(-200, 201, 200):
        for y in range(-200, 201, 200):
            with py5.push_matrix():
                py5.translate(x, 0, y)
                if use_sphere:
                    py5.sphere(90)
                else:
                    py5.box(180)

def mouse_pressed():
    global use_sphere
    if py5.mouse_y > py5.height - 100:
        use_sphere = not use_sphere

    id = py5.mouse_y // 20
    if id < len(hints):
        hints[id][1] = not hints[id][1]

    apply_hints()

def apply_hints():
    for _, status, disable_const, enable_const in hints:
        py5.hint(enable_const if status else disable_const)

py5.run_sketch()