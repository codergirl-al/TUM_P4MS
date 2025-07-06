def compute_triangle(a, b, c):
	if a + b <= c or a + c <= b or b + c <= a:
		return -1
	perimeter = a + b + c
	s = perimeter / 2
	area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	return round(perimeter, 2), round(area, 2)