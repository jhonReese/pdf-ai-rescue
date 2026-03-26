#!/bin/bash
if [ -z "$1" ]; then
    echo "⚠️ 啟動失敗！請提供目標 PDF 檔案。例如：rescue broken.pdf"
    exit 1
fi

FILE="$1"
BASENAME="${FILE%.pdf}"
EXTRACT_DIR="_${FILE}.extracted"
FINAL_PDF="${BASENAME}_ai_recovered.pdf"

echo "🚀 [啟動頂尖救援與 AI 重組協議] 目標: $FILE"

echo "▶️ 階段 1: 嘗試 qpdf 結構修復..."
qpdf "$FILE" "${BASENAME}_qpdf.pdf" 2>/dev/null

echo "▶️ 階段 2: 啟動 binwalk 二進位深層提取..."
binwalk -e --dd=".*" "$FILE" >/dev/null 2>&1

echo "▶️ 階段 3: 自動修正提取出的圖片副檔名..."
if [ -d "$EXTRACT_DIR" ]; then
    cd "$EXTRACT_DIR"
    for f in *; do 
        if file "$f" | grep -qi "JPEG"; then mv "$f" "${f}.jpg" 2>/dev/null; fi
        if file "$f" | grep -qi "PNG"; then mv "$f" "${f}.png" 2>/dev/null; fi
    done
    cd ..
    
    echo "▶️ 階段 4: 移交 AI 視覺引擎進行特徵分析與無損重組..."
    python3 /usr/local/bin/ai_vision.py "$EXTRACT_DIR" "../$FINAL_PDF"
else
    echo "❌ binwalk 未能建立提取資料夾，檔案可能無實體數據。"
fi

echo "=================================================="
echo "🎯 任務完成！請檢查目錄下的 $FINAL_PDF"
