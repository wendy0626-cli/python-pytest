# -*- coding: utf-8 -*-
__author__ = 'Guibin'

import pytest
import requests
from time import sleep
from api.template_api import TemplateAPI
from tools.get_log import GetLog
from tools.read_file import read_json
import allure

log = GetLog.get_log()

@allure.feature('Test class template')
class TestTemplate:
    session = None

    @classmethod
    def setup_class(cls):
        cls.session = requests.Session()
        cls.template = TemplateAPI()

    @classmethod
    def teardown_class(cls):
        cls.session.close()

    @classmethod
    def setup(cls):
        sleep(1.5)

    '''
    @allure.story("Test method template-add")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_add"))
    def test_add(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_add(self.session, attr1, attr2)
        # 打印日志
        log.info("添加功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"
    '''
    '''
    @allure.story("Test method template-upd")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_upd"))
    def test_upd(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_upd(self.session, attr1, attr2)
        # 打印日志
        log.info("修改功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"
    '''
    @allure.story("Test method template-get")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_get"))
    def test_get(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_get(self.session, attr1, attr2)
        # 打印日志
        log.info("查询功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"

    '''
    @allure.story("Test method template-del")
    @pytest.mark.parametrize(("uid", "success", "expect"), read_json("test_del"))
    def test_del(self, uid, success, expect):
        # 添加功能API调用
        response = self.template.api_del(self.session, uid)
        # 打印日志
        log.info("删除功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"
    '''