import requests
API_KEY="814ae22dc8dee21099aeb27cb9525f64"
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
# ユーザーから都市名を入力してもらう
city_name = input("都市名を英語で入力してね")
city = city_name
request_url = f' {BASE_URL}?q={city}&appid={API_KEY}'
response = requests.get (request_url)
if response.status_code == 200:
    data = response. json()
    weather = data['weather'][0]['description']
    temperature = round (data[ 'main' ]['temp'] - 273.15, 2)
    print(f'Weather: {weather}')
    print(f' Temperature: {temperature}℃')


    if weather == "clear sky" and temperature>30:
        print("プールや川で水遊び！熱中症には気を付けて！")
    elif weather=="few clouds"and temperature>30:
                print("ひまわり畑や大自然の景色を眺めに行ってみるといいね")
    elif weather=="scattered clouds"and temperature>30:
                print("アイスやかき氷を食べに行ってみよう！")
    elif weather=="broken clouds"and temperature>30:
                print("浴衣を着て食べ歩きが楽しそう！")
    elif weather=="light rain"and temperature>30:
                print("流しそうめんで夏を感じよう！")
    elif weather=="rain"and temperature>30:
                print("水族館でゆったり過ごしてみるとよさそう！")
    elif weather=="thunderstorm"and temperature>30:
                print("外は危ないから家の中でゲームや本を読んでゆっくりしよう！")
    elif weather=="mist"and temperature>30:
                print("なるべく外に出ないようにしよう！")

    elif weather == "clear sky" and 31>temperature>20:
                print("自然を感じられる旅行に行ってみよう！")
    elif weather=="few clouds"and 31>temperature>20:
                print("遊園地に行って楽しもう！")
    elif weather=="scattered clouds"and 31>temperature>20:
                print("カフェ巡りで心を癒そう！")
    elif weather=="broken clouds"and 31>temperature>20:
                print("ドライブ旅行で行ったことのない場所に行ってみよう！")
    elif weather=="shower rain"and 31>temperature>20:
                print("室内アスレチックで体を動かしてリフレッシュしよう！")
    elif weather=="light rain"and 31>temperature>20:
                print("室内アスレチックで体を動かしてリフレッシュしよう！")
    elif weather=="rain"and 31>temperature>20:
                print("ショッピングで破産するまで買いまくれ！")
    elif weather=="thunderstorm"and 31>temperature>20:
                print("外は危ないから家の中でゲームや本を読んでゆっくりしよう！")
    elif weather=="mist"and 31>temperature>20:
                print("なるべく外に出ないようにしよう！")

    elif weather == "clear sky" and 21>temperature>12:
                print("季節を感じられるスポットに行ってみよう！")
    elif weather=="few clouds"and 21>temperature>12:
                print("景色のいい公園をお散歩してみよう！")
    elif weather=="scattered clouds"and 21>temperature>12:
                print("食べ歩きに行ってお腹いっぱいになるまで食べまくろう！")
    elif weather=="broken clouds"and 21>temperature>12:
                print("おしゃれなごはん屋さんに行って幸せを感じよう！")
    elif weather=="shower rain"and 21>temperature>12:
                print("室内で楽しめるおしゃれスポットに行って写真をいっぱい撮ろう！")
    elif weather=="light rain"and 21>temperature>12:
                print("室内で楽しめるおしゃれスポットに行って写真をいっぱい撮ろう！")
    elif weather=="rain"and 21>temperature>12:
                print("カラオケやボーリングで楽しい時間を過ごそう！")
    elif weather=="thunderstorm"and 21>temperature>12:
                print("外は危ないから家の中でゲームや本を読んでゆっくりしよう！")
    elif weather=="mist"and 21>temperature>12:
                print("なるべく外に出ないようにしよう！")
    
    elif weather == "clear sky" and 13>temperature:
                print("朝日や夕日を見に行こう！")
    elif weather=="few clouds"and 13>temperature:
                print("イルミネーションを見に行こう！")
    elif weather=="scattered clouds"and 13>temperature:
                print("温泉巡りで体を温めよう！")
    elif weather=="broken clouds"and 13>temperature:
                print("映画を見てゆっくりしよう！")
    elif weather=="shower rain"and 13>temperature:
                print("体が温まるおいしいごはんを食べに行こう！")
    elif weather=="light rain"and 13>temperature:
                print("体が温まるおいしいごはんを食べに行こう！")            
    elif weather=="rain"and 13>temperature:
                print("おうちでパーティーをしよう！")
    elif weather=="thunderstorm"and 13>temperature:
                print("外は危ないから家の中でゲームや本を読んでゆっくりしよう！")
    elif weather=="mist"and 13>temperature:
                print("なるべく外に出ないようにしよう！")
    else:
        print("雪遊びで体を動かそう！")
    
else:
    print('天気情報を取得できませんでした')