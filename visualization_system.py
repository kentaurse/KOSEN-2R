import matplotlib.pyplot as plt
import seaborn as sns

class ResultVisualizer:
    def __init__(self):
        plt.style.use('seaborn')
        self.fig_size = (12, 8)
        
    def plot_frequency_response(self, data, critical_bands=True):
        """周波数応答プロット生成"""
        plt.figure(figsize=self.fig_size)
        
        # メインプロット
        plt.plot(data[:, 0], data[:, 1], 'b-', linewidth=1.5)
        
        if critical_bands:
            # 重要周波数帯のハイライト
            plt.axvspan(43, 53, alpha=0.2, color='yellow', label='Band 1')
            plt.axvspan(53, 57, alpha=0.2, color='red', label='Band 2')
        
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Acceleration (g)')
        plt.title('Frequency Response Analysis')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        return plt.gcf() 