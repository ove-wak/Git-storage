import xlrd
import requests
import json
my_headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Access-Control-Allow-Origin': '*',
    'Connection':'keep-alive',
    'Content-Length':'70',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'JSESSIONID=62464859B62D2E5BA50FCCF378AC39FD; .ASPXAUTH1=60070DE9C7F817435961D3429B190424F959A7D6B5943332CA247D274CCB8799F5CDCB1258F2D42B04B84C30E03C709F700332CA86224C46CBD37CFC5AF128901BBCC0820563D10A0FAEAC1D78AE081CCAE16917CF65B8FD48F2EE135AA5749C4CDC789907C15D66E1C70B090375EA93C037A6E482F06E90FB8C61265532B5A01F89EDC9066DA97DBF23296D3F4EF6DFEF3E80056AF1C8EE54A3CB1454A7E39E5B4444FD8B348FC74B61C1C4A8E64D66F5DE05912C38257E5681EE117E80DF5CBEB0EC3B8648EE22726421602A69D0F6DD4FEB702251C03E0FB2288D9E7F56FC4477CC16; JSESSIONID=69C110BA7F806C563B3C2DEE62278EFC',
    'Host':'mydorm.whu.edu.cn',
    'Origin':'http://mydorm.whu.edu.cn',
    'Referer':'http://mydorm.whu.edu.cn/ihome/freshman/query_bunk_by_userCardId',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
# sss     = requests.Session()
url = 'http://210.42.121.246:80/ihome/freshman/get_bunk_by_userCardId'
# print(my_headers)
# datat = xlrd.open_workbook(r'C:\Users\wak\Documents\Tencent Files\835447773\FileRecv\2017全日制学生.xlsx')
# table = datat.sheets()[0]
# nrows =  table.nrows
# for i in range(nrows):
#     print(table.row_values(i))

# print(table.row_values(2)[3])
# print(table.row_values(2)[0])
params = {
   'userCardId' : '2017282110213',
   'userName' : '王安康',
   'CSRFToken' : '85e52b5b-9d44-4b37-adcc-42567870c0da'
}
json_params = json.dumps(params)
# headers = {'content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
cookies = {"JSESSIONID":"25ADF3B209D5B0375D519FBC25FEF5BF",
             ".ASPXAUTH1":"60070DE9C7F817435961D3429B190424F959A7D6B5943332CA247D274CCB8799F5CDCB1258F2D42B04B84C30E03C709F700332CA86224C46CBD37CFC5AF128901BBCC0820563D10A0FAEAC1D78AE081CCAE16917CF65B8FD48F2EE135AA5749C4CDC789907C15D66E1C70B090375EA93C037A6E482F06E90FB8C61265532B5A01F89EDC9066DA97DBF23296D3F4EF6DFEF3E80056AF1C8EE54A3CB1454A7E39E5B4444FD8B348FC74B61C1C4A8E64D66F5DE05912C38257E5681EE117E80DF5CBEB0EC3B8648EE22726421602A69D0F6DD4FEB702251C03E0FB2288D9E7F56FC4477CC16"}
re = requests.post(url, data = json_params, headers = my_headers)
# re = requests.get('http://httpbin.org/get?name=wak&n=1')
print(re.status_code)
print(re.headers)
print(re.text)

#第一个错误 眼瞎地址看错
#第二个错误 返回203 跨域请求失败
