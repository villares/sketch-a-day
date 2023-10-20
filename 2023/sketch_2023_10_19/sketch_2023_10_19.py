def setup():
#    size(600, 600, P3D)
#    begin_raw(SVG, 's.svg')
#    rotate_y(QUARTER_PI)
    size(600, 600, P2D)
    begin_shape()
    fill(0, 200, 0)
    vertex(300, 100)
    fill(0, 0, 200)
    vertex(100, 500)
    fill(200, 0, 0)
    vertex(500, 500)    
    end_shape(CLOSE)
#    end_raw()
        
        
        
        
        
        
#         
#     no_stroke()   
#     for r in range(255, -1, -1):
#         fill(r)
#         circle(150, 300, r * 2)
#         
#     cor_a = color(0, 0, 200)
#     cor_b = color(200, 0, 0)
#     for r in range(255, -1, -1):
#         cor = lerp_color(cor_a, cor_b, 1 - r / 255)
#         fill(cor)
#         no_stroke()
#         circle(450, 300, r * 2)
#         stroke(cor)
#         line(r, 0, r, 200)

        
        

