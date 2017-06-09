import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_updateResStatus_info(unittest.TestCase):
    ''' 删除资源详情接口 '''

    def setUp(self):
        test_data.ua_res_insert(1)
        test_data.ua_emp_insert(1)
        self.emp=test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.emp,roleid=1)
        self.s1=test_data.ua_res_search('id','α')


        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/res/updateResStatus"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数_all'''
        payload = {"resId":self.s1,'status':0}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)

        time.sleep(1)

    def test_status_incorrect(self):
        ''' 错误的参数_状态值'''
        payload = {"resId":self.s1,'status':9}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)


        time.sleep(1)


    def test_id_incorrect(self):
        ''' 错误的参数_不存在的id'''
        payload = {"resId":99089,'status':0}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)


    def test_id_null_incorrect(self):
        ''' 错误的参数_空的id'''
        payload = {"resId":"",'status':0}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)


    def test_status_null_incorrect(self):
        ''' 错误的参数_空的status'''
        payload = {"resId":self.s1,'status':''}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)


    def tearDown(self):


        test_data.ua_roleemp_delete(EMP_ID=self.emp)
        test_data.ua_emp_delete(type='β')
        test_data.ua_res_delete('α')

        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()