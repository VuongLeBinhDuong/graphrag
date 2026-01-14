# Hướng Dẫn Sử Dụng Trên Overleaf

## Cách Khắc Phục Lỗi Font Tiếng Việt

### Phương Pháp 1: Sử Dụng XeLaTeX (Khuyến nghị)

1. **Upload file** `report_overleaf.tex` lên Overleaf
2. **Đổi Compiler**:
   - Click vào menu **Menu** (góc trên bên trái)
   - Chọn **Compiler** → **XeLaTeX**
   - Hoặc click vào **Settings** → **Compiler** → chọn **XeLaTeX**
3. **Compile** lại document

### Phương Pháp 2: Sử Dụng pdfLaTeX với T5 Encoding

Nếu không có XeLaTeX, sửa file như sau:

1. **Comment** các dòng XeLaTeX:
```latex
% \usepackage{fontspec}
% \usepackage{xunicode}
% \usepackage{xltxtra}
% \setmainfont{Latin Modern Roman}
```

2. **Uncomment** các dòng pdfLaTeX:
```latex
\usepackage[utf8]{inputenc}
\usepackage[vietnamese,english]{babel}
\usepackage[T5]{fontenc}
```

3. **Đổi Compiler** về **pdfLaTeX**
4. **Compile** lại

### Phương Pháp 3: Chỉ Dùng Tiếng Anh (Đơn giản nhất)

Nếu vẫn gặp vấn đề, có thể tạo phiên bản chỉ tiếng Anh:

1. Comment dòng babel Vietnamese:
```latex
% \usepackage[vietnamese,english]{babel}
\usepackage[english]{babel}
```

2. Dịch các phần tiếng Việt sang tiếng Anh

## Các Bước Trên Overleaf

### Bước 1: Tạo Project Mới
1. Đăng nhập vào [Overleaf](https://www.overleaf.com)
2. Click **New Project** → **Upload Project**
3. Upload file `report_overleaf.tex`

### Bước 2: Cấu Hình Compiler
1. Click **Menu** (góc trên bên trái)
2. Chọn **Settings**
3. Trong phần **Compiler**, chọn **XeLaTeX**
4. Click **Save**

### Bước 3: Compile
1. Click nút **Recompile** (hoặc Ctrl + Enter)
2. Kiểm tra PDF output

## Troubleshooting

### Lỗi: "Font not found"
- **Giải pháp**: Thay `\setmainfont{Latin Modern Roman}` bằng font có sẵn:
  - `Times New Roman`
  - `Arial`
  - `Helvetica`
  - Hoặc bỏ dòng này để dùng font mặc định

### Lỗi: "Package fontspec Error"
- **Giải pháp**: Đảm bảo đã chọn **XeLaTeX** compiler, không phải pdfLaTeX

### Lỗi: "Undefined control sequence"
- **Giải pháp**: Kiểm tra xem có comment/uncomment đúng các package không

### PDF không hiển thị tiếng Việt
- **Giải pháp**: 
  1. Đảm bảo đã chọn XeLaTeX
  2. Kiểm tra font có hỗ trợ tiếng Việt
  3. Thử font khác: `\setmainfont{Times New Roman}`

## Font Khuyến Nghị Cho Overleaf

Các font sau thường có sẵn và hỗ trợ tốt tiếng Việt:
- `Latin Modern Roman` (mặc định)
- `Times New Roman`
- `Arial`
- `Helvetica`

## Quick Fix Template

Nếu muốn nhanh, copy đoạn này vào đầu file:

```latex
% Overleaf XeLaTeX Template
\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}  % Hoặc font khác có sẵn
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=2.5cm}
% ... rest of packages
```

## Liên Hệ Hỗ Trợ

Nếu vẫn gặp vấn đề:
1. Kiểm tra log file trên Overleaf (click **Logs and output files**)
2. Xem error messages chi tiết
3. Thử compile với file mẫu đơn giản trước


