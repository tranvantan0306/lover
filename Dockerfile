# Sử dụng hình ảnh cơ sở có sẵn với Python
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tệp requirements.txt vào thư mục làm việc của Docker
COPY requirements.txt .

# Cài đặt các gói từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép tất cả các tệp từ thư mục hiện tại vào thư mục /app trong Docker
COPY . .

# Mở cổng 3100
EXPOSE 3100

# Lệnh để chạy ứng dụng Python
CMD ["python", "main.py"]
