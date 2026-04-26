# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Define Parameters
f_c = 1e9  # Carrier Frequency (Hz)
B = 200e6  # Bandwidth (Hz)
T = 40e-6  # Chirp Duration (s)
fs = 5e9  # Sampling Frequency (Hz)
t = np.linspace(0, T, int(T * fs))  # Time Vector, Discrete Time Points
S = B / T  # Chirp Slope (Hz/s)
c = 3e8  # Speed of Light (m/s)

# Generate FMCW Chirp Signal
phase = 2 * np.pi * (f_c * t + (S / 2) * t**2)  # Phase of the Chirp Signal
transmit_chirp = np.cos(phase)  # Real Part of the Chirp Signal

# Simulate Target
R = 100  # Target Range (m)
tau = 2 * R / c  # Time Delay (s), Round Trip Time, Echo Time

# Generate Received Signal (Echo)
phase_echo = 2 * np.pi * (f_c * (t - tau) + (S / 2) * (t - tau)**2)  # Phase of the Echo Signal
received_chirp = np.cos(phase_echo)  # Real Part of the Echo Signal

#Generate Mixed Signal (Beat Signal)
mixed_signal = transmit_chirp * received_chirp  # Beat Signal (Real Part)

# Plot
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t , transmit_chirp)
plt.title('FMCW Chirp Signal (Real Part)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, received_chirp)
plt.title('Received Echo Signal (Real Part)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, mixed_signal)
plt.title('Mixed Signal (Beat Signal)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

