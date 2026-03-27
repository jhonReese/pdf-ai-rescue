import os, glob, re, csv, img2pdf, pytesseract
from PIL import Image
from collections import Counter


TARGET_VOCAB = {"orthogonal", "eigenvalue", "eigenvector", "determinant", "derivative", "integral", "asymptote", "limit", "convergence", "matrix", "hypothesis", "synthesis", "evaluate", "conjecture", "paradigm"}

def process_and_extract(target_dir, output_pdf, skip_merge=False):
    print(f"🧠 [AI Vision & NLP V2.0] 啟動本機提煉引擎: {target_dir}")
    os.chdir(target_dir)
    images = sorted(glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.pnm"))
    if not images: return
    
    full_text = ""
    theorems = []
    
    for img_file in images:
        try:
            
            text = pytesseract.image_to_string(Image.open(img_file), lang='eng+equ')
            full_text += text + "\n"
            
            
            for match in re.finditer(r'(?i)(Theorem|Definition|Proof|Lemma)[\s\S]{10,250}(?=\n\n|\Z)', text):
                clean_text = " ".join(match.group().replace('\n', ' ').split())
                theorems.append(clean_text)
                
            print(f"    ✔️ 深度解析 [{img_file}] 完成")
        except Exception as e:
            print(f"    ❌ 解析失敗 [{img_file}]: {e}")

    # Output 1
    if theorems:
        with open("../Math_Core_Concepts.md", "w", encoding="utf-8") as f:
            f.write("# 📐 V2.0 自動萃取：核心定理與定義筆記\n\n")
            for t in theorems: f.write(f"> {t}\n\n")
        print("  📚 [NLP 萃取] 數學核心概念筆記已生成！")

    # Output 2
    words = re.findall(r'\b[a-zA-Z]{6,}\b', full_text.lower())
    found_vocab = [w for w in words if w in TARGET_VOCAB or len(w) > 9]
    vocab_counts = Counter(found_vocab)
    
    with open("../GRE_TOEFL_Anki_Deck.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for word, count in vocab_counts.most_common(70):
            writer.writerow([word, f"出現 {count} 次<br><i>Reese's PDF AI V2.0 生成</i>", "Phase1_Target"])
    print("  🃏 [NLP 萃取] Anki 閃卡牌組 (CSV) 已生成！")

    # Output 3
    if not skip_merge:
        print("📦 [Auto-Merge] 封裝無損 PDF...")
        try:
            
            clean_images = sorted(glob.glob("*.png") + glob.glob("*.jpg"))
            if clean_images:
                with open(output_pdf, "wb") as f:
                    f.write(img2pdf.convert(clean_images))
                print(f"✅ 完美重組！檔案儲存至: {output_pdf}")
        except Exception as e: print(f"❌ PDF 合併失敗: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3: print(" Usage: ai_vision.py <dir> <out_pdf> [--skip-merge]")
    else:
        skip_merge = "--skip-merge" in sys.argv
        process_and_extract(sys.argv[1], sys.argv[2], skip_merge)
