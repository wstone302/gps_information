import georinex as gr

rinex_file = "C:/Users/user/Desktop/100_0082_Rinex.obs"
obs = gr.load(rinex_file)

if obs is None:
    print("❌ 讀取失敗，請檢查檔案格式")
else:
    print("✅ 讀取成功，資料資訊如下：")
    print(obs)


import georinex as gr
import pandas as pd

# 讀取 RINEX 觀測數據
rinex_file = "C:/Users/user/Desktop/100_0082_Rinex.obs"
obs = gr.load(rinex_file)

# 轉換為 DataFrame
df = obs.to_dataframe()
print(df)


import matplotlib.pyplot as plt

# 獲取唯一的時間點
time_point = df.index.get_level_values("time")[0]  # 只取第一個時間點

# 過濾 C/N0 相關數據 (S1I, S7I)
cn0_data = df.filter(like="S")  # 只取 'S' 開頭的欄位

# 繪製信號強度條狀圖
plt.figure(figsize=(8, 5))
plt.bar(cn0_data.columns, cn0_data.iloc[0].values)
plt.xlabel("Signal Type")
plt.ylabel("C/N0 (dB-Hz)")
plt.title(f"Satellite C/N0 Signal Strength at {time_point}")
plt.grid(axis="y")
plt.show()

# 確保數據有多個時間點
if len(df.index.get_level_values("time").unique()) > 1:
    num_sats = df.groupby("time").size()  # 計算每個時間點的衛星數量

    plt.figure(figsize=(10, 5))
    plt.plot(num_sats.index, num_sats.values, marker="o", linestyle="-", label="Visible Satellites")
    plt.xlabel("Time")
    plt.ylabel("Number of Satellites")
    plt.title("Number of Visible Satellites Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
else:
    print("⚠️ 只有一個時間點，無法繪製衛星數量變化圖！")
