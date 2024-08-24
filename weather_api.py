import requests

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
service_key = "lqXYf9dWTudG4St6mupVVd/j6xC6zUaeTNuHKY2KoJgbXgervy9MdGi9WK4P0xiCaeEKlzcXF5hO8ahIV5R3bA=="

# 웹 요청시 같이 전달될 데이터 = 요청 메시지
params = {
    'serviceKey' : service_key,
    'numOfRows' : 30,
    'pageNo' : 1,
    'dataType' : 'JSON',
    'base_date' : '20240823', # 오늘 날짜
    'base_time' : '1400', # 요청 가능 발표 시간
    'nx' : 48, # 샘플 지역
    'ny' : 84 # 샘플 지역
}

res = requests.get(url=url , params=params)
print(res.status_code, type(res.text), res.url)
print()
print(res.text)