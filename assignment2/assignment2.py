import pygame
import random
import sys

# 常量定义
BLOCK_SIZE = 40
CELL_EMPTY = 0
CELL_BODY = 1
CELL_HEAD = 2
GRID_SIZE = 10

# 初始化Pygame
pygame.init()

# 设置窗口
WIDTH = GRID_SIZE * (BLOCK_SIZE + 4)
HEIGHT = GRID_SIZE * (BLOCK_SIZE + 4) + BLOCK_SIZE * 1.5 + 4
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aircraft Game")

# 设置颜色
colors = {
    CELL_EMPTY: (236, 239, 241),  # cell_empty
    CELL_BODY: (21, 101, 192),    # cell_body
    CELL_HEAD: (194, 24, 91),      # cell_head
    'gray': (169, 169, 169)        # 灰色
}

# 游戏变量
board = []
visited = []
score = 0
remain = 2

def init_board(size):
    global board, visited
    board = [[CELL_EMPTY for _ in range(size)] for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]

def check_aircraft_valid(head_direction, i_center, j_center):
    directions = {
        0: [(0, 0), (0, -1), (-1, 0), (-2, 0), (1, 0), (2, 0), (0, 1), (0, 2), (-1, 2), (1, 2)],
        1: [(0, 0), (0, 1), (-1, 0), (-2, 0), (1, 0), (2, 0), (0, -1), (0, -2), (-1, -2), (1, -2)],
        2: [(0, 0), (-1, 0), (0, -1), (0, -2), (0, 1), (0, 2), (1, 0), (2, 0), (2, -1), (2, 1)],
        3: [(0, 0), (1, 0), (0, -1), (0, -2), (0, 1), (0, 2), (-1, 0), (-2, 0), (-2, -1), (-2, 1)]
    }

    for dx, dy in directions[head_direction]:
        if not (0 <= i_center + dx < len(board) and 0 <= j_center + dy < len(board)):
            return False
        if board[i_center + dx][j_center + dy] != CELL_EMPTY:
            return False
    return True

def create_aircraft(size, count):
    global remain
    remain = count
    for _ in range(count):
        head_direction = random.randint(0, 3)
        while True:
            i_center = random.randint(2, size - 3)
            j_center = random.randint(2, size - 3)

            if check_aircraft_valid(head_direction, i_center, j_center):
                if head_direction == 0:  # left
                    board[i_center][j_center] = CELL_BODY
                    board[i_center][j_center - 1] = CELL_HEAD
                    for dx in [-1, -2, 1, 2]:
                        board[i_center + dx][j_center] = CELL_BODY
                    for dy in [1, 2]:
                        board[i_center][j_center + dy] = CELL_BODY
                    board[i_center - 1][j_center + 2] = CELL_BODY
                    board[i_center + 1][j_center + 2] = CELL_BODY
                elif head_direction == 1:  # right
                    board[i_center][j_center] = CELL_BODY
                    board[i_center][j_center + 1] = CELL_HEAD
                    for dx in [-1, -2, 1, 2]:
                        board[i_center + dx][j_center] = CELL_BODY
                    for dy in [-1, -2]:
                        board[i_center][j_center + dy] = CELL_BODY
                    board[i_center - 1][j_center - 2] = CELL_BODY
                    board[i_center + 1][j_center - 2] = CELL_BODY
                elif head_direction == 2:  # up
                    board[i_center][j_center] = CELL_BODY
                    board[i_center - 1][j_center] = CELL_HEAD
                    for dy in [-1, -2, 1, 2]:
                        board[i_center][j_center + dy] = CELL_BODY
                    for dx in [1, 2]:
                        board[i_center + dx][j_center] = CELL_BODY
                    board[i_center + 2][j_center - 1] = CELL_BODY
                    board[i_center + 2][j_center + 1] = CELL_BODY
                else:  # down
                    board[i_center][j_center] = CELL_BODY
                    board[i_center + 1][j_center] = CELL_HEAD
                    for dy in [-1, -2, 1, 2]:
                        board[i_center][j_center + dy] = CELL_BODY
                    for dx in [-1, -2]:
                        board[i_center + dx][j_center] = CELL_BODY
                    board[i_center - 2][j_center - 1] = CELL_BODY
                    board[i_center - 2][j_center + 1] = CELL_BODY
                break

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = colors['gray'] if not visited[i][j] else colors[board[i][j]]
            pygame.draw.rect(screen, color, (
                j * (BLOCK_SIZE + 4), i * (BLOCK_SIZE + 4) + BLOCK_SIZE * 1.5 + 4, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (
                j * (BLOCK_SIZE + 4), i * (BLOCK_SIZE + 4) + BLOCK_SIZE * 1.5 + 4, BLOCK_SIZE, BLOCK_SIZE), 1)

def show_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

def show_remain():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Remain: {remain}', True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 10))

def reset_game():
    global score
    score = 0
    init_board(GRID_SIZE)

# 获取用户输入的飞机数量
def get_aircraft_count():
    while True:
        try:
            count = int(input("Please enter the number of aircraft (greater than 0 and less than or equal to 3): "))
            if count <= 0:
                print("Invalid input, please enter a number greater than 0.")
            elif count > 3:
                print("Too many, please enter a number less than or equal to 3.")
            else:
                return count
        except ValueError:
            print("Please enter a valid number.")

# 主逻辑
aircraft_count = get_aircraft_count()
reset_game()
create_aircraft(GRID_SIZE, aircraft_count)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y > (BLOCK_SIZE * 1.5 + 4):
                i = int((y - (BLOCK_SIZE * 1.5 + 4)) // (BLOCK_SIZE + 4))
                j = int(x // (BLOCK_SIZE + 4))

                if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and not visited[i][j]:
                    visited[i][j] = True
                    score += 1

                    if board[i][j] == CELL_HEAD:
                        remain -= 1

                    if remain == 0:
                        font = pygame.font.Font(None, 72)
                        text = font.render("Good Job!", True, (255, 0, 0))
                        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                        font = pygame.font.Font(None, 48)
                        text2 = font.render(f"Your score is: {score}", True, (0, 0, 0))
                        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.wait(5000)
                        reset_game()
                        create_aircraft(GRID_SIZE, aircraft_count)

    screen.fill((255, 255, 255))
    draw_grid()
    show_score()
    show_remain()

    pygame.display.flip()