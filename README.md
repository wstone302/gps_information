# 提取 GPS 元數據工具

## 簡介
本工具使用 `ExifTool` 提取圖片或影片的所有元數據，並將其存儲到 CSV 檔案中。該工具可批量處理指定資料夾內的所有圖片與影片，支援多種格式，如 JPG、PNG、MP4、MOV 等。

## 需求環境
- Conda 環境
- Python 3.x
- `exiftool`（已內嵌於 `./exiftool-13.14_64/exiftool.exe`）
- `pandas`（用於 CSV 生成）

## 安裝與設定
### 1. 建立 Conda 環境並安裝必要 Python 套件
確保已安裝 Conda，然後執行以下指令：
```sh
conda create -n gps_exif_env python=3.8 -y
conda activate gps_exif_env
pip install pandas
```

### 2. 下載 `ExifTool`
確保 `ExifTool` 已下載並存放於 `./exiftool-13.14_64/exiftool.exe`。

## 使用方法
### 1. 切換至專案目錄並執行 Python 腳本
```sh
cd /path/to/gps_information
conda activate gps_exif_env
python gps_information.py
```
然後依照提示輸入包含圖片或影片的資料夾路徑。

### 2. 輸入資料夾路徑
當系統提示時，輸入包含圖片或影片的資料夾。例如：
```
請輸入包含圖片或影片的資料夾路徑: C:\Users\user\Desktop\imgs
```

### 3. 結果輸出
程式會自動提取所有元數據，並將其儲存到該資料夾內的 `alldata.csv`。

## 支援的文件格式
- 圖片：JPG, JPEG, PNG, TIF, TIFF
- 影片：MP4, MOV, AVI, MKV

## 生成的 CSV 檔案格式
CSV 檔案將包含每個文件的所有可用元數據，每行對應一個檔案，並包含以下欄位（部分取決於文件是否含有對應數據）：
- File Name
- GPS 經緯度
- 拍攝時間
- 相機型號
- 解析度
- 其他 Exif/XMP/Composite 數據

## 錯誤處理
- 若資料夾不存在，程式將回報錯誤。
- 若檔案無可用元數據，則不會寫入至 CSV。
