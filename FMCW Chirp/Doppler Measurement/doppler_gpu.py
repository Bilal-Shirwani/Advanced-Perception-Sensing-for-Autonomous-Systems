import cupy as cp             # Using CuPy instead of NumPy
import numpy as np            # Still needed for plotting (Matplotlib needs CPU data)
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION (Same as before) ---
fs = 10e6
start_freq = 24e9
bandwidth = 500e6
chirp_duration = 50e-6
slope = bandwidth / chirp_duration
num_chirps = 128
c = 3e8
r_start = 50.0
velocity = 20.0

# --- 2. GENERATE 2D DATA CUBE ON GPU ---
# Create the time axis directly on the GPU
t = cp.linspace(0, chirp_duration, int(fs * chirp_duration))
N = len(t)

# Initialize the Data Cube on the GPU (VRAM)
data_cube = cp.zeros((num_chirps, N), dtype=cp.complex64)

print("Processing on GPU...")
for i in range(num_chirps):
    t_slow = i * chirp_duration
    r_current = r_start + (velocity * t_slow)
    td = 2 * r_current / c
    
    # Calculation happens on the NVIDIA GPU
    phase = 2 * cp.pi * (slope * td * t + start_freq * td)
    data_cube[i, :] = cp.exp(1j * phase) # Complex representation is faster for FFTs

# --- 3. GPU-ACCELERATED FFTs ---
# Step A: Range FFT (Fast-Time)
range_fft = cp.fft.fft(data_cube, axis=1)

# Step B: Doppler FFT (Slow-Time)
rd_map = cp.fft.fftshift(cp.fft.fft(range_fft, axis=0), axes=0)
rd_map_db = 20 * cp.log10(cp.abs(rd_map) + 1e-9)

# --- 4. VISUALIZATION ---
# CRITICAL: We must move data back to the CPU (NumPy) for Matplotlib to display it
rd_map_cpu = cp.asnumpy(rd_map_db) 

plt.figure(figsize=(10, 8))
plt.imshow(rd_map_cpu[:, 0:N//2], aspect='auto', cmap='jet', origin='lower')
plt.title("GPU-Accelerated Range-Doppler Map")
plt.xlabel("Range Bins")
plt.ylabel("Doppler Bins (Velocity)")
plt.colorbar(label="Power (dB)")
plt.show()