import datetime
import json
import requests

def format_date(timestamp_obj):
    from datetime import datetime
    datetime_obj = datetime.fromtimestamp(timestamp_obj)
    return str(datetime_obj)




def get_data(url):
    response = requests.get(url,headers={"User-agent":"your bot 0.1"})
    print(response)

    python_obj = json.loads(response.text)
    news = python_obj["data"]["children"]
    filter_data = []
    num = 1
    for new in news:
        news_date = {
            f"New:{num}":{
                "title":new["data"]["title"],
                "author":new["data"]["author"],
                "created":format_date(new["data"]["created"])
            }
        }

        filter_data.append(news_date)
        num +=1

    return filter_data

def write_to_json(date):
    with open("RadditNews.json","w") as file:
        json.dump(date,file,indent=4)


def main(url):
    date = get_data(url)
    write_to_json(date)


main("https://www.reddit.com/r/gadgets/.json")



""""
Alloha
"""
