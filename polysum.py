import math

def polysum(n, s):
	"""
	Input: number of sides n and 
	length of side of regular polygon s

	Returns the sum of area and square of
	perimeter of regular polygon
	"""
	
	area = (0.25*n*s*s)/math.tan(math.pi/n)
	per = n * s
	per = per * per
	
	return round(area + per, 4)
