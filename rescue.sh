#!/bin/bash

# V2.0 世界級智慧 PDF 救援與學術提煉選擇器

MODE="$1"
FILE="$2"
BASENAME="${FILE%.pdf}"
EXTRACT_DIR="_${FILE}.extracted"
FINAL_PDF="${BASENAME}_recovered_v2.pdf"

print_usage() {
    echo "=========================================================="
    echo "🚀 Ultimate AI PDF Rescue & Academic Engine V2.0"
    echo "=========================================================="
    echo "Usage: rescue <MODE> <FILE.pdf>"
    echo ""
    echo "MODES:"
    echo "  --full         (修復與學習) 嘗試合併 Logical/Forensic 提取並生成 AI 筆記"
    echo "  --repair-only (只修復) 只用 qpdf 修復結構，不進行圖片提取或 AI 分析"
    echo "  --learn-only  (只學習) 假設檔案健康，用 Logical 提取生成 AI 筆記，不重組合併 PDF"
    echo "=========================================================="
}

# 嚴謹的參數檢查
if [[ -z "$MODE" || -z "$FILE" ]]; then
    print_usage
    exit 1
fi

if [[ ! -f "$FILE" ]]; then
    echo "❌ 啟動失敗！找不到目標 PDF 檔案: $FILE"
    exit 1
fi

echo "🚨 [啟動 V2.0 協議] 模式: $MODE | 目標: $FILE"

# ==========================================
# 模式執行邏輯
# ==========================================

case "$MODE" in
    "--repair-only")
        echo "▶️ 階段 1: 執行 qpdf 底層結構修復..."
        qpdf "$FILE" "${BASENAME}_repaired_only.pdf" 2>/dev/null
        echo "🎯 修復完成！請檢查目錄下的 ${BASENAME}_repaired_only.pdf"
        ;;

    "--learn-only")
        mkdir -p "$EXTRACT_DIR"
        echo "▶️ 階段 1: 執行智慧解鎖 (Mutool Logical Assets Extraction)..."
        # Thomas' Calculus 這裡就會成功解鎖所有內嵌圖片與文字
        mutool extract "$FILE" -p "$EXTRACT_DIR" >/dev/null 2>&1
        
        # 移交 Python Brain，並跳過最後的 PDF 合併重組
        python3 /usr/local/bin/ai_vision.py "$EXTRACT_DIR" "../$FINAL_PDF" --skip-merge
        echo "🎯 學術提煉完成！請檢查 GRE 閃卡與數學筆記檔。"
        ;;

    "--full")
        # 這是最嚴謹、整合度最高的模式
        echo "▶️ 階段 1: 嘗試合併 qpdf 結構修復..."
        qpdf "$FILE" "${BASENAME}_qpdf_fixed.pdf" 2>/dev/null

        mkdir -p "$EXTRACT_DIR"
        echo "▶️ 階段 2: 執行混合提取協議 (Logical & Forensic)..."
        
        # 1. 先用鎖匠指令 (Healthy PDFs)
        mutool extract "$FILE" -p "$EXTRACT_DIR" >/dev/null 2>&1
        
        # 2. 再用破壞剪指令 (Corrupted OOM PDFs)
        binwalk -e --dd=".*" "$FILE" -C "$EXTRACT_DIR" >/dev/null 2>&1
        
        echo "▶️ 階段 3: 圖片格式標準化..."
        cd "$EXTRACT_DIR"
        for f in *; do 
            if file "$f" | grep -qi "JPEG"; then mv "$f" "${f}.jpg" 2>/dev/null; fi
            if file "$f" | grep -qi "PNG"; then mv "$f" "${f}.png" 2>/dev/null; fi
        done
        cd ..

        # 移交 Python Brain
        python3 /usr/local/bin/ai_vision.py "$EXTRACT_DIR" "../$FINAL_PDF"
        echo "🎯 任務完成！已修復 PDF 並生成所有學術提煉檔。"
        ;;

    *)
        echo "❌ 錯誤：不正確的模式: $MODE"
        print_usage
        exit 1
        ;;
esac
