from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver


    def click(self, loc):
        self.find_element(loc).click()

    def send_keys(self, loc, text):
        self.find_element(loc).send_keys(text)

    # 自定义函数，调用系统函数，只是重名而已
    def find_element(self, loc):
        # return self.driver.find_element(loc[0], loc[1])
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath_with_feature(loc_value)

        return WebDriverWait(self.driver, 10, 2).until(lambda x:x.find_element(loc_by, loc_value))

    def find_elements(self, loc):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath_with_feature(loc_value)

        return WebDriverWait(self.driver, 10, 2).until(lambda x: x.find_elements(loc_by, loc_value))


    # xpath工具类
    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and"
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"

        return feature


    # xpath工具类
    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and")

        loc = feature_start + feature + feature_end

        return loc