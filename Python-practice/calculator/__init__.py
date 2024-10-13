from basic import Calculator
from engineering import Engineering_Calculator
from engineering import DivisionByZeroError

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

