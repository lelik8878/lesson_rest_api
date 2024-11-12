import requests

data_to_send = {'name': 'Johan', 'price': 38, 'image': r'E:\content\products\little_one\003\detail_001.webp'}
file_to_send = open(r'E:\content\products\little_one\003\detail_001.webp', 'rb') #file_to_send картинка, которую будем отправлять, rb- бинарный режим
files = {'image': file_to_send}

first_query = requests.post('http://127.0.0.1:8000/api/save_to_db/', data=data_to_send, files=files)
file_to_send.close()
print(first_query)
