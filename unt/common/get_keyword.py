import jsonpath


class GetKeyword:

    @staticmethod
    def get_value_by_keyword(data, keyword, index):
        return jsonpath.jsonpath(data, f"$..{keyword}")[index]  # 源数据，表达式，返回单个

    @staticmethod
    def get_values_by_keyword(data, keyword):
        return jsonpath.jsonpath(data, f"$..{keyword}")  # 源数据，表达式，返回多个
