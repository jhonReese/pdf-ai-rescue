# 採用 2026 穩定版 Ubuntu 作為基底
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# 安裝底層救援工具、Python 環境與 Tesseract AI OCR 引擎 (包含繁中與數學方程式包)
RUN apt-get update && apt-get install -y \
    qpdf ghostscript binwalk file mupdf-tools \
    python3 python3-pip python3-venv \
    tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-eng tesseract-ocr-equ \
    && rm -rf /var/lib/apt/lists/*

# 建立虛擬環境並安裝 Python 套件
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install --no-cache-dir img2pdf pytesseract Pillow

WORKDIR /workspace

# 複製並賦予執行權限
COPY rescue.sh /usr/local/bin/rescue
COPY ai_vision.py /usr/local/bin/ai_vision.py
RUN chmod +x /usr/local/bin/rescue

CMD ["/bin/bash"]
