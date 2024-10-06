import matplotlib.pyplot as plt

def plot_fhr(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Time_sec'], data['Fhr1(BPM)'], color='blue')
    plt.title('Time vs FHR1')
    plt.xlabel('Time (seconds)')
    plt.ylabel('FHR1 (bpm)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(data['Time_sec'], data['Fhr2(BPM)'], color='blue')
    plt.title('Time vs FHR2')
    plt.xlabel('Time (seconds)')
    plt.ylabel('FHR2 (bpm)')
    plt.grid(True)
    plt.show()

def plot_uc(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Time_sec'], data['Uc(TOCO)'], color='green')
    plt.title('Time vs UC(TOCO)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('UC(TOCO)')
    plt.grid(True)
    plt.show()
