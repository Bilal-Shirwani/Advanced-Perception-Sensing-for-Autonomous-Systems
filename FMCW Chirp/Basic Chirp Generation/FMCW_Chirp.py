import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration (The 'Radar Hardware' Settings)
sample_rate = 1000.0                  # Hz (How many points per second)
duration = 1.0                        # Seconds (How long the chirp lasts)
f_start = 5.0                         # Hz (Start frequency - low for visibilty)
f_end = 50.0                          # Hz (End frequency)

# 2. Setup Time Axis
# Use np.linspace or np.arange
# It should go from 0 to 'duration', with 'sample_rate * duration' total points
t = np.linspace(0, duration, int(sample_rate * duration))
print(t)

# 3. Claculate slope (S)
# Slope = (Change in Freq)/(Change in Time)
S = (f_end - f_start) / 1
print(S)

# 4. Calculate the Phase (The Hard Part)
# Use the formula: Phase = 2 * pi * (f_start * t + 0.5 * S * t^2)
phase = 2 * np.pi * ((f_start * t) + (0.5 * S * t**2))

# 5. Generate Signal
signal = np.cos(phase)

# 6. Visualization
plt.figure(figsize=(10,6))

# Plot 1: Frequency vs Time (Theoretical)
plt.subplot(2,1,1)
# Plot the ideal frequency line: f = f_start + S * t
plt.plot(t, f_start + S * t)
plt.title("Frequency Ramp (What the Radar intends to send)")
plt.xlabel("Time")
plt.ylabel("Frequency (Hz)")
plt.grid(True)

# Plot 2: The actual waveform (Time Domain)
plt.subplot(2, 1, 2)
plt.plot(t, signal)
plt.title("Transmitted Chirp Signal (What goes over the air)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()