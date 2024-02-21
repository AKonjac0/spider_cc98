import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6IjAzQTg0MkUwMjlENkE2MzQzNUVFNzNDODk5MDI4MkNGMzk5Mzc4QjBSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkE2aEM0Q25XcGpRMTduUEltUUtDenptVGVMQSJ9.eyJuYmYiOjE3MDA5MDMwODUsImV4cCI6MTcwMDkwNjY4NSwiaXNzIjoiaHR0cHM6Ly9vcGVuaWQuY2M5OC5vcmciLCJjbGllbnRfaWQiOiI5YTFmZDIwMC04Njg3LTQ0YjEtNGMyMC0wOGQ1MGE5NmU1Y2QiLCJzdWIiOiI3MzUzNzYiLCJhdXRoX3RpbWUiOjE3MDA0NDc5NDIsImlkcCI6ImxvY2FsIiwidW5pcXVlX25hbWUiOiJBS29uamFjXyIsIm5hbWUiOiJBS29uamFjXyIsImZvcnVtLnByaXZpbGVnZSI6NCwianRpIjoiNjQ5N0ZBMjg4Q0M4Mjc4NUU0NjIxRUFCM0VBRTgzMjYiLCJpYXQiOjE3MDA0NDc5NDIsInNjb3BlIjpbImNjOTgtYXBpIiwib3BlbmlkIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbIkNDOTgiXX0.DghUNt3eFyuCTgkvfkqnJS4peQkKqP5UFJjMbukiJJma_-nQWvGxcVsThTkFNqtKV15HM-e33APpOSbDTkc_Qv6ZbtSY5qsjoXgji54WwaL7IoWrPLKORaR0uTIhgz7Yk2Jfj9ufGpxEIX9Kfbv2DNPqh8pqG6BjqKM_lt_1l1UGHVxpnr_ntF6R-uX9memD2Q3xvRH7mY5ZH8C4jYlfX7e0ouct_t515Eg3DtZpsuQZXz9T_ROCT0XSWcYohcUHGRaLlMU85v-xA9mkbCBMEwg1Qwv5x0RkJ_NAmbrkIR13gJODCup-n3aAahnuKFYjkPVlQzjyj5ObWmQG3vwq0g',
    'Cookie':"lang=zh-CN; _pm0=6M52ijUpdeIm448kYxkLhibnZz0gNCSa6NPmgqci4WE%3D; _ga=GA1.3.302578037.1696553050; HMACCOUNT_-_hm.baidu.com=E2AED51B271A32FC; HMACCOUNT_BFESS_-_hm.baidu.com=E2AED51B271A32FC; Hm_lvt_8ac2f3a56ae6c3341b2d041c3c86e69d_-_chalaoshi.de=1697079088; cf_clearance_-_chalaoshi.de=_jakDtV9ESj.kTUYpoVGSU7zjvYCl5ARXf0U09JhYPY-1697079087-0-1-dc9a8254.f04ad9ea.8b9bddb4-0.2.1697079087; Hm_lvt_0ccdb69da7dc24fdfbd452186f767da6_-_nesa.zju.edu.cn=1697036630,1697100341; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1698235424; iPlanetDirectoryPro=fvcxrP30VEAgKDMwWUPyK4G%2BOCQRLziX9gfu0tlEvB9DRkm0YWfnOhA9Crni5hq7%2FBp1PghbZYNSve%2FANFh8VvR41iAOGLkszz8E2oNmntRYi1C5bJXna0mJV%2FmEAAZT9MWy%2F4FZRw%2BVo5ite%2FLS5tedUQlDKQx3SKER2t2aGVOAV57TZEHroq%2FNpXM2mnawbH%2FfYnG%2BskU3GskzDB%2BUoEMHlHnvSW4CpOYZWswGtSkCBXT8c%2BlsAyTZKGyKM9AtlRazEjjWFBWDJSmhRZ2fJdzixiFahElmQccL8PG1hcOTZxc%2FvLXuGyGwnG6Jh2xObKk30eXI1VTW7vs0pBAyxz5xLpGvCg58dlZVr1Gi3yfKkSy2MREVI6%2F7g9%2FrIbOk; TWFID=a7ba490106e5e8f8"


}
body = json.dumps({"UserName": "AKonjac_", "Password": "AKonjac_050419"})


        # token = jsonpath(res.json(), "$..access_token")[0]

Url = r'http://api-cc98-org-s.webvpn.zju.edu.cn:8001/board/68/topic?from=0&size=20&sf_request_type=fetch'
res = requests.post(url=Url, headers=header)
# ret = requests.post(Url, headers=header)
print(res)
# resp = requests.get(Url, headers=headers)
# html = resp.text
# print(html)
