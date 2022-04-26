### Challenge web-basic: http://18.162.149.167/

Đầu tiên chúng ta dùng burpsuite để bắt gói tin requests.

![web1](https://user-images.githubusercontent.com/77691959/165356954-40e22adc-564d-45f0-9033-9089c4a0c01c.png)

Nó bảo rằng phải vào api "/ehc", nên chúng ta sửa GET của nó, đồng thời thêm Referer headers.

![web2](https://user-images.githubusercontent.com/77691959/165357709-86346098-35aa-4fa1-8a79-15d72bbdcf3c.png)

Tiếp theo nó yêu cầu mình phải truy cập url này bằng 'EHC' browser, nên chúng ta đổi User-Agent headers thành "EHC".

![web3](https://user-images.githubusercontent.com/77691959/165358140-5c66e23e-afe7-4cd8-a8f1-d7375bc37f48.png)

Tiếp theo, chúng ta nhận được một tin nhắn "WE CANNOT BE TRACKED!", sau một lúc tìm kiếm trên mạng thì biết được rằng phải thêm DNT headers.

![web4](https://user-images.githubusercontent.com/77691959/165359122-a6693b5a-27e6-457d-b25a-40bec86ed085.png)

Theo đó chúng ta thấy được tin nhắn tiếp theo có đề cập đến ngôn ngữ và cụ thể đây là Japanese.\
Vậy nên có thể đổi Accept-Language headers thành "ja".

![web5](https://user-images.githubusercontent.com/77691959/165360080-64d77668-2ffa-43f1-b8a2-fdf2f5a64c25.png)

Tiếp đó, chúng ta nhận được tin nhắn liên quan đến thời gian và ở đây nó đề cập đến "Year".\
Vậy chúng ta cần phải thêm Date headers, và năm thành lập EHC là 2017.

![web6](https://user-images.githubusercontent.com/77691959/165361449-f0702307-f5e8-4116-b036-7e5be4728ee5.png)

Yeahhhhhhhhhhh, flag here.

Source code:
```python
import requests

url = "http://18.162.149.167/ehc"
headers = {
    "Host": "18.162.149.167",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "EHC",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ja",
    "Connection": "close",
    "Referer": "http://18.162.149.167",
    "DNT": "1",
    "Date": "2017"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text)
```

### Flag: ehc{n3v3r_g0nn4_g1v3_y0u_uP}
