

mykey = str(1)    
svgNS = "http://www.w3.org/2000/svg"     
svgelement = document.createElementNS(svgNS, 'svg')    
svgelement.setAttributeNS(None,"width","100%")   
svgelement.setAttributeNS(None,"height","100%")
svgelement.setAttributeNS(None,"key", mykey)    
def circle(x, y, d, stroke='black', fill='white'):
    c = document.createElementNS(svgNS, "circle")
    c.setAttributeNS(None,"cx", x)
    c.setAttributeNS(None,"cy",y)
    c.setAttributeNS(None,"r", d / 2)
    c.setAttributeNS(None,"fill", fill)
    c.setAttributeNS(None,"stroke", stroke)
    svgelement.appendChild(c)
    return c

def rect(x, y, w, h, stroke='black', fill='white'):
    r = document.createElementNS(svgNS, "rect")
    r.setAttributeNS(None,"x", x)
    r.setAttributeNS(None,"y", y)
    r.setAttributeNS(None,"width", w)
    r.setAttributeNS(None,"height", h)
    r.setAttributeNS(None,"fill", fill)
    r.setAttributeNS(None,"stroke", stroke)
    svgelement.appendChild(r)
    return r

circle(100, 100, 100) 
rect(100, 100, 100, 50)

# write into DIV    
document.getElementById("ContainerBox").append(svgelement)   