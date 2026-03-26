#!/bin/bash
if [ -z "$1" ]; then echo "⚠️ 請提供目標 PDF"; exit 1; fi
FILE="$1"; BASENAME="${FILE%.pdf}"; EXTRACT_DIR="_${FILE}.extracted"; FINAL_PDF="${BASENAME}_ai_recovered.pdf"
echo "🚀 [啟動頂尖救援與 AI 重組協議] 目標: $FILE"
qpdf "$FILE" "${BASENAME}_qpdf.pdf" 2>/dev/null
binwalk -e --dd=".*" "$FILE" >/dev/null 2>&1
if [ -d "$EXTRACT_DIR" ]; then
    cd "$EXTRACT_DIR"
    for f in *; do 
        if file "$f" | grep -qi "JPEG"; then mv "$f" "${f}.jpg" 2>/dev/null; fi
        if file "$f" | grep -qi "PNG"; then mv "$f" "${f}.png" 2>/dev/null; fi
    done
    cd ..
    python3 /usr/local/bin/ai_vision.py "$EXTRACT_DIR" "../$FINAL_PDF"
else
    echo "❌ binwalk 未能建立提取資料夾"
fi
echo "🎯 任務完成！請檢查目錄下的 $FINAL_PDF"
