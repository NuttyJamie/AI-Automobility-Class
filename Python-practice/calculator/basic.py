import utils

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
	print("="*45)

