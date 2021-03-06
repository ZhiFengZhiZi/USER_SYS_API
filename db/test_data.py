import sys,time
sys.path.append('../db_fixture')
from db.mysql_db import DB
from db.mysql_db_2 import DB as DB2
from common import urlbase



# Inster table datas
def ua_emp_insert(count):
    table = 'ua_employee'
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    try:


        if  count==1:
            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.close()

        elif  count==2:

            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
               'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}



            emp2 = {'EMP_NO':'99992','EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
           'EMP_STATUS': '1', 'CELL_PHONE': '1010123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()

        elif count == 9:
            table_name = table
            emp = {'EMP_NO': '99991', 'EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2',
                   'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                   'EMP_STATUS': '0', 'CELL_PHONE': '9898123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            emp2 = {'EMP_NO': '99992', 'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1',
                    'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                    'EMP_STATUS': '1', 'CELL_PHONE': '1010123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()
    except Exception as err:
        return  err
    finally:
        return "good"

def ua_emp_search(value,type):
    semp = {'EMP_CNAME': '测试账号α'}
    semp2 = {'EMP_CNAME': '测试账号β'}
    table_name = "ua_employee"


    if   type=='α':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp)
        db.close()
    elif type == 'β':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp2)
        db.close()
    return s

def ua_emp_delete(type,id):
    table_name = "ua_employee"
    table_name2 = "ua_online_employee"
    table_name3 ="ua_logon_log"
    table_name4 = 'ua_operation_log'
    data = {'EMP_CNAME': '测试账号α'}
    data2 = {'EMP_CNAME': '测试账号β'}
    data_id = {'EMP_ID': id}
    data_id2 = {'EMP_ID': id}
    data_id3 = {'EMP_ID': id}

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name4, table_data=data_id3)
        db.clear(table_name=table_name2, table_data=data_id)
        db.clear(table_name=table_name3, table_data=data_id2)
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name4, table_data=data_id3)
        db.clear(table_name=table_name2, table_data=data_id)
        db.clear(table_name=table_name3, table_data=data_id2)
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_role_insert(count):
    table_name = "ua_role"
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if count==1 :
        role = {'ROLE_CODE': 'ROLE01', 'ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA', 'STATUS': '1','UPDATE_TIME':nowtime}
        db = DB()
        db.insert(table_name=table_name, table_data=role)
        db.close()


    elif count==2 :
        role = {'ROLE_CODE': 'ROLE01', 'ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA',
                'STATUS': '1','UPDATE_TIME':nowtime}
        role2 = {'ROLE_CODE': 'ROLE02', 'ROLE_NAME': '测试角色β', 'PINYIN': 'BETA',
                 'STATUS': '1','UPDATE_TIME':nowtime}
        db = DB()
        db.insert(table_name=table_name, table_data=role)
        db.insert(table_name=table_name, table_data=role2)
        db.close()

def ua_role_search(value, type):
    semp = {'ROLE_NAME': '测试角色α'}
    semp2 = {'ROLE_NAME': '测试角色β'}
    table_name = "ua_role"

    if type == 'α':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp)
            db.close()
    if type == 'β':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp2)
            db.close()

    return s

def ua_role_delete(type):
    data = {'ROLE_NAME': '测试角色α'}
    data2 = {'ROLE_NAME': '测试角色β'}
    table_name = "ua_role"

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_res_insert(count):
    table_name = "ua_resource"

    if count == 1:
            role = {'RES_NAME':'测试管理α','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            db = DB()
            db.insert(table_name=table_name, table_data=role)
            db.close()

    if count == 2:
            role = {'RES_NAME':'测试管理α','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            role2 = {'RES_NAME':'测试管理β','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            db = DB()
            db.insert(table_name=table_name, table_data=role)
            db.insert(table_name=table_name, table_data=role2)
            db.close()

def ua_res_search(value, type):
        semp = {'RES_NAME': '测试管理α'}
        semp2 = {'RES_NAME': '测试管理β'}
        semp3 = {'id': value}
        table_name = "ua_resource"

        if type == 'α':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp)
            db.close()
        if type == 'β':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp2)
            db.close()

        if type =='id':

            db = DB()

            s = db.select(table_value='RES_NAME', table_name=table_name, table_data=semp3)
            db.close()

        return s

def ua_res_delete(type):
    data = {'RES_NAME': '测试管理α'}

    data2 = {'RES_NAME': '测试管理β'}
    table_name = "ua_resource"

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_roleemp_insert(empid,roleid):
    table_name = "ua_role_emp"
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    data = {'EMP_ID':empid,'ROLE_ID':roleid,'STATUS':1,'UPDATE_TIME':nowtime}
    db = DB()
    db.insert(table_name=table_name, table_data=data)
    db.close()

def ua_roleemp_delete(EMP_ID):
    data = {'EMP_ID':EMP_ID}

    table_name = "ua_role_emp"

    db = DB()
    db.clear(table_name=table_name, table_data=data)
    db.close()


