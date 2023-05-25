import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Die Daten werden von der Datei 'ecg_ppg_data.npy' eingelesen und umgeformt
data= 'ecg_ppg_data.npy'

datei = np.load(data)
ecg = -datei[:,:1]
EKG=np.reshape(ecg,len(ecg))
ppg = datei[:,-1]
PPG=np.reshape(ppg,len(ppg))

# Auffinden der Spitzen im EKG (R-Zacken)- und PPG-Signal.
peaks, _ = find_peaks(EKG, height=0.4)
peaksPPG, _ = find_peaks(PPG, height=0)
r_Zacken= np.array(peaks)
rr_abstaende= np.zeros((len(r_Zacken))-1)

# Subtrahieren der Spitzen des PPG-Signals von den Spitzen des EKG-Signals.
PTT = peaksPPG[1:] - peaks
'''''
 Erstellen eines neuen Arrays mit der gleichen Länge wie das PPG-Signal. 
Dann füllt es das Array mit dem PTT-Werte.
'''
ptt_kurve = np.zeros(len(ppg))

# Füllen das Array "ptt_kurve" mit den PTT-Werten.
for index, value in enumerate(peaksPPG[1:]):
    ptt_kurve[value:] = PTT[index]





# Die Kurven unteranderem Rohdaten und PTT-Kurve werden graphisch dargestellt.
fig,axs=plt.subplots(4, sharex=True, constrained_layout=True)
fig.suptitle('Puls-Transit-Zeit', fontsize='xx-large', weight='extra bold')
axs[0].plot(ecg)
axs[0].plot(ppg)
axs[0].set_ylabel('mv')
axs[0].set_title('EKG und PPG Signale')
axs[1].plot(ecg)
axs[1].set_title('R-Zacken im EKG')
axs[1].set_ylabel('mv')
axs[1].plot(peaks,EKG[peaks],"X", color="orange")
axs[2].plot(ppg)
axs[2].set_title('Maxima in PPG-Kurve')
axs[2].plot(peaksPPG,PPG[peaksPPG],"X",np.zeros_like(PPG), "--", color="orange")
axs[2].set_ylabel('mm Hg')
axs[3].set_ylim(315,335)
axs[3].set_title('PTT-Kurve')
axs[3].set_ylabel('mm Hg')
axs[3].plot(ptt_kurve)
for ax in axs.flat:
    ax.set(xlabel='Zeit Sec')
plt.show()
