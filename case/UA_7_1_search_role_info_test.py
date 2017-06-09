import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_search_role_info(unittest.TestCase):
    ''' 查询角色详情接口 '''

    def setUp(self):

        test_data.ua_emp_insert(count=1)
        test_data.ua_role_insert(count=1)
        self.emp = test_data.ua_emp_search(value='id',type='β')
        self.s1 = test_data.ua_role_search(value='id',type='α')
        test_data.ua_roleemp_insert(empid=self.emp, roleid=1)
        test_data.ua_role_insert(1)


        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/getRoleInfoList"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数_id'''
        payload = {"roleid":self.s1}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], "测试角色α")

        time.sleep(1)


    def test_incorrect_id(self):
        ''' 错误的参数_不存在的id'''

        payload = {"roleid":99999}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)
        time.sleep(1)



    def test_incorrect_null(self):
        ''' 错误的参数_null'''

        payload = {"roleid": None}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)

        time.sleep(1)


    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.emp)
        test_data.ua_emp_delete(type='β')
        test_data.ua_role_delete('α')


        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()