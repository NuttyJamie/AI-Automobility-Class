import math

class Calculator:
	"""
사칙연산을 수행하는 계산기 클래스.

덧/뺄/곱/나눗셈을 수행하는 주요 사칙연산 메서드와 
반올림 메서드, 강제 실수 반환 메서드로 구성된다.

각 사칙 연산 메서드에 정수 또는 실수의 피연산자를 인자로 전달하고 
'precision', 'return_float' 옵션을 지정하여 계산 결과의 포맷을 변경 가능하다. 

_precision:
	계산 결과와 반올림할 자릿수를 인자로 전달받는다. 
	전달받은 정수형 인자를 문자열로 변환 후 format 함수로 자릿수에 맞게 출력한다.

_return_float:
	계산 결과(정수/실수)와 실수 변환 여부(Bool값)를 인자로 전달받는다.
	변환 여부에 따라 삼항연산자를 통해 float형변환 또는 그대로 출력한다.
	
사용 예시:
	print(calc.add(1,2,3, return_float=True))
	print(calc.subtract(10,2,3, precision=2))
	"""
	def __init__(self):
		pass
		
	def _precision(self, num: int, digit: int) -> str:
		format_string = "{:." + str(digit) + "f}"
		return format_string.format(num)

	def _return_float(self, obj: int, opt: bool=False) -> float:
		return float(obj) if opt is True else obj

	def add(self, *args: list, **kwargs: dict) -> float:
		"""
0으로 초기화된 result에 각 인자를 더한 후 지정된 옵션에 따라 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.
		"""
		self.result=0
		for i in range(len(args)):
			self.result+=args[i]

		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def subtract(self, *args: list, **kwargs: dict) -> float:
		"""
첫 번째 인자에서 나머지 인자들을 뺀 값을 지정된 옵션에 따라 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.
		"""
		self.result=args[0]
		for i in range(len(args[1:])):
			self.result-=args[i+1]

		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def multiply(self, *args: list, **kwargs: dict) -> float:
		"""
전달된 인자를 모두 곱한 값을 지정된 옵션에 따라 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.
		"""
		self.result=args[0]
		for i in range(len(args[1:])):
			self.result*=args[i+1]
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def divide(self, *args: list, **kwargs: dict) -> float:
		"""
첫 번째 인자를 나머지 인자로 차례로 나눈 값을 지정된 옵션에 따라 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

예외:
	0으로 나누기를 시도할 경우 에러를 반환한다. 
	ex) print(calc.divide(2,4,0))
		"""
		self.result=args[0]
		for i in range(len(args[1:])):
			if args[i+1] != 0:
				self.result/=args[i+1]
			else:
				return 'Not divisible by zero'
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

class Engineering_Calculator(Calculator):
	"""
기본 사칙연산 계산기 클래스 Calculator를 상속받아 사칙연산, 반올림,
실수 반환 기능과 더불어 여러 공학용 계산을 수행하는 공학용 계산기 클래스.

각 사칙 연산 메서드에 정수 또는 실수의 피연산자를 인자로 전달하고 
'precision', 'return_float' 옵션을 지정하여 계산 결과의 포맷을 변경 가능하다. 

_precision:
	계산 결과와 반올림할 자릿수를 인자로 전달받는다. 
	전달받은 정수형 인자를 문자열로 변환 후 format 함수로 자릿수에 맞게 출력한다.

_return_float:
	계산 결과(정수/실수)와 실수 변환 여부(Bool값)를 인자로 전달받는다.
	변환 여부에 따라 삼항연산자를 통해 float형변환 또는 그대로 출력한다.
	
사용 예시:
	print(eng_calc.power(8, 3, return_float=True))
	print(eng_calc.square_root(16, precision=3))
	print(eng_calc.log(100, precision=4))
	print(eng_calc.sin(30, angle_unit='degree', precision=4))
	"""
	def __init__(self):
		pass

	def square_root(self, x: float, **kwargs: dict) -> float:
		"""
첫 번째 인자의 제곱근을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.square_root(16, precision=3))
		"""
		self.result=math.isqrt(x)
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def power(self, x: float, y: float, **kwargs: dict) -> float:
		"""
x의 y제곱을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.power(8, 3, return_float=True))
		"""
		self.result=pow(x, y)
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	#TODO:x=0, base=0,1 exception error
	def log(self, x: float, base: int =10, **kwargs: dict) -> float:
		"""
log_base_(x) 값을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.log(100, precision=4))
		"""
		self.result=math.log(x, base)
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	#TODO:x=0 exception error
	def ln(self, x: float, **kwargs: dict) -> float:
		"""
상용로그 ln(x) 값을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.ln(388, precision=7))
		"""
		self.result=math.log(x)
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def sin(self, x: float, angle_unit: str ='radian', **kwargs: dict) -> float:
		"""
삼각함수 sin(x) 값을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.sin(30, angle_unit='degree', precision=4))
		"""
		self.result=math.sin(x)\
				if angle_unit == 'radian' \
				else math.sin(math.radians(x))

		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def cos(self, x: float, angle_unit: str ='radian', **kwargs: dict) -> float:
		"""
삼각함수 cos(x) 값을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.cos(90, angle_unit='degree'))
		"""
		self.result=math.cos(x)\
				if angle_unit == 'radian' \
				else math.cos(math.radians(x))

		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	#TODO:edgecase exception
	def tan(self, x: float, angle_unit: str ='radian', **kwargs: dict) -> float:
		"""
삼각함수 tan(x) 값을 반환한다.

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.tan(45, angle_unit='degree', precision=4))
		"""
		self.result=math.tan(x)\
				if angle_unit == 'radian' \
				else math.tan(math.radians(x))

		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

	def divide(self, *args: list, **kwargs: dict) -> float:
		"""
Calculator.divide 메서드 오버라이딩.
첫 번째 인자를 나머지 인자로 차례로 나눈 값을 지정된 옵션에 따라 반환한다.

예외:
	0으로 나누기를 시도할 경우 에러를 반환한다. 
	example:
		try:
			print(eng_cal.divide(5, 0))
		except DivisionByZeroError as e:
			print(e)

옵션:
	'precision':
		int, default=None
		result의 소숫점 자릿수를 precision 값에 맞게 반올림 후 반환한다.
	'return_float':
		Bool, default=False
		True일 경우 강제 형 변환을 통해 result를 실수로 반환한다.

사용 예시:
	print(eng_cal.divide(60, 6))
		"""
		self.result=args[0]
		for i in range(len(args[1:])):
			if args[i+1] == 0:
				raise DivisionByZeroError("Division by zero is not allowed")
			else:
				self.result/=args[i+1]
		return self._return_float(self.result, kwargs.get('return_float')) \
				if 'precision' not in kwargs \
				else self._precision(self.result, kwargs['precision'])

