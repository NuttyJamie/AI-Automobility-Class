#패키지 구조
calculator/
│
├── __init__.py
│		표준 math모듈과 계산기 모듈 import	
├── basic.py
│		#클래스
│		Calculator()
│			#메서드
│			add()
│			subtract()
│			multiply()
│			divide()
├── engineering.py
│		#클래스
│		Calculator()	#basic.Calculator 상속
│			#메서드
│			square_root()
│			power()
│			log()
│			ln()
│			sin()
│			cos()
│			tan()
│			divide()
├── utils.py
│		#함수	
│		round_result()
│		convert_to_radians()
└── README.md

=================사용 예시==================
#인스턴스 생성:
cal=Calculator()

#메서드 사용
print(cal.add(1,2,3, return_float=True))    => 6.0
print(cal.add(4291.802992,2,3.4280))        => 4297.230992
print(cal.add(1,2,3, precision=4))          => 6.0000
print(cal.subtract(10,2,3, precision=2))    => 5.00
print(cal.multiply(2,3,4))                  => 24
print(cal.divide(2,4,0))                    => Not divisible by zero

#인스턴스 생성:
eng_cal=Engineering_Calculator()

print(eng_cal.power(8, 3, return_float=True))            => 512.0
print(eng_cal.square_root(16, precision=3))              => 4.000
print(eng_cal.log(100, precision=4))                     => 2.0000
print(eng_cal.ln(388, precision=7))                      => 5.9610053
print(eng_cal.cos(60, angle_unit='degree', precision=2)) => 0.50
print(eng_cal.sin(30, angle_unit='degree', precision=4)) => 0.5000

#divide 메서드 예외 처리:
try:
    print(eng_cal.divide(5, 0))
except DivisionByZeroError as e:
    print(e)

=> Division by zero is not allowed
=============================================
