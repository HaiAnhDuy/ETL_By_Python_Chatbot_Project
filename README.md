# Tên Dự Án

Chatbot Truy Cứu Thông Tin Chuyển Khoản

## Giới Thiệu

Đây là dự án xây dựng chatbot với mục đích tra cứu tên,số tiền,nội dung chuyển khoản bằng mã giao dịch.Dự án được xây dựng khi mà Mặt Trận Tổ Quốc Việt Nam (MTTQVN) công bố file sao kê cứu trợ đồng bào Miền Bắc trong khuôn khổ khắc phục thiệt hại do bão só 3.Dữ liệu mà dự án này sử dụng là file sao kê lần thứ nhất.

## Kiến Trúc

![image](https://github.com/user-attachments/assets/39b5eec7-2978-4bdf-924b-534dab6b07b7)

## Về Code

### File main.py

- Giải quyết những vấn đề sau:
  + Đọc file pdf (sử dụng thư viện tabula)
  + Xử lý và chuẩn hóa dữ liệu
  + Phân tích dữ liệu quan trọng
  + Lưu dữ liệu dưới dạng CSV
  + Tải lên Amazon S3

## Hướng Dẫn Sử Dụng

1.Truy cập [Chatbot Kiểm Tra Độ Liêm](https://www.facebook.com/profile.php?id=61565706104968&sk=friends_likes) để có thể sử dụng chatbot.
2.Bạn có thể test bằng cách bấm vào nút "Message"
![image](https://github.com/user-attachments/assets/0f9c3c43-b934-46c8-a863-130983873878)
3.Nhập từ 'check var' và đợi phản hồi
![image](https://github.com/user-attachments/assets/fc2c204a-c9db-4071-bcfd-7ce624d8ae5b)
4.Làm theo lời chatbot gửi 'y' để tiếp tục cuộc trò chuyện
![image](https://github.com/user-attachments/assets/2ad533dc-e896-475e-8e70-b4ed051b9aff)
5.Lưu ý bạn có thể chọn ngẫu nhiên mã trong [FILE SAO KÊ](https://github.com/HaiAnhDuy/ETL_By_Python_Chatbot_Project/blob/master/sao-ke.pdf) (Bắt đầy từ page 2).Khi nhập mã giao dịch bạn nên bỏ dấu chấm ngăn cách ở giữa
![image](https://github.com/user-attachments/assets/d7f4bd91-faa7-4e53-a29d-40fee5fed490)
6.Ví Dụ
![image](https://github.com/user-attachments/assets/512703ea-3a3d-46b0-bd6c-9cbc9b89e405)

![image](https://github.com/user-attachments/assets/c480401c-d552-4a80-b05c-5a72c585d57f)


