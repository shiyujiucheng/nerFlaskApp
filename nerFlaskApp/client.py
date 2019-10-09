#coding=utf-8
import json
import requests

if __name__ == '__main__':

    s = requests

    data = {"sentences": "[['成','都','住','宿', '费','能','报','销','吗','，','我','是','资','阳','的','员','工']]"}
    data = json.dumps(data)
    r = s.post('http://127.0.0.1:5000/nerapi', data)

    print(r.status_code)
    print(r.text)