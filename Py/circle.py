import matplotlib.pyplot as plot

def createCircle():
    circle = plot.Circle((0,0), radius= 5)
    return circle

def createCircle2():
    circle = plot.Circle((15,15), radius= 5)
    return circle

def showShape(patch):
	ax = plot.gca()
	ax.add_patch(patch)
	plot.axis('scaled')
    plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
	plot.show()

if __name__== '__main__':
    c = createCircle()
    d = createCircle2()
    showShape(c,d)
