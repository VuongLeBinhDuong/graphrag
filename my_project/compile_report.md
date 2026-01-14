# Hướng Dẫn Biên Dịch Báo Cáo LaTeX

## Yêu Cầu

Cần cài đặt LaTeX distribution:
- **Windows**: MiKTeX hoặc TeX Live
- **Linux**: `sudo apt-get install texlive-full` hoặc `sudo yum install texlive-scheme-full`
- **Mac**: MacTeX

## Cách Biên Dịch

### Windows (PowerShell)

```powershell
# Với MiKTeX
pdflatex report.tex
pdflatex report.tex  # Chạy lại lần 2 để tạo references

# Hoặc dùng TeX Live
xelatex report.tex
xelatex report.tex
```

### Linux/Mac

```bash
# Với pdflatex
pdflatex report.tex
pdflatex report.tex

# Hoặc với xelatex (hỗ trợ tiếng Việt tốt hơn)
xelatex report.tex
xelatex report.tex
```

## Output

File PDF sẽ được tạo ra: `report.pdf`

## Lưu Ý

- File sử dụng package `babel` với Vietnamese và English
- Nếu gặp lỗi về font tiếng Việt, có thể:
  1. Sử dụng `xelatex` thay vì `pdflatex`
  2. Hoặc comment dòng `\usepackage[vietnamese,english]{babel}` và chỉ dùng English

## Quick Compile Script

Tạo file `compile.bat` (Windows) hoặc `compile.sh` (Linux/Mac):

### Windows (compile.bat)
```batch
@echo off
pdflatex report.tex
pdflatex report.tex
del *.aux *.log *.out
echo Done! Check report.pdf
```

### Linux/Mac (compile.sh)
```bash
#!/bin/bash
pdflatex report.tex
pdflatex report.tex
rm *.aux *.log *.out
echo "Done! Check report.pdf"
```

Sau đó chạy:
- Windows: `.\compile.bat`
- Linux/Mac: `chmod +x compile.sh && ./compile.sh`


