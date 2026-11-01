import requests
import json
import time
import os
from requests.exceptions import ReadTimeout, HTTPError, RequestException

def fetch(urls, hosts = "www.bing.com", num = 50):
    url = urls

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Host": hosts,
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0"
    }

    if not os.path.exists("data") :
        os.mkdir("data")
        print("创建data文件夹!")
    if not os.path.exists("images"):
        os.mkdir("images")
        print("创建images文件夹!")

    print("="*17+f"开始爬取:{url}"+"="*17)

    for i in range(0, num, 1):
        time.sleep(1.7)
        try:
            response = requests.get(url, headers=headers, timeout=5.0)
            print(f"状态码{response.status_code}")

            if response.status_code == 200:
                print(f"请求成功{response.status_code}!")

                if len(response.text) < 20:
                    print("网站拦截!")
                    print(response.text)

                elif len(response.text) >= 20:
                    print("开始解析")

                    try:
                        data = response.json()
                        print("json解析成功!")
                        print(data)

                        file_name = time.strftime("%Y%m%d_%H%M%S")
                        with open(f"data/bilibili_{file_name}.json","w",encoding="utf-8") as f:
                            f.write(json.dumps(data, ensure_ascii=False, indent=4))
                        print(f"数据以保存到data/{file_name}.json.")
                        break

                    except Exception as e:
                        print("json解析错误,输出文本")
                        data = response.text
                        print(data[:500] if len(data) > 500 else data)
                        break
                    
        except ReadTimeout:
            print("连接超时!")
        except HTTPError:
            print("HTTP异常!")
        except RequestException:
            print("请求异常!")
        except Exception as e:
            print(f"未知错误")

    print("=" * 17 + " 爬取结束 " + "=" * 17)

if __name__ == "__main__":
    url = input("url:")
    go_url = input("go_url:")
    if go_url == "":
        go_url = "www.bing.com"
        print("默认使用bing.com。")
    fetch(url, go_url)
    #fetch("https://api.bilibili.com/x/web-interface/view?bvid=BV1Da4y1N7su", "api.bilibili.com")
