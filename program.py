import additional_program


class Triangle:
	def __init__(self, a, b, c):
		self._is_triangle(a, b, c)
		self.check_param(a)
		self.check_param(b)
		self.check_param(c)
		self._a = a
		self._b = b
		self_c = c

	@staticmethod
	def check_param(value):
		if type(value) not in (int, float) or value <= 0:
			raise TypeError('стороны треугольника должны быть положительными числами')

	@staticmethod
	def _is_triangle(a, b, c):
		if a >= c + b or c >= a + b or b >= c + a:
			raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]  # эту строчку не менять (переменную input_data также не менять)

lst_tr = []
for tup in input_data:
	try:
		obj = Tuple(*tup)
		lst_tr.append(obj)
	except:
		continue

additional_program.main()