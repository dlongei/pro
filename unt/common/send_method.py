import requests
import json
import jsonpath


class Sendmethod:

    @staticmethod
    def send_method(method, url, params=None, data=None, headers=None):
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=params)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, json=data, headers=headers)  # files=data, data=data
        else:
            print("请求方式错误！")
            response = None
        if method == "delete":
            return response.status_code  # delete方法返回数据类型
        else:
            return response.json()  # 返回类型

    @staticmethod
    def format_responss(response):
        return json.dumps(response, indent=2, ensure_ascii=False)


# if __name__ == '__main__':
#
#     # 登录
#     url = "http://122.226.7.83:8002/ztc-corp-api/account/login?loginName=ztc_corp&loginPwd=123456&accountType=1"
#     method = "post"
#     r = Sendmethon.send_method(method=method, url=url)
#     print(Sendmethon.format_responss(r))
#
#     # 查询
#     url = "http://122.226.7.83:8002/ztc-corp-api/admin/modules/jxc/drug/stock/getListByPage?commonName=%E8%82%BA%E5%AE%81%E9%A2%97%E7%B2%92&storeName=&pageIndex=1&pageSize=10"
#     method = "post"
#     to = jsonpath.jsonpath(r, "$..token")[0]  #
#     # to = r["data"]["token"]  # 从返回值的字典中获取token
#     # json = {"commonName": "肺宁颗粒",
#     #         "storeName": "",
#     #         "pageIndex": 1,
#     #         "pageSize": 10
#     #         }
#     headers = {"Content-Type": "application/json;charset=UTF-8",
#                "token": to}
#     res = Sendmethon.send_method(method=method, url=url, headers=headers)
#     print(Sendmethon.format_responss(res))
