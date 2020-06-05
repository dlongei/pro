import unittest
from interface.sel import Select_name
from common.get_keyword import GetKeyword


class Test_select(unittest.TestCase):
    def setUp(self):
        self.selectname = Select_name()

    def test_select_data(self):
        # data = {
        #         "commonName": "肺宁颗粒",
        #         "storeName": "",
        #         "pageIndex": 1,
        #         "pageSize": 10
        #          }
        data = None    # 参数直接放到URL里
        response = self.selectname.selectname(data)

        commonname = GetKeyword.get_value_by_keyword(response, "commonName", 0)
        self.assertEquals(commonname, "肺宁颗粒")


if __name__ == '__main__':
    unittest.main()
