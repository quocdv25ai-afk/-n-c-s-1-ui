# SmartStudy AI - Ứng dụng Quản lý Học tập

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/Framework-CustomTkinter-green.svg" alt="CustomTkinter">
    <img src="https://img.shields.io/badge/Version-1.0.0-purple.svg" alt="Version">
</p>

> **SmartStudy AI** là ứng dụng desktop được thiết kế để hỗ trợ sinh viên quản lý học tập hiệu quả với giao diện hiện đại, đẹp mắt.

---

## ✨ Tính năng chính

### 📊 Dashboard
- Tổng quan thống kê học tập (GPA, tỷ lệ điểm danh, công việc hoàn thành)
- Lịch học tuần nhanh
- Công việc hôm nay
- Thông báo và nhắc nhở

### 📅 Lịch học
- Xem lịch theo **tuần** hoặc **tháng**
- Chi tiết từng buổi học (thời gian, phòng, loại LT/TH)
- Điều hướng dễ dàng giữa các tuần

### 📝 Quản lý Công việc
- Thêm, sửa, xóa công việc
- Lọc theo: Tất cả, Hôm nay, Tuần này, Đã hoàn thành
- Mức độ ưu tiên (Cao, Trung bình, Thấp)
- Thống kê tiến độ

### 🤖 AI Hỗ trợ
- Chatbot trợ lý học tập 24/7
- Gợi ý câu hỏi nhanh
- Giao diện chat hiện đại

### 👤 Hồ sơ & Cài đặt
- Thông tin cá nhân & học tập
- Cài đặt giao diện (Dark/Light mode)
- Quản lý tài khoản

---

## 📁 Cấu trúc dự án

```
SmartStudyAI/
├── main.py                 # Điểm khởi đầu ứng dụng
├── app.py                  # Class ứng dụng chính
├── requirements.txt        # Thư viện cần thiết
├── README.md               # Tài liệu dự án
│
└── ui/                     # Giao diện người dùng
    ├── __init__.py         # Package init
    ├── sidebar.py          # Thanh menu điều hướng
    ├── dashboard.py        # Trang Dashboard
    ├── schedule.py         # Trang Lịch học
    ├── tasks.py            # Trang Quản lý Task
    ├── ai_chat.py          # Trang AI Chat
    ├── profile.py          # Trang Hồ sơ
    └── widgets.py          # Các component tái sử dụng
```

---

## 🛠️ Cài đặt

### Yêu cầu hệ thống
- **Python**: 3.10 trở lên
- **Hệ điều hành**: Windows 10/11, macOS, Linux

### Các bước cài đặt

#### 1. Clone hoặc tải dự án
```bash
cd "d:/Đồ án cơ sở 1"
```

#### 2. Tạo môi trường ảo (Khuyến nghị)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

#### 4. Chạy ứng dụng
```bash
python main.py
```

---

## 🎨 Giao diện

### Màu sắc chủ đạo
| Màu | Hex Code | Sử dụng |
|-----|----------|---------|
| Tím Gradient | `#667eea` → `#764ba2` | Màu chính, nút bấm |
| Xanh Gradient | `#11998e` → `#38ef7d` | Màu phụ, thành công |
| Cam | `#f59e0b` | Cảnh báo, mức trung bình |
| Đỏ | `#ef4444` | Nguy hiểm, mức cao, lỗi |

### Font chữ
- **Font chính**: Segoe UI (Windows), SF Pro Display (macOS)
- **Font emoji**: Segoe UI Emoji

---

## 👥 Đội ngũ phát triển

| Thành viên | Vai trò | Mô tả |
|------------|---------|--------|
| [Tên sinh viên 1] | Giao diện người dùng | Thiết kế và phát triển UI/UX |
| [Tên sinh viên 2] | Cơ sở dữ liệu | Quản lý dữ liệu và backend |
| [Tên sinh viên 3] | AI Chatbot | Tích hợp trí tuệ nhân tạo |

---

## 📝 Ghi chú cho sinh viên

### Phần giao diện (Đã hoàn thành)
- Dashboard với widgets thống kê
- Lịch học tuần/tháng
- Quản lý công việc (CRUD)
- AI Chat giao diện
- Hồ sơ và cài đặt

### Tích hợp với các module khác
1. **Database Module**: Thêm code kết nối database trong `app.py`
2. **AI Module**: Tích hợp API AI trong `ui/ai_chat.py`

### Cách chạy demo
```bash
# Demo giao diện (không cần database)
python main.py
```

---

## 🐛 Xử lý lỗi thường gặp

### Lỗi: Module not found
```bash
pip install -r requirements.txt
```

### Lỗi: Font hiển thị không đúng
Đảm bảo hệ điều hành có font Segoe UI (Windows) hoặc cài đặt font tương thích.

### Lỗi: Màn hình trắng
Kiểm tra phiên bản Python (cần 3.10+):
```bash
python --version
```

---

## 📄 License

MIT License - Sử dụng tự do cho mục đích học tập.

---

<p align="center">
    Made with ❤️ by SmartStudy Team
</p>
