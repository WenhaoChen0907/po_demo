import os,sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_data_with_file
import pytest
import allure


def data_with_key(key):
    return yml_data_with_file("search_data")[key]


class TestSearch:
    
    """
    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("content", data_with_key("test_search"))
    # @pytest.mark.parametrize("content", yml_data_with_file("search_data")["test_search"])
    def test_search(self, content):
        # 点击搜索
        self.search_page.click_search()
        # 输入文字
        self.search_page.input_text(content)
        # 点击返回
        self.search_page.click_back()

    """

    @allure.step(title="登录测试")
    def test_01(self):
        allure.attach('输入账号', '测试账号有：1， 2,3')
        print("pass")
        allure.attach('输入密码', '密码有：1， 2,3')
        print("pass")
        assert 0
     
