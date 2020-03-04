#coding = utf-8
import requests
import api.api_login
import config

class UserInfo():
    rc = config.read_config.ReadConfig(r"D:\Users\Raymond\PycharmProjects\bokeyuan0229\config\config.ini")
    base_url = rc.get_url("base_url")
    def get_userinfo(self):
        url = self.base_url + "/user/CurrentUserInfo?_=1582970534138"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        s = requests.session()
        l = api.api_login.Login()
        c = l.add_cookies()
        # print(c)
        s.cookies.update(c)
        # print(s.cookies)
        r = s.get(url,headers = headers,verify=False)
        # print(r.content)
        return r.content


if __name__ == '__main__':
    userinfo = UserInfo()
    userinfo.get_userinfo()