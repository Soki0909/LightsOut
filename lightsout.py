import random

#指定のパネルの反転をする関数
def lightsout(x, y):
    light_bool[x][y] = not light_bool[x][y]
    if x > 0:
        light_bool[x-1][y] = not light_bool[x-1][y]
    if x < n-1:
        light_bool[x+1][y] = not light_bool[x+1][y]
    if y > 0:
        light_bool[x][y-1] = not light_bool[x][y-1]
    if y < n-1:
        light_bool[x][y+1] = not light_bool[x][y+1]

#問題のランダム生成
n = 4
light_bool = [[True] * n for _ in range(n)]

for _ in range(random.randint(3, n*2)):
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    lightsout(x, y)#クリア可能にする処理

#メインゲーム
while True:
    count = 0
    for row in light_bool:
        for entry in row:
            if entry:
                light = "'.' "
                count += 1
            else:
                light = "'#' "
            print(light, end="")
        print()

    if count == n ** 2:
        print("game clear!!")
        break
    
    try:
        x, y = map(int, input().split())
        lightsout(x-1, y-1)
    except ValueError:
        print("入力方式が違います")
    except IndexError:
        print("パネルが存在しません")