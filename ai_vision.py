import os, glob, re, csv, img2pdf, pytesseract
from PIL import Image
from collections import Counter

TARGET_VOCAB = {"orthogonal", "eigenvalue", "eigenvector", "determinant", "derivative", "integral", "asymptote", "hypothesis", "synthesis", "evaluate", "conjecture", "paradigm", "anomaly"}

def process_and_extract(target_dir, output_pdf):
    print(f"🧠 [AI Vision & NLP] 啟動 10 年超前學術提煉引擎: {target_dir}")
    os.chdir(target_dir)
    images = sorted(glob.glob("*.jpg") + glob.glob("*.png"))
    if not images: return
    
    full_text = ""
    theorems = []
    
    for img_file in images:
        try:
            text = pytesseract.image_to_string(Image.open(img_file), lang='eng+equ')
            full_text += text + "\n"
            for match in re.finditer(r'(?i)(Theorem|Definition|Proof|Lemma)[\s\S]{10,150}(?=\n\n|\Z)', text):
                clean_text = " ".join(match.group().replace('\n', ' ').split())
                theorems.append(clean_text)
            print(f"    ✔️ 深度解析 [{img_file}] 完成")
        except Exception as e:
            print(f"    ❌ 解析 [{img_file}] 失敗: {e}")

    if theorems:
        with open("../Math_Core_Concepts.md", "w", encoding="utf-8") as f:
            f.write("# 📐 自動萃取：核心定理與定義筆記\n\n")
            for t in theorems: f.write(f"> {t}\n\n")
        print("  📚 [NLP 萃取] 數學核心筆記已生成！")

    words = re.findall(r'\b[a-zA-Z]{6,}\b', full_text.lower())
    found_vocab = [w for w in words if w in TARGET_VOCAB or len(w) > 9]
    vocab_counts = Counter(found_vocab)
    
    with open("../GRE_TOEFL_Anki_Deck.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for word, count in vocab_counts.most_common(50):
            writer.writerow([word, f"出現 {count} 次<br><i>PDF AI 引擎生成</i>", "TOEFL_GRE_Auto"])
    print("  🃏 [NLP 萃取] Anki 閃卡牌組 (CSV) 已生成！")

    print("📦 [Auto-Merge] 封裝無損 PDF...")
    with open(output_pdf, "wb") as f: f.write(img2pdf.convert(images))
    print(f"✅ 完美重組！檔案儲存至: {output_pdf}")

if __name__ == "__main__":
    import sys
    process_and_extract(sys.argv[1], sys.argv[2])
