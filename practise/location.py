import requests  
import json  
  
s = requests.session()  
url = 'http://api.map.baidu.com/highacciploc/v1?qcip=139.214.254.47&qterm=pc&ak=YourKey&coord=bd09ll&extensions=3'  
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}  
response = s.get(url, headers = header, timeout = 20)  
print(response.text)  
  
json = json.loads(response.text)  
  
print('位置：'+str(json['content']['formatted_address']))  
print('商圈：'+str(json['content']['business']))  
print('经度：'+str(json['content']['location']['lat']))  
print('维度：'+str(json['content']['location']['lng']))  
print('准确度：'+str(json['content']['confidence']))