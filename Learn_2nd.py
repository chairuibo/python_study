import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text[0:1000]
    except:
        return "出现异常！！"

if __name__ == "__main__":
    url="https://www.baidu.com"
    print(getHTMLText(url))