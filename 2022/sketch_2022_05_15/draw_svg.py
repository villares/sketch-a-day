

mykey = str(1)    
svgNS = "http://www.w3.org/2000/svg"     
svgelement = document.createElementNS(svgNS, 'svg')    
svgelement.setAttributeNS(None,"width","100%")   
svgelement.setAttributeNS(None,"height","100%")
svgelement.setAttributeNS(None,"key", mykey)    
def circle(x, y, d, stroke='black', fill='white'):
    c = document.createElementNS(svgNS, "circle")
    # c.setAttributeNS(None,"id","mycircle")
    c.setAttributeNS(None,"cx", x)
    c.setAttributeNS(None,"cy",y)
    c.setAttributeNS(None,"r", d / 2)
    c.setAttributeNS(None,"fill", fill)
    c.setAttributeNS(None,"stroke", stroke)
    return c

def rect(x, y, w, h, stroke='black', fill='white'):
    c = document.createElementNS(svgNS, "rect")
    # c.setAttributeNS(None,"id","mycircle")
    c.setAttributeNS(None,"x", x)
    c.setAttributeNS(None,"y", y)
    c.setAttributeNS(None,"width", w)
    c.setAttributeNS(None,"height", h)
    c.setAttributeNS(None,"fill", fill)
    c.setAttributeNS(None,"stroke", stroke)
    return c

svgelement.appendChild(circle(100, 100, 100))    
svgelement.appendChild(rect(100, 100, 100, 50))    

# write into DIV    
document.getElementById("ContainerBox").append(svgelement)   