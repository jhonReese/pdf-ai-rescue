# 🚀 Ultimate AI PDF Rescue Toolkit & Academic Engine V2.0

Reese Wang 的 PDF 救援 toolkit，起因是女友的 iPad 內建的「檔案」發生 OOM，故而建立此工具。結合底層二進位鑑識 (binwalk, qpdf, mupdf) 與 AI 視覺引擎 (Tesseract eng+equ)，專為修復因記憶體溢出、存檔崩潰而損毀的原文書與手寫筆記所設計，同時也為正常學術資料學習。

## 🔥 V2.0 
1. **修復與學習 (--full)**：混合 Logical/Forensic 提取技術，駭客程度的頂級救援PDF，並同時提煉主動學習 AI筆記。
2. **只學習 (--learn-only)**：針對**正常的原文書 (如 Calculus)** ，快速萃取數學定理與Anki高階閃卡csv.。
3. **只修復 (--repair-only)**：純粹使用 binwalk, qpdf, mupdf 進行底層修復，不進行 AI 視覺引擎。


## ⚡ 如何在本機使用一鍵指令
```
### 修復與學習 (--full)：結構全毀損、崩潰的作業
```bash
docker run -it --rm -v "$(pwd):/workspace" reesewang0305/pdf-ai-rescue rescue --full broken.pdf
(我們從二進位屎山中把資料炸出來並救回)

### 只學習 (--learn-only)：正常原文書提煉 (例如 Thomas' Calculus)
```bash
docker run -it --rm -v "$(pwd):/workspace" reesewang0305/pdf-ai-rescue rescue --learn-only Thomas.pdf
(你會成功解鎖所有內嵌圖片與文字)


### 只修復 (--repair-only)：只要修復檔案，不要 AI 
```bash
docker run -it --rm -v "$(pwd):/workspace" reesewang0305/pdf-ai-rescue rescue --repair-only damaged.pdf
