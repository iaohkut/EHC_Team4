# EHC_Team4
Steganography Challenge:

Đầu tiên có một file tải về:

![image](https://user-images.githubusercontent.com/93731698/162355869-2cf386cf-ac70-4206-ad5d-9fcb0872b4a7.png)

![image](https://user-images.githubusercontent.com/93731698/162355898-a170dd3f-5002-4a7e-ae18-507f957590f4.png)

Đọc được chiều cao 160 chiều rộng 553

![image](https://user-images.githubusercontent.com/93731698/162355921-c76bffbe-b932-47f0-85ec-41132587f61f.png)

Ta có chiều rộng

![image](https://user-images.githubusercontent.com/93731698/162355955-f0d623f9-448a-474b-b621-dc993347af1c.png)

Ta có chiều cao 

![image](https://user-images.githubusercontent.com/93731698/162355974-b0c7d4f4-9c0b-4994-bab4-6423b0d6fef4.png)

Chỉnh sửa chiều cao lên 01 2C

![image](https://user-images.githubusercontent.com/93731698/162356004-e90c2b38-bc91-4889-bae5-8f98403048a3.png)

![image](https://user-images.githubusercontent.com/93731698/162356026-87852396-d3e4-4497-9e77-2bd5d87c6731.png)

Bắt đầu bằng 1 file PNG sau khi nhìn tới cuối thấy FF D9 mà đây là định dạng của JPG, sau đó mình đoán đó là IEND em nhìn dưới thấy header FF D8 thấy bắt đầu JPG 

![image](https://user-images.githubusercontent.com/93731698/162356071-43ff6d06-d2aa-4f7c-891b-3e7ed07a0dbe.png)

![image](https://user-images.githubusercontent.com/93731698/162356207-2f2800d5-8453-41b6-a9c4-fc4ce368a849.png)

=> Em dự đoán file ảnh này kết hợp 3 file, em tách ra 3 file ( vì đề bài cũng bảo có 3 sercet text )

e xóa từ 82 tới hết bên đầu

![image](https://user-images.githubusercontent.com/93731698/162356242-07b31a86-b16d-4eb9-abc9-5061aeca3da9.png)

tiếp theo tách thành 2 file

![image](https://user-images.githubusercontent.com/93731698/162356258-ec127c2f-edcd-4621-aefd-6b239a6bb1c1.png)

search google thì zip header format phải 50 4B nên sửa lại

![image](https://user-images.githubusercontent.com/93731698/162356280-e10f6c61-20c3-482e-a95e-03716f80fdc1.png)

text2.png là zip nên em đã:

![image](https://user-images.githubusercontent.com/93731698/162356364-0cfaee07-ec8e-47bc-8e33-18484437632c.png)

https://user-images.githubusercontent.com/93731698/157847977-d70732e0-7693-4061-b299-5e3b9feaa82b.png

![image](https://user-images.githubusercontent.com/93731698/162356407-a17e6b1c-3109-4d6c-baf0-b20b512aa9df.png)

![image](https://user-images.githubusercontent.com/93731698/162356426-78373161-3074-4b77-82ef-93d4a10524ae.png)

=> 3 text là: 
+, This is some hidden text
+, Nobody's gonna know
   Never gonna give you up
   This is how secret message can be sent
+, if you don't use stegseek, I recommend it. 




