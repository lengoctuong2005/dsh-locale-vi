# DeepSeek Harness Vietnamese Language Pack (`dsh-locale-vi`)

Gói bản địa hóa Tiếng Việt toàn diện, tự nhiên và chuẩn kỹ thuật cho hệ sinh thái **DeepSeek Harness (DSH Desktop / Tauri / Web)**.

---

## 🌟 Tính Năng Nổi Bật

- **Bản địa hóa 106 Namespaces**: Dịch thuật chuyên sâu toàn bộ giao diện DSH từ trang chủ, thanh tác tử, menu cài đặt, khung chat, popover chọn chuyên gia, quản trị luồng cho đến thông báo lỗi hệ thống.
- **Làm sạch 100% Chuỗi Ngoại Lai**: Quét sạch và loại bỏ hoàn toàn các chuỗi tiếng Trung (CJK), tiếng Pháp, tiếng Tây Ban Nha và các cụm từ tiếng Anh lai tạp.
- **Hỗ trợ 9 Chế Độ Tác Tử (Agent Presets)**:
  - `Standard mode`: Tiêu chuẩn
  - `God mode`: Toàn năng (100% quyền hạn công cụ REA / MCP / Terminal)
  - `Team / Swarm mode`: Đội ngũ đa tác tử
  - `Workflow mode`: Quy trình kiểm định chất lượng (DoD/TDD)
  - `DeepTutor mode`: Học tập & Luyện tập phản biện Socratic
  - `Speed mode`: Siêu tốc (Phản hồi cô đọng, tối ưu độ trễ)
  - `PTC mode`: Gọi công cụ lập trình (Programmatic Tool Calling)
  - `Minimal mode`: Tối giản
  - `Creator mode`: Nhà sáng tạo & Phát triển Plugin
- **Tương Thích Hoàn Hảo Với Đội Ngũ Chuyên Gia (Agency Agents)**: Bản địa hóa toàn bộ thẻ thành viên, huy hiệu và giao diện chọn đồng thời nhiều nhóm chuyên gia (*Multi-Team Selection*).
- **Thiết Kế Cho Cordis Micro-Kernel**: Nạp trực tiếp qua cơ chế `dsh.bundle.patch` và inject client tự động khi ứng dụng khởi động.

---

## 🚀 Cấu Trúc Gói

```text
dsh-locale-vi/
├── client.js          # Từ điển bản địa hóa và bộ điều phối ngôn ngữ client (106 namespaces)
├── index.js           # Điểm nạp plugin cho Cordis Micro-Kernel backend
├── cordis.patch.yml   # Cấu hình patch tích hợp vào DSH
├── package.json       # Khai báo gói và metadata Cordis
├── test-locale.py     # Bộ kiểm tra tự động các chuỗi bản địa hóa cốt lõi
├── test-im.cjs        # Bộ kiểm tra nạp client và cơ chế fallback ngôn ngữ
├── LICENSE            # Giấy phép mã nguồn mở MIT
└── README.md          # Tài liệu hướng dẫn sử dụng
```

---

## 📦 Cài Đặt & Kích Hoạt

### Cách 1: Liên kết trực tiếp vào thư mục Plugins của DSH

1. Sao chép hoặc clone repository vào thư mục plugins của DSH:
   ```bash
   git clone https://github.com/lengoctuong2005/dsh-locale-vi.git ~/.dsh/plugins/dsh-locale-vi
   ```

2. Tạo symlink vào `node_modules` của Desktop Profile:
   ```bash
   ln -sf ~/.dsh/plugins/dsh-locale-vi ~/.dsh/profiles/desktop/node_modules/dsh-locale-vi
   ```

3. Đăng ký plugin vào `~/.dsh/profiles/desktop/cordis.patch.yml`:
   ```yaml
   - id: locale-vi
     name: 'dsh-locale-vi'
   ```

4. Khởi động lại ứng dụng DeepSeek Harness Desktop hoặc Web:
   ```bash
   deepseek-harness-desktop
   ```

---

## 🧪 Kiểm Thử & Xác Minh Chất Lượng

Chạy bộ kiểm thử tự động để xác nhận toàn vẹn cú pháp và chất lượng dịch thuật:

```bash
# Kiểm tra cú pháp JavaScript
node --check client.js
node --check index.js

# Chạy bộ kiểm thử đơn vị
node test-im.cjs
python3 test-locale.py
```

---

## 📄 Bản Quyền & Giấy Phép

Phát hành dưới giấy phép mã nguồn mở [MIT License](LICENSE).  
Bản quyền (c) 2026 **Le Ngoc Tuong** (`taikhoanpubg200@gmail.com`).
