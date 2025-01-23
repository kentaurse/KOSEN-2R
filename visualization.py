import matplotlib.pyplot as plt

def plot_frequency_response(data):
    plt.figure(figsize=(12, 8))
    plt.plot(data[:, 0], data[:, 1])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Acceleration (g)')
    plt.title('Frequency Response Analysis')
    
    # 重要周波数帯域のハイライト
    plt.axvspan(43, 53, alpha=0.2, color='yellow')
    plt.axvspan(53, 57, alpha=0.2, color='red')
    
    plt.grid(True)
    plt.savefig('frequency_response.png') 