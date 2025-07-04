import os
import json
import pandas as pd
import subprocess

def get_metadata(file_path, exiftool_path):
    """
    從圖片或影片的元數據中提取所有可用資訊。
    """
    if not os.path.exists(file_path):
        print(f"檔案不存在: {file_path}")
        return None
    
    try:
        result = subprocess.run([exiftool_path, '-json', file_path], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"ExifTool 執行錯誤: {e}")
        return None
    
    if not output.strip():
        print(f"ExifTool 返回空內容，可能是 {file_path} 沒有元數據或命令執行失敗")
        return None
    
    try:
        metadata = json.loads(output)[0]
        return metadata
    except (IndexError, json.JSONDecodeError):
        print(f"解析 {file_path} 的元數據失敗")
        return None

def extract_metadata_from_folder(folder_path):
    """
    批量處理資料夾內的圖片和影片，提取所有元數據並存成 CSV 檔案。
    """
    exiftool_path = "C:/Users/user/Desktop/done/exiftool-13.14_64/exiftool.exe"
    
    if not os.path.exists(folder_path):
        print(f"資料夾不存在: {folder_path}")
        return
    
    data = []
    supported_extensions = {'.jpg', '.jpeg', '.png', '.tif', '.tiff', '.mp4', '.mov', '.avi', '.mkv'}
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in supported_extensions:
                file_path = os.path.join(root, file)
                metadata = get_metadata(file_path, exiftool_path)
                if metadata:
                    metadata["File Name"] = file
                    data.append(metadata)
    
    if data:
        df = pd.DataFrame(data)
        output_csv = os.path.join(folder_path, "alldata.csv")
        df.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"所有元數據已儲存至 {output_csv}")
    else:
        print("未找到任何可用的元數據")

if __name__ == "__main__":
    folder_path = input("請輸入包含圖片或影片的資料夾路徑: ")
    extract_metadata_from_folder(folder_path)
