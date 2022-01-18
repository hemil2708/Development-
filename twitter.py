import scrapy
import requests
from scrapy.http import HtmlResponse
from scrapy.cmdline import execute
import json
import pandas as pd
class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['www.example.com']
    start_urls = ['http://www.example.com/']

    def parse(self,response):
        lol = []
        try:
            url = "https://twitter.com/i/api/graphql/I5nvpI91ljifos1Y3Lltyg/UserByRestId?variables=%7B%22userId%22%3A%222425151%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"

            payload = {}
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-IN,en;q=0.9',
                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'content-type': 'application/json',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                'x-guest-token': '1483418809587609600',
                'Cookie': 'guest_id=v1%3A164250964413447407; guest_id_ads=v1%3A164250964413447407; guest_id_marketing=v1%3A164250964413447407; personalization_id="v1_pkBMNGpbngkGhKIqINGj6Q=="'
            }

            res = requests.get(url, headers=headers, data=payload)
            data = json.loads(res.text)
            username = data['data']['user']['result']['legacy']['name']
            des = data['data']['user']['result']['legacy']['description']
            location = data['data']['user']['result']['legacy']['location']
            display_url = data['data']['user']['result']['legacy']['entities']['url']['urls'][0]['display_url']
            joining_date = data['data']['user']['result']['legacy']['created_at']
            following = data['data']['user']['result']['legacy']['friends_count']
            followers = data['data']['user']['result']['legacy']['followers_count']
            profile_baner_url = data['data']['user']['result']['legacy']['profile_banner_url']
            profile_pic_url = data['data']['user']['result']['legacy']['profile_image_url_https']
            user_id = data['data']['user']['result']['id']
            item = {}
            item['Id'] = user_id
            item['Username'] = username
            item['Description'] = des
            item['Location'] = location
            item['Display_Url'] = display_url
            item['Joining_Date'] = joining_date
            item['Following'] = following
            item['followers'] = followers
            item['Profile_banner_Url'] = profile_baner_url
            item['Profile_pic_url'] = profile_pic_url
            lol.append(item)
            df = pd.DataFrame(lol)
            df.to_csv("Twitter.Csv", index=True)
            print("Csv created")
        except Exception as e:
            print()


if __name__ == '__main__':
    execute("scrapy crawl twitter".split())