import random
import time

# 셀의 상태를 나타내는 상수
DEAD = False
LIVE = True

# 게임의 규칙에 따른 생명 기준 상수
DEATH_LIMIT: int = 1  # 인접 셀이 1개 이하일 때 셀 삭제
SURVIVE_LIMIT: int = 3  # 인접 셀이 2개 또는 3개일 때 셀 보존
REPRODUCTION_NEIGHBORS: int = 3  # 인접 셀이 3개일 때 새로운 셀 탄생
BIRTH_RATE: float = 0.85

# 셀 출력 기호
CELL_CHARACTER = u"\u2588"

# 출력 딜레이 시간
RENDER_DELAY = 1

class Board:
	def __init__(self, width: int = 100, height: int = 100):
		"""
		보드 초기화 및 크기 설정

		매개 변수:
			width: int
				보드의 폭
			height: int
				보드의 높이
				
		사용 예시:
			board = Board()
			board.randomize_board()
			board.run()
		"""
		self.width = width
		self.height = height
		self.state = self.initialize_board()

	def initialize_board(self) -> list[list[bool]]:
		"""
		모든 셀을 DEAD 상태로 초기화한 2차원 리스트를 반환
		"""
		return [[DEAD for _ in range(self.height)] for _ in range(self.width)]

	def randomize_board(self) -> list[list[int]]:
		"""
		모든 셀을 탄생 확률 계수(BIRTH RATE)를 기반으로 무작위로 초기화한 2차원 리스트를 반환
		"""
		self.state = self.initialize_board()
		for x in range(self.width):
			for y in range(self.height):
				self.state[x][y] = LIVE if random.random() > BIRTH_RATE else DEAD
		return self.state

	def get_next_cell_value(self, cell_coords: tuple) -> int:
		"""
		주어진 셀의 다음 상태를 계산하여 반환

		매개 변수:
			cell_coords: tuple 
				(x, y) 좌표 튜플
		"""
		x, y = cell_coords
		live_neighbors = self.count_live_neighbors(x, y)

		if self.state[x][y] == LIVE:
			if live_neighbors <= DEATH_LIMIT:
				return DEAD
			elif live_neighbors <= SURVIVE_LIMIT:
				return LIVE
			else:
				return DEAD
		else:
			if live_neighbors == REPRODUCTION_NEIGHBORS:
				return LIVE
			else:
				return DEAD

	def count_live_neighbors(self, x: int, y: int) -> int:
		"""
		주어진 셀을 기준으로 인접 셀의 개수를 계산하여 반환

		매개 변수:
			x: int
				셀의 x 좌표
			y: int
				셀의 y 좌표
		"""
		live_neighbors = 0
		for x1 in range(x - 1, x + 2):
			if x1 < 0 or x1 >= self.width:
				continue
			for y1 in range(y - 1, y + 2):
				if y1 < 0 or y1 >= self.height or (x1 == x and y1 == y):
					continue
				if self.state[x1][y1] == LIVE:
					live_neighbors += 1
		return live_neighbors

	def update_board(self) -> list[list[int]]:
		"""
		모든 셀의 다음 상태를 계산하고 보드를 업데이트
		"""
		next_state = self.initialize_board()
		for x in range(self.width):
			for y in range(self.height):
				next_state[x][y] = self.get_next_cell_value((x, y))
		self.state = next_state
		return self.state

	def render(self) -> None:
		"""
		현재 보드 상태를 출력
		"""
		display_as = {DEAD: ' ', LIVE: CELL_CHARACTER}
		lines = []
		for y in range(self.height):
			line = ''
			for x in range(self.width):
				line+=display_as[self.state[x][y]] * 2
			lines.append(line)
		print("\n".join(lines))

	def load_board_state(self, filepath: str) -> list[list[int]]:
		"""
		파일에서 보드 상태를 읽고 초기화

		매개 변수:
			filepath: 읽어올 파일 경로
		"""
		with open(filepath, 'r') as f:
			lines = [l.rstrip() for l in f.readlines()]

		height = len(lines)
		width = len(lines[0])
		board = self.initialize_board()

		for x, line in enumerate(lines):
			for y, char in enumerate(line):
				board[x][y] = int(char)
		self.state = board
		self.width = width
		self.height = height
		return board

	def run(self) -> None:
		"""
		게임 루프를 시작하여 보드 상태를 반복적으로 갱신 및 출력
		"""
		while True:
			self.render()
			self.update_board()
			time.sleep(RENDER_DELAY)

if __name__ == "__main__":
	board = Board()
	board.randomize_board()
	board.run()
