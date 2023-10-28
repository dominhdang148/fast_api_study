# Tự học FASTAPI

## Cài đặt

1. Clone dự án về máy bằng lệnh:

```bash
$ git clone https://github.com/dominhdang148/fast_api_study.git
```

2. Trong thư mục dự án gõ lệnh sau để tạo _môi trường ảo_. (Nếu đã có môi trường ảo rồi thì bỏ qua bước này)

```bash
$ python -m venv env
```

> **Lưu ý:** Sử dụng phiên bản Python 3.10.x để có kết quả chạy chính xác nhất. Cú pháp python shell ở mỗi hệ điều hành có thể khác nhau

3. Khởi động môi trường ảo

```bash
$ source env/bin/activate
(env)$
```

> Nếu sử dụng hệ điều hành Windows:

```bash
> env\Scripts\activate
(env)>
```

4. Thực hiên tải các module, package cần thiết

```bash
$ pip install -r requirements.txt
```

5. Sử dụng uvicorn để chạy server. Mở browser và gõ URL localhost:8000/docs để xem kết quả

```bash
$ uvicorn main:app
```
