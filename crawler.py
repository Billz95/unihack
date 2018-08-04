import requests
from bs4 import BeautifulSoup
import json

url = "http://www.jbhifi.com.au"
# UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"

HA = {"Host": "products.jbhifi.com.au",
    "Connection" : "keep-alive",
      "Content-Length" : "144",
    "Accept" : "*/*",
    "Origin" : "https://www.jbhifi.com.au",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "DNT" : "1",
    "Content-Type" : "application/json; charset=UTF-8",
    "Referer" : "https://www.jbhifi.com.au/",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "en-AU,en;q=0.9,zh;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6",
"Cookie" : "_ga=GA1.3.716774373.1533401505; _gid=GA1.3.1608953892.1533401505; __insp_wid=1014521198; __insp_slim=1533404486085; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuamJoaWZpLmNvbS5hdS8%3D; __insp_targlpt=SkIgSGktRmkgfCBKQiBIaS1GaSAtIEF1c3RyYWxpYSdzIExhcmdlc3QgSG9tZSBFbnRlcnRhaW5tZW50IFJldGFpbGVy; __insp_norec_sess=true; ADRUM=s=1533407626659&r=https%3A%2F%2Fwww.jbhifi.com.au%2F%3F0; _dc_gtm_UA-917980-2=1"}

header = HA


def get_id (a, b):
    jb_session = requests.Session()
    # jb_session.get(url,headers=header)
    # print(jb_session.headers)

    # ids = []
    # for i in range(a, b):
    #     ids.append('"' + str(i) + '"')
    ids = [
    "880873",
    "881891",
    "883123",
    "870428",
    "884202",
    "830326",
    "881893",
    "868359",
    "888662",
    "863509",
    "812335",
    "870198",
    "881233",
    "887260",
    "820000000"
  ]

    postData = { "Ids" : ids }
    print(JSON.dumps(postData))

    f = jb_session.post("https://products.jbhifi.com.au/product/get/id", data = jsonify.jsonify(postData), headers=header)
    print(f.content)

get_id(800080,800090)
