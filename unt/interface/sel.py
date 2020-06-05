from common.send_method import Sendmethon
from common.get_keyword import GetKeyword
import jsonpath


class Select_name:

    def __init__(self, method='post'):
        #  参数直接放到URL里
        self.url = "http://122.226.7.83:8002/ztc-corp-api/admin/modules/jxc/drug/stock/getListByPage?commonName=%E8%82%BA%E5%AE%81%E9%A2%97%E7%B2%92&storeName=&pageIndex=1&pageSize=10"
        self.method = method

    def selectname(self, data):  # 先登录获取token，再按名称查询
        # 登录系统，获取token
        url = "http://122.226.7.83:8002/ztc-corp-api/account/login?loginName=ztc_corp&loginPwd=123456&accountType=1"
        method = "post"
        r = Sendmethon.send_method(method=method, url=url)
        to = jsonpath.jsonpath(r, "$..token")[0]
        headers = {"Content-Type": "application/json;charset=UTF-8",
                   "token": to
                   }

        # 发送查询请求
        response = Sendmethon.send_method(method=self.method, url=self.url, headers=headers, data=data)
        return response

    def getname(self, data):  # 获取查询结果name值
        response = self.selectname(data)
        commonname = GetKeyword.get_value_by_keyword(response, "commonName", 0)
        return commonname