class DivisionByZeroError(Exception):
	"""
0으로 나눗셈을 시도할 경우 주어진 에러 문구를 출력하고
에러를 발생시키는 사용자 정의 에러 클래스.
	"""
	def __init__(self, msg: str):
		self.msg=msg
	def __str__(self):
		return self.msg

__all__=["Calculator", "Engineering_Calculator"]

if __name__ == '__main__':
	print("{0:=^40}".format("사용 예시"))
	print("#인스턴스 생성:\ncal=Calculator()\n")
	cal=Calculator()

	print("#메서드 사용")
	print("{0:<43}".format("print(cal.add(1,2,3, return_float=True))"), end=' => ')
	print(cal.add(1,2,3, return_float=True))
	print("{0:<43}".format("print(cal.add(4291.802992,2,3.4280))"), end=' => ')
	print(cal.add(4291.802992,2,3.4280))
	print("{0:<43}".format("print(cal.add(1,2,3, precision=4))"), end=' => ')
	print(cal.add(1,2,3, precision=4))
	print("{0:<43}".format("print(cal.subtract(10,2,3, precision=2))"), end=' => ')
	print(cal.subtract(10,2,3, precision=2))
	print("{0:<43}".format("print(cal.multiply(2,3,4))"), end=' => ')
	print(cal.multiply(2,3,4))
	print("{0:<43}".format("print(cal.divide(2,4,0))"), end=' => ')
	print(cal.divide(2,4,0))

	print("\n#인스턴스 생성:\neng_cal=Engineering_Calculator()\n")
	eng_cal=Engineering_Calculator()
	print("{0:<56}".format("print(eng_cal.power(8, 3, return_float=True))"), end=' => ')
	print(eng_cal.power(8, 3, return_float=True))
	print("{0:<56}".format("print(eng_cal.square_root(16, precision=3))"), end=' => ')
	print(eng_cal.square_root(16, precision=3))
	print("{0:<56}".format("print(eng_cal.log(100, precision=4))"), end=' => ')
	print(eng_cal.log(100, precision=4))
	print("{0:<56}".format("print(eng_cal.ln(388, precision=7))"), end=' => ')
	print(eng_cal.ln(388, precision=7))
	print("{0:<56}".format("print(eng_cal.cos(60, angle_unit='degree', precision=2))"), end=' => ')
	print(eng_cal.cos(60, angle_unit='degree', precision=2))
	print("{0:<56}".format("print(eng_cal.sin(30, angle_unit='degree', precision=4))"), end=' => ')
	print(eng_cal.sin(30, angle_unit='degree', precision=4))
	print("\n#divide 메서드 예외 처리:")
	print("try:\n    print(eng_cal.divide(5, 0))\nexcept DivisionByZeroError as e:\n    print(e)\n\n=> ", end='')
	try:
		print(eng_cal.divide(5, 0))
	except DivisionByZeroError as e:
		print(e)
	print("="*45)

