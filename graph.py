import matplotlib.pyplot as plt
import numpy as np

# データの生成
freq = np.linspace(40.0, 60.0, 1000)
response = np.zeros_like(freq)

# 2つの共振ピークを持つ応答関数の生成
def response_function(f, f_n, zeta, amp):
    return amp / np.sqrt((1 - (f/f_n)**2)**2 + (2*zeta*f/f_n)**2)

# リードミファイルの仕様に基づく設定
# 47.5 Hzと55.3 Hzの2つの共振ピーク
# 伝達率: 1.89 (43-53Hz帯域) と 2.08 (53-57Hz帯域)
response += response_function(freq, 47.5, 0.02, 2.84)  # 1次共振
response += response_function(freq, 55.3, 0.02, 3.12)  # 2次共振

# プロットの作成
plt.figure(figsize=(12, 8))
plt.plot(freq, response, 'b-', linewidth=0.5)  # 線を細くして見やすく

# グリッド設定
plt.grid(True, which='both', color='gray', linestyle='-', alpha=0.2)

# 重要な周波数帯域のハイライト
plt.axvspan(43, 53, alpha=0.2, color='yellow', label='43-53 Hz帯域')
plt.axvspan(53, 57, alpha=0.2, color='red', label='53-57 Hz帯域')

# 共振ピークの表示
plt.plot(47.5, 2.84, 'ro', label='共振点1 (47.5 Hz, 2.84g)')
plt.plot(55.3, 3.12, 'go', label='共振点2 (55.3 Hz, 3.12g)')

# グラフの装飾
plt.xlabel('周波数 [Hz]')
plt.ylabel('応答加速度 [g]')
plt.title('KOSEN-2R 周波数応答特性')
plt.legend(loc='upper right')

# 軸の範囲設定
plt.xlim(40.0, 60.0)
plt.ylim(0.0, 4.0)

# x軸の目盛り設定
plt.xticks(np.arange(40.0, 60.1, 2.5))

# グラフの保存
plt.savefig('frequency_response.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()