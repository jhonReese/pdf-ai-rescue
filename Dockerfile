FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y qpdf ghostscript binwalk file mupdf-tools python3 python3-pip python3-venv tesseract-ocr tesseract-ocr-eng wget && rm -rf /var/lib/apt/lists/*
RUN TESSDATA_DIR=$(find /usr/share -name tessdata -type d | head -n 1) && wget -q https://github.com/tesseract-ocr/tessdata/raw/main/equ.traineddata -P "$TESSDATA_DIR"
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install --no-cache-dir img2pdf pytesseract Pillow
WORKDIR /workspace
COPY rescue.sh /usr/local/bin/rescue
COPY ai_vision.py /usr/local/bin/ai_vision.py
RUN chmod +x /usr/local/bin/rescue
CMD ["/bin/bash"]
