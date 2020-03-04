#coding: utf-8
import requests
from config.read_config import ReadConfig
import urllib3
urllib3.disable_warnings()


class Login():
    rc = ReadConfig(r"D:\Users\Raymond\PycharmProjects\bokeyuan0229\config\config.ini")
    base_url = rc.get_url("base_url")
    #获取首页cookies
    def add_cookies(self):
        url =self.base_url + "/signin"
        headers ={"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        s = requests.session()
        r = requests.get(url,headers=headers,verify=False)
        #print(r.text)
        # print(s.cookies)
        # print(s)
        #添加登录返回的cookies
        c = requests.cookies.RequestsCookieJar()
        c.set('.CNBlogsCookie', '36DC5EC587B07D1883CAD0751A9AE0C1B3F625EB638FDFBFD35EA0C8B4DA5DF78686CA6086ADA26C4291BFE97939E93FBE15A243DF632BD3E21C9926D0E2F26F852239E75DB2A902460BB0DE3789279DA81A50EF; expires=Sun, 15 Mar 2020 09:00:18 GMT; domain=.cnblogs.com; path=/; httponly')
        c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Nf-Z6tqUPlNrwu2nvfTJEg-1gCJfCJMIpTjdQv6_KY-n74sRUQII00bRhSHBJHnTnnWmNKEhO_L0IxRqly1wC_oGDqVYgQNyvEumhj1fqZGXQilcJ4NvCWqFzY2-JS4lIjJb4Drf9trBCk0GdDYXKjAhu15bwRPhmZaIuSWek_t07jydxKQU0PBxEm9K7k7VDwK_X5Vtv4ZoHFEwmJn5dMUDy3V3PzfbR-Kvxgg5ectN5ojAMWUs6eH8pNTHmja6kEBKc8jfTyigJOMJlK9ouej0JIo8SLYBp4M_SP1JsPcnxoOYLG89Tr_SeTfPj7aLaVdfQTrRiAZbs6Q_TiG6kjpbA7EOYv_0BTTso0eZKEYT9UKYyKGL5T5jjD_GN7HEB_mISGQhiCFwbj00M0VDbS1kMlNR2085qMXQLqp-UnlSwrseFFvD2W5jP58AO1ySgS8Ubo3cal7OrmeIqWCiXMOGgv9qmwSBfzQXctgf4GDvnctFOYYmd7I0lO6blzVeoTJ7us9HdD7JAbh8p8VJaWQXpAi-0c4mFWWymdDc2oD907mNlkD-J7nTL_vG1Z5hw; expires=Sun, 15 Mar 2020 09:00:18 GMT; domain=.cnblogs.com; path=/; httponly')
        c.set('AlwaysCreateItemsAsActive',"True")
        c.set('AdminCookieAlwaysExpandAdvanced',"True")
        s.cookies.update(c)
        # print (s.cookies)
        # print(s)
        return s.cookies
        # url2 = base_url + "/user/CurrentUserInfo?_=1582970534138"
        # r1 = requests.get(url2, headers=headers,verify=False)
        # print(r1.content)



if __name__ == '__main__':
    login = Login()
    login.add_cookies()
    # get_userinfo()




