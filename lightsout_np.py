import numpy as np

#指定のパネルの反転をする関数
def lightsout(x, y):
    right = np.stack([x[np.where(x < n-1)]+1, y[np.where(x < n-1)]])
    left = np.stack([x[np.where(x > 0)]-1, y[np.where(x > 0)]])
    down = np.stack([x[np.where(y < n-1)], y[np.where(y < n-1)]+1])
    up = np.stack([x[np.where(y > 0)], y[np.where(y > 0)]-1])
    light_bool[x, y] = np.logical_not(light_bool[x, y])
    light_bool[right[0], right[1]] = np.logical_not(light_bool[right[0], right[1]])
    light_bool[left[0], left[1]] = np.logical_not(light_bool[left[0], left[1]])
    light_bool[down[0], down[1]] = np.logical_not(light_bool[down[0], down[1]])
    light_bool[up[0], up[1]] = np.logical_not(light_bool[up[0], up[1]])

#問題のランダム生成
n = 4
light_bool = np.full((n, n), True)
create_random = np.random.randint(0, n, (2, np.random.randint(3, n*2)))
lightsout(create_random[0], create_random[1]) #クリア可能にする処理

#メインゲーム
while True:
    print(np.where(light_bool, ".", "#"))

    if  np.all(light_bool):
        print("game clear!!")
        break

    try:
        x, y = map(int, input().split())
        lightsout(np.array([x-1]), np.array([y-1]))
    except ValueError:
        print("入力方式が違います")
    except IndexError:
        print("パネルが存在しません")