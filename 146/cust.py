import requests
import json
import re
import requests.utils

class CustomerPerson():

    def __init__(self):
        self.lgoin_url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login'
        self.url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/custPersonal/query'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
        self.data = {
            "ageNum": 1,
            "pageSize": 10,
            "_actionLoaction": "",
            "_actionMuneId": "RES10768",
            "_selectTabName": "",
            "_buttonName": "",
            "location_url": "",
        }
        self.lgoin_data = {
            "loginUriSuffix": "",
            "username": "506025",
            "password" :"MC40NjE4MDM3NjUyNTk3OTkwNV9tc2RwXzFfbXNkcF90eXBlPTE="
        }

    def test_login(self):
        s = requests.session()
        login_response = s.post(self.lgoin_url, data=self.lgoin_data, headers=self.headers)
        # print(login_response.request.headers["Cookie"])
        cookie = requests.utils.dict_from_cookiejar(s.cookies)
        print(cookie)
        response = s.get(self.url, cookies=cookie, headers=self.headers)
        # print(response.text)
        return response

    def get_person_info(self):
        response_json = json.loads(self.test_login().text)
        # print(response_json,type(response_json))
        with open("客户信息.txt", "w", encoding="utf-8") as f:
            for i in response_json["data"]["grid"]["list"]:
                f.write(i["cstNm"] + "," + i["crdtNo"] + "\n")


if __name__ == '__main__':
    c = CustomerPerson()
    c.get_person_info()
    # c.test_login()