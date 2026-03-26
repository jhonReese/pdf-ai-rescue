# 🚀 Ultimate AI PDF Rescue Toolkit & Academic Engine

這不只是一個 PDF 救援工具，這是一座超前世界的**「主動學習型基礎設施」**。
Reese Wang 的 PDF 救援 toolkit，起因是女友的 iPad 內建的「檔案」發生 OOM，故而建立此工具。結合底層二進位鑑識 (binwalk, qpdf) 與 AI 視覺引擎 (Tesseract OCR)，專為修復因記憶體溢出、存檔崩潰而損毀的原文書與手寫筆記所設計。

## 🔥 獨家殺手級功能 (World-Class Features)
1. **二進位深層提取**：無視 PDF 目錄結構毀損，從檔案的Spaghetti code中暴力提煉出所有圖層與筆記。
2. **AI 無損重組**：自動判讀碎片的排列順序，無損重組為完美的高畫質 PDF。
3. **數學定理自動萃取 (Theorem Extractor)**：自動掃描微積分、線性代數文本，將 Theorem、Definition、Proof 等關鍵字段落獨立匯出為 Markdown 筆記。
4. **大考單字收割 (Anki Deck Generator)**：自動過濾文本中的簡單單字，精準捕捉 GRE/TOEFL 的高頻學術單字，並直接匯出為 Anki 可讀的 CSV 閃卡組。

## ⚡ 如何使用 (最精簡分享版)
只要你的電腦裝有 Docker，完全不用懂程式，打開終端機，執行以下唯一一行指令即可完成一切 (請將「你的壞掉檔案.pdf」替換成你自己的檔名)：

```bash
docker run -it --rm -v "$(pwd):/workspace" jhonreese/pdf-ai-rescue rescue 你的壞掉檔案.pdf
執行完畢後，資料夾內會自動生成：修復好的 PDF、單字閃卡 CSV、以及數學核心筆記。
