import requests
from requests_hustauth import HustAuth

def query_courses(Uname:str, Upass:str, kcmc:str) -> list:
    session = requests.Session()
    hust_auth = HustAuth(Uname,Upass)
    
    url_loign = 'http://mhub.hust.edu.cn/cas/login?redirectUrl=/wyckController/queryCourseList'
    session.get(url_loign, auth=hust_auth)

    url_queryCourseList = f'http://mhub.hust.edu.cn/wyckController/queryCourseList?kcmc={kcmc}'
    resp = session.get(url_queryCourseList, auth=hust_auth)

    return resp.json()
