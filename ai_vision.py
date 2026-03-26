import os
import glob
import re
import img2pdf
import pytesseract
from PIL import Image
from collections import Counter

# 模擬高階單字庫 (在此簡單示範，實際運行可擴充)
ADVANCED_VOCAB = {"analyze", "theorem", "matrix", "derivative", "integral", "orthogonal", "eigenvalue", "hypothesis", "synthesis", "evaluate"}

def process_and_merge(target_dir, output_pdf):
    print(f"🧠 [AI Vision & NLP] 啟動本機神經網路分析: {target_dir}")
    os.chdir(target_dir)
    
    images = glob.glob("*.jpg") + glob.glob("*.png")
    if not images:
        print("  ⚠️ 無圖片可處理。")
        return

    images.sort()
    full_text = ""
    
    print("  🔍 正在執行數學矩陣與原文書文本解析...")
    for img_file in images:
        try:
            # 提取文本，包含英文與數學符號包
            text = pytesseract.image_to_string(Image.open(img_file), lang='eng+equ')
            full_text += text + " "
            print(f"    ✔️ 深度解析 [{img_file}] 完成")
        except Exception as e:
            print(f"    ❌ 解析失敗 [{img_file}]: {e}")

    # 創新功能：GRE/TOEFL 單字收割與統計
    words = re.findall(r'\b[a-zA-Z]{5,}\b', full_text.lower())
    found_vocab = [w for w in words if w in ADVANCED_VOCAB or len(w) > 8]
    vocab_counts = Counter(found_vocab)
    
    vocab_file = "../GRE_TOEFL_Vocab_Flashcards.txt"
    with open(vocab_file, "w", encoding="utf-8") as f:
        f.write("=== 🚀 專屬 GRE/TOEFL 學術單字萃取 ===\n")
        f.write("結合你的原文書內容，自動捕捉以下高頻/長篇學術單字：\n\n")
        for word, count in vocab_counts.most_common(20):
            f.write(f"- {word} (出現 {count} 次)\n")
    print(f"  📚 [NLP 萃取成功] 專屬單字卡已生成至 {vocab_file}")

    # 無損 PDF 重組
    print("📦 [Auto-Merge] 封裝無損 PDF...")
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(images))
        print(f"✅ 完美重組！檔案儲存至: {output_pdf}")
    except Exception as e:
        print(f"❌ PDF 重組失敗: {e}")

if __name__ == "__main__":
    import sys
    process_and_merge(sys.argv[1], sys.argv[2])
