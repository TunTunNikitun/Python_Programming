"""
Выведите таблицу размером n×n, заполненную числами от 11 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""


def zm(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n ** 2 + 1):
        arr[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for x in list(zip(*arr)):
        print(*x)


zm(int(input()))