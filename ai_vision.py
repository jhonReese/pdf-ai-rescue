import os
import glob
import pytesseract
import img2pdf
from PIL import Image

def analyze_and_merge(target_dir, output_pdf):
    print(f"🧠 [AI Vision] 正在掃描目錄: {target_dir}")
    os.chdir(target_dir)
    
    # 尋找所有提取出來的圖片
    images = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")
    if not images:
        print("  ⚠️ 找不到任何圖片碎片，跳過合併與辨識。")
        return

    print(f"  🔍 發現 {len(images)} 張碎片，啟動 OCR 與數學特徵辨識...")
    
    image_data = []
    for img_file in images:
        try:
            # 載入圖片並使用繁體中文+英文+數學方程式模型進行辨識
            img = Image.open(img_file)
            # 配置 tesseract: chi_tra(繁中) + eng(英文) + equ(數學公式)
            text = pytesseract.image_to_string(img, lang='chi_tra+eng+equ').strip()
            
            # 創新亮點：根據提取出的文字長度或特定關鍵字作為權重排序的基礎
            # 這裡我們記錄下檔案與其 AI 提取的特徵文字
            image_data.append({
                "file": img_file,
                "text": text,
                "text_length": len(text)
            })
            print(f"    ✔️ 辨識完成 [{img_file}] - 擷取字數: {len(text)}")
        except Exception as e:
            print(f"    ❌ 辨識失敗 [{img_file}]: {e}")
            image_data.append({"file": img_file, "text": "", "text_length": 0})

    # 智慧排序：預設先以檔名排序，若未來需要根據微積分/線性代數邏輯排序，可在此擴充 NLP 邏輯
    image_data.sort(key=lambda x: x['file'])
    
    # 將圖片路徑抽出來準備合併
    sorted_files = [data["file"] for data in image_data]
    
    print("📦 [Auto-Merge] 正在將碎片無損重組為健康 PDF...")
    try:
        # 使用 img2pdf 進行無損位元組層級的封裝，保留原始畫質
        pdf_bytes = img2pdf.convert(sorted_files)
        with open(output_pdf, "wb") as f:
            f.write(pdf_bytes)
        print(f"✅ 完美！已成功合併 {len(sorted_files)} 張碎片至 {output_pdf}")
    except Exception as e:
        print(f"❌ 合併失敗: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 ai_vision.py <target_directory> <output_pdf>")
    else:
        analyze_and_merge(sys.argv[1], sys.argv[2])
