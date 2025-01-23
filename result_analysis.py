import ansys.mapdl.core as mapdl
import numpy as np

def analyze_frequency_response(results_file):
    # 周波数応答データの読み込み
    freq_data = np.loadtxt(results_file)
    
    # 特定周波数帯域の分析
    def analyze_band(freq_min, freq_max):
        mask = (freq_data[:, 0] >= freq_min) & (freq_data[:, 0] <= freq_max)
        band_data = freq_data[mask]
        return {
            'max_acceleration': np.max(band_data[:, 1]),
            'resonance_freq': band_data[np.argmax(band_data[:, 1]), 0]
        }
    
    # 43-53 Hz帯域の分析
    band1 = analyze_band(43, 53)
    # 53-57 Hz帯域の分析
    band2 = analyze_band(53, 57)
    
    return band1, band2 