import numpy as np
from ansys.mapdl.core import launch_mapdl

class VibrationAnalyzer:
    def __init__(self):
        self.mapdl = launch_mapdl()
        
    def analyze_frequency_response(self, results_file):
        """周波数応答の詳細分析"""
        data = np.loadtxt(results_file)
        
        def analyze_frequency_band(freq_min, freq_max):
            mask = (data[:, 0] >= freq_min) & (data[:, 0] <= freq_max)
            band_data = data[mask]
            
            results = {
                'peak_acceleration': np.max(band_data[:, 1]),
                'resonance_frequency': band_data[np.argmax(band_data[:, 1]), 0],
                'average_response': np.mean(band_data[:, 1]),
                'standard_deviation': np.std(band_data[:, 1])
            }
            
            return results
        
        # 特定周波数帯の分析
        band_43_53 = analyze_frequency_band(43, 53)
        band_53_57 = analyze_frequency_band(53, 57)
        
        return {
            'band_43_53': band_43_53,
            'band_53_57': band_53_57,
            'overall_max': np.max(data[:, 1]),
            'critical_frequencies': self._find_critical_frequencies(data)
        }
    
    def _find_critical_frequencies(self, data):
        """共振周波数の特定"""
        from scipy.signal import find_peaks
        peaks, _ = find_peaks(data[:, 1], height=0.8*np.max(data[:, 1]))
        return data[peaks, 0] 