def ua_resurls_delete(res_id):
    data = {'RES_ID': res_id}
    table_name = "ua_resource_urls"

    db = DB()
    db.clear(table_name=table_name,table_data=data)
    db.close()

def ua_resauth_delete(res_id):
    data = {'RES_ID': res_id}
    table_name = "ua_role_authorize"

    db = DB()
    db.clear(table_name=table_name,table_data=data)
    db.close()


def dtb_clause_inser(count):
    table_name = "prd_clause"
    clause = {'NAME':'测试用大地下条款α','INSURER_ID':'2','INS_TYPE_ID':'1','DESCRIPTION':'1','CONTENT':'4',
              'OPERATOR':'admin','MS':'0'}
    clause2 = {'NAME': '测试用大地下条款β', 'INSURER_ID': '2', 'INS_TYPE_ID': '1', 'DESCRIPTION': '1', 'CONTENT': '4',
              'OPERATOR': 'admin','MS':'0'}

    if count==1 :
        db = DB2()
        db.insert(table_name=table_name, table_data=clause)
        db.close()


    elif count==2 :

        db = DB2()
        db.insert(table_name=table_name, table_data=clause)
        db.insert(table_name=table_name, table_data=clause2)
        db.close()


def dtb_clause_search(value, type):
    sclause = {'NAME': '测试用大地下条款α'}
    sclause2 = {'NAME': '测试用大地下条款β'}
    table_name = "prd_clause"

    if type == 'α':
            db = DB2()

            s = db.select(table_value=value, table_name=table_name, table_data=sclause)
            db.close()
    if type == 'β':
            db = DB2()

            s = db.select(table_value=value, table_name=table_name, table_data=sclause2)
            db.close()

    return s


def dtb_clause_delete(type):
    sclause = {'NAME': '测试用大地下条款α'}
    sclause2 = {'NAME': '测试用大地下条款β'}
    table_name = "prd_clause"

    if type == 'α':
        db = DB2()
        db.clear(table_name=table_name,table_data=sclause)
        db.close()

    elif type == 'β':
        db = DB2()
        db.clear(table_name=table_name, table_data=sclause2)
        db.close()


def ua_org_insert(count):
    table_name = "ua_org"
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if count == 1:
            org = {'ID':'77798','PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门','CREATE_TIME': nowtime,'STATUS':1
                ,'UPDATE_TIME':nowtime,'OPERATOR':'aotutest' }
            #
            db = DB()
            db.insert(table_name=table_name, table_data=org)
            db.close()

    if count == 2:
            org = {'ID': '77798', 'PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门', 'CREATE_TIME': nowtime, 'STATUS': 1
            , 'UPDATE_TIME': nowtime, 'OPERATOR': 'aotutest'}
            org2 = {'ID': '77799', 'PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门', 'CREATE_TIME': nowtime, 'STATUS': 1
            , 'UPDATE_TIME': nowtime, 'OPERATOR': 'aotutest'}
            db = DB()
            db.insert(table_name=table_name, table_data=org)
            db.insert(table_name=table_name, table_data=org2)
            db.close()

    if count == 3:
            org = {'ID': '77797', 'PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门', 'CREATE_TIME': nowtime, 'STATUS': 1
            , 'UPDATE_TIME': nowtime, 'OPERATOR': 'aotutest'}
            org2 = {'ID': '77798', 'PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门', 'CREATE_TIME': nowtime, 'STATUS': 1
            , 'UPDATE_TIME': nowtime, 'OPERATOR': 'aotutest'}
            org3 = {'ID': '77799', 'PARENT_ID': '3', 'ORG_NAME': '系统研发中心测试部门', 'CREATE_TIME': nowtime, 'STATUS': 1
                , 'UPDATE_TIME': nowtime, 'OPERATOR': 'aotutest'}
            db = DB()
            db.insert(table_name=table_name, table_data=org)
            db.insert(table_name=table_name, table_data=org2)
            db.insert(table_name=table_name, table_data=org3)
            db.close()


def ua_org_search(value, type):
        semp = {'RES_NAME': '测试管理α'}
        semp2 = {'RES_NAME': '测试管理β'}
        semp3 = {'id': value}
        table_name = "ua_resource"

        if type == 'α':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp)
            db.close()
        if type == 'β':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp2)
            db.close()

        if type =='id':

            db = DB()

            s = db.select(table_value='RES_NAME', table_name=table_name, table_data=semp3)
            db.close()

        return s


def ua_org_delete(id):
    sorg = {'id': id}
    table_name = "ua_org"


    db = DB()
    db.clear(table_name=table_name,table_data=sorg)
    db.close()



if __name__ == '__main__':
    dtb_clause_inser(count=1)
    s=dtb_clause_search(value='NAME',type='α')


    print(s)