# Lesson 1

## Tổng quan:

FastAPI là một microframework hiện đại, hiệu suất cao để xây dựng web API với ngôn ngữ Python 3.8+ dựa trên các tiêu chuẩn của Python, giúp code ít hơn, triển khai nhanh hơn và hổ trợ docs API đầy đủ.  
FastAPI phù hợp cho một dự án cần triển khai trong thời gian ngắn nhưng vẫn đảm bảo đầy đủ các yếu tố đi kèm.  
**Các tính năng chính:**

- **Nhanh (Fast)** Theo [FastAPI document](https://fastapi.tiangolo.com/), FastAPI có tốc độ ngang bằng so với NodeJs và Go.
- **Triển khai nhanh (Fast to code)** Tăng tốc độ triển khai các tính năng từ 200% đến 300%
- **Ít lỗi hơn (Fewer bugs)** Giảm khoảng 40% lỗi do lập trình viên gây ra
- **Trực quan và tiện dụng (Intuitive)** Được nhiều trình chỉnh sửa hỗ trợ, có thể chạy trên nhiều nền tảng khác nhau. Tốn ít thời gian gỡ lỗi hơn (hưởng lợi từ Python là một ngôn ngữ thông dịch)
- **Dễ dàng tiếp cận (Easy)** FastAPI dễ học, sử dụng và triển khai, giúp tiết kiệm thời gian đọc tài liệu
- **Code ngắn gọn (Short)** FastAPI giúp giảm thiểu trùng lặp code _(code duplication)_. Nhiều tính năng đã được triển khai sẵn, giúp giảm thiểu bugs
- **Mạnh mẽ (Robust)** Code sẵn sàng cho môi trường production và API docs _(Swagger)_ được sinh tự động.

## Setup dự án

### 1. Phiên bản

FastAPI hỗ trợ `python 3.8+`

### 2. Tạo môi trường ảo

Để phát triển 1 dự án Python, việc thiết lập một môi trường ảo là cần thiết, giúp cho việc cài đặt các Python packages (Kể cả phiên bản) mà không ảnh hưởng đến các dự án Python khác.

Sử dụng venv để tạo môi trường ảo

```bash
$ python -m venv env
```

Kích hoạt môi trường ảo:

```bash
$ source env/bin/activate
```
