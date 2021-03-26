import requests
import re
import json
import datetime

def save_data(data,name):
    f = open(f"{name}.txt","w",encoding='utf-8')
    f.write(data)
    f.close
    return 'Save Ok!'

def get_data(id):
    url = "https://www.joox.com/th/chart/"+str(id)
    payload={}
    headers = {
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie': 'user_lang=en; user_region=us'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


list_options = [
    "[42] Thailand Top 100",
    "[44] Top 50 International",
    "[73] Top Karaoke Hits",
    "[46] Top 50 ลูกทุ่ง | ไทบ้าน",
    "[47] Top 50 K-Pop",
]

for list_option in list_options:
    print(list_option)

response = get_data(int(input("ID Chart : ")))

matchs = re.findall(r"\"application\/json\">(.*)<\/script><script nomodule=\"\"",response.text)

list_music_json = json.loads(matchs[0])

list_music = list_music_json['props']['pageProps']['trackList']['tracks']['items']

list_music_all = ""

n = 1
for item in list_music:
    # print(f"[{n}]{item['name']} - {item['artist_list'][0]['name']}")
    if (n == 1):
        list_music_all += (f"{n}|{item['name']}|{item['artist_list'][0]['name']}|{item['album_name']}")
    else:
        list_music_all += ("\n"+f"{n}|{item['name']}|{item['artist_list'][0]['name']}|{item['album_name']}")
    n +=1


print(save_data(list_music_all,'data'))

