def round_result(value, precision):
	format_string = "{:." + str(precision) + "f}"
	return format_string.format(value)

def convert_to_radians(angle: float, unit: str = 'degree'):
	math.radians(angle)
