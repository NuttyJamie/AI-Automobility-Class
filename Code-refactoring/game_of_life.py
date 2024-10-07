# 라이브러리 import
import random	
import time	

# 셀 생사 여부를 나타내는 변수에 0or1 지정
# 0, 1 => True, False bool 값으로 대체
DEAD = 0	
LIVE = 1

# 셀들이 활동할 수 있는 가로x세로 크기의 보드를 생성 후 반환
# state 위주의 동작보다 board와 cell 위주의 이름, 동작이 조금 더 직관적으로 해석할 수 있을 것으로 예상, Board 클래스를 작성하고 단위 시간마다 상태를 갱신하는 등 관련 함수들을 캡슐화 하기로 결정. 
def dead_state(width, height):
    """Constuct an empty state with all cells set to DEAD.

    Parameters
    ----------
    width: the width of the state, in cells
    height: the height of the state, in cells

    Returns
    -------
    A state of dimensions width x height, with all cells set to DEAD
    """
    return [[DEAD for _ in range(height)] for _ in range(width)]

# 보드 내의 모든 셀들의 상태를 무작위로 지정 후 반환
def random_state(width, height):
    """Construct a random state with all cells randomly set.

    Parameters
    ----------
    width: the width of the state, in cells
    height: the height of the state, in cells

    Returns
    -------
    A state of dimensions width x height, with all cells randomly set to either
        DEAD or LIVE with equal probability.
    """
    state = dead_state(width, height)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            random_number = random.random()
            if random_number > 0.85:
                cell_state = LIVE
            else:
                cell_state = DEAD
            state[x][y] = cell_state

    return state

# 입력 상태의 폭을 반환
def state_width(state):
    """Get the width of a state.

    Parameters
    ----------
    state: a Game state

    Returns
    -------
    The width of the input state
    """
    return len(state)

# 입력 상태의 높이를 반환
def state_height(state):
    """Get the height of a state.

    Parameters
    ----------
    state: a Game state

    Returns
    -------
    The height of the input state
    """
    return len(state[0])

# 세포의 다음 상태를 반환
def next_cell_value(cell_coords, state):
    """Get the next value of a single cell in a state.

    Parameters
    ----------
    cell_coords: an (x, y) tuple of the co-ordinates of a cell
    state: the current state of the Game board

    Returns
    -------
    The new state of the given cell - either DEAD or LIVE.
    """
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    # Iterate around this cell's neighbors
    for x1 in range((x-1), (x+1)+1):
        # Make sure we don't go off the edge of the board
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            # Make sure we don't go off the edge of the board
            if y1 < 0 or y1 >= height: continue
            # Make sure we don't count the cell as a neighbor of itself!
            if x1 == x and y1 == y: continue

            if state[x1][y1] == LIVE:
                n_live_neighbors += 1

    if state[x][y] == LIVE:
        if n_live_neighbors <= 1:
            return DEAD
        elif n_live_neighbors <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if n_live_neighbors == 3:
            return LIVE
        else:
            return DEAD

# 모든 셀의 다음 상태를 계산 후 다음 보드의 상태를 반환
def next_board_state(init_state):
    """Take a single step in the Game of Life.

    Parameters
    ----------
    init_state: the initial state of the Game board

    Returns
    -------
    The next state of the Game board, after taking one step for every cell in
        the previous state.
    """
    width = state_width(init_state)
    height = state_height(init_state)
    next_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), init_state)

    return next_state

# 계산이 끝난 상태의 보드를 출력 
def render(state):
    """Displays a state by printing it to the terminal.

    Parameters
    ----------
    state: a Game state

    Returns
    -------
    Nothing - this is purely a display function.
    """
    display_as = {
        DEAD: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick
        # "ASCII" character like a '$' or '#'.
        LIVE: u"\u2588"
    }
    lines = []
    for y in range(0, state_height(state)):
        line = ''
        for x in range(0, state_width(state)):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)

# 파일을 열어 보드를 로드
def load_board_state(filepath):
    """Loads a board state from the given filepath

    Parameters
    ----------
    filepath: the filepath to load the state from. Dead cells should be
        represented by 0s, live cells by 1s

    Returns
    -------
    The board state loaded from the given filepath
    """
    with open(filepath, 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = dead_state(height, width)

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            board[x][y] = int(char)
    return board

# 게임 무한 루프로 가동 
def run_forever(init_state):
    """Runs the Game of Life forever, starting from the given initial state.

    Parameters
    ----------
    init_state: the Game state to start at

    Returns
    -------
    This function never returns - the program must be forcibly exited!
    """
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

# 인터프리터에서 실행 시 100*50 사이즈의 랜덤상태 실행
if __name__ == "__main__":
    init_state = random_state(100, 50)
    # init_state = load_board_state('./toad.txt')
    run_forever(init_state)
