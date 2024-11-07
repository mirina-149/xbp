print("★ 数当てゲーム ★")
#乱数を生成する関数
import random
#1から100までのランダムな整数
#aはコンピューターが決めた整数
a = random.randint(1, 100)
#While Trueで答えがTrueになるまで繰り返す
#bは回答者が入力した整数
while True:
    b = int(input("1から100までの数を予想してください"))
    if b == a:
        print("正解!")
        break
    #回答した数字が答えより小さい時
    elif b < a:
        print("もっと大きい数です。")
    #回答した数字が答えより大きい時（elifでもないとき）
    else:
        print("もっと小さい数です。")