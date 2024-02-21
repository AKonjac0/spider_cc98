import requests
import json
import openpyxl
import time
import openpyxl.styles
# http://openid-cc98-org-s.webvpn.zju.edu.cn:8001/connect/token?sf_request_type=fetch

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjAzQTg0MkUwMjlENkE2MzQzNUVFNzNDODk5MDI4MkNGMzk5Mzc4QjBSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkE2aEM0Q25XcGpRMTduUEltUUtDenptVGVMQSJ9.eyJuYmYiOjE3MDA5NTcwMjEsImV4cCI6MTcwMDk2MDYyMSwiaXNzIjoiaHR0cHM6Ly9vcGVuaWQuY2M5OC5vcmciLCJjbGllbnRfaWQiOiI5YTFmZDIwMC04Njg3LTQ0YjEtNGMyMC0wOGQ1MGE5NmU1Y2QiLCJzdWIiOiI3MzUzNzYiLCJhdXRoX3RpbWUiOjE3MDA0NDc5NDIsImlkcCI6ImxvY2FsIiwidW5pcXVlX25hbWUiOiJBS29uamFjXyIsIm5hbWUiOiJBS29uamFjXyIsImZvcnVtLnByaXZpbGVnZSI6NCwianRpIjoiNjQ5N0ZBMjg4Q0M4Mjc4NUU0NjIxRUFCM0VBRTgzMjYiLCJpYXQiOjE3MDA0NDc5NDIsInNjb3BlIjpbImNjOTgtYXBpIiwib3BlbmlkIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbIkNDOTgiXX0.hIeHCbulSG3luRAV1sIUr6Y7GuMXGmCFZAYMJzfHt7K_RNff-l9Bqs2oMsJAEqXzHgoK18MGV-A9x4e9TZqRNF0SMpEH48vx0YNvDnB1Tzi3RvmHx54lU95iBl8yNaw6Lq33YD0rCL7IY1VrDmH7a1Pj46rnpjm-DPNU2VVf_C8Cqp3yFUurB1XbYbNJ7qBatX58LFxawFuNqnmgRj03SVXtebBFSInnaGuu7dcztOXIjAsZQdWAEU0kYM1UGO6EAiWXUdHn_noQwWTy0pcUiMsfqAJTUhV3iIKl1x-eJFuF4MuSw0bAggdjrx3OmGx-uVxK24FAJ2pLD3OSQCwvTQ'
}
workbook_name = 'cc98_study_0.xlsx'


def get_time(t0, t1, t2):
    t = t2 - t1
    h = int(t / 3600)
    m = int((t - h * 3600) / 60)
    s = int((t - h * 3600 - m * 60))
    print("section time:" + str(h) + ":" + str(m) + ":" + str(s))
    t = t2 - t0
    h = int(t / 3600)
    m = int((t - h * 3600) / 60)
    s = int((t - h * 3600 - m * 60))
    print("total time:" + str(h) + ":" + str(m) + ":" + str(s))


def work(i, sheet):
    Url = r'http://api-cc98-org-s.webvpn.zju.edu.cn:8001/topic/{}?sf_request_type=fetch'.format(i)
    resp = requests.get(Url, headers=headers)
    html = resp.text
    # print(html)

    if html == "topic_not_exists":
        print(str(i) + ":not exist")
        return
    elif html == "topic_is_deleted":
        print(str(i) + ":deleted")
        return
    try:

        js_html = json.loads(html)
        cnt = int(js_html["replyCount"] / 10)

        tmp = []
        for j in range(0, cnt + 1):
            url = r'http://api-cc98-org-s.webvpn.zju.edu.cn:8001/Topic/{}/post?from={}&size=10&sf_request_type=fetch'.format(
                i, j * 10)
            res = requests.get(url, headers=headers)
            htmls = res.text
            js_htmls = json.loads(htmls)
            for k in range(0, 10):
                try:
                    tmp.append([str(js_htmls[k]["floor"]), js_htmls[k]["content"]])
                except IndexError:
                    continue

        print(str(i) + ":saved")
        sheet.append(['topic', str(i), js_html["title"]])
        row = sheet[sheet.max_row]
        for r in row:
            r.font = openpyxl.styles.Font(name="微软雅黑", size=10, bold=True, italic=False)
        for T in tmp:
            try:
                sheet.append(T)
            except openpyxl.utils.exceptions.IllegalCharacterError:
                print("IllegalCharacter:" + str(T[0]))
                continue

    except json.decoder.JSONDecodeError:
        print(str(i) + ":Authorization Error")
        return


def spider():

    t0 = time.time()
    t1 = time.time()
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'cc98'
    web_url = r'http://api-cc98-org-s.webvpn.zju.edu.cn:8001/board/68?sf_request_type=fetch'
    resp = requests.get(web_url, headers=headers)
    html = resp.text
    js_html = json.loads(html)

    num = int(js_html["topicCount"] / 20)
    for n in range(1261, num + 1):
        web_Url = r'http://api-cc98-org-s.webvpn.zju.edu.cn:8001/board/68/topic?from={}&size=20&sf_request_type=fetch'.format(n * 10)
        resp = requests.get(web_Url, headers=headers)
        html = resp.text
        js_html = json.loads(html)
        try:
            for k in range(0, 20):
                try:
                    work(js_html[k]["id"], sheet)
                except IndexError:
                    continue
        except json.decoder.JSONDecodeError:
            print("topic list Authorization error")
            continue
        if n % 5 == 0:
            workbook.save(workbook_name)
            get_time(t0, t1, time.time())
            t1 = time.time()

    workbook.save(workbook_name)


if __name__ == "__main__":
    spider()