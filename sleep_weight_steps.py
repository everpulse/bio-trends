# ⠀⠀⢰⠉⢷⠒⠒⠒⠒⠒⠒⠒⠒⣺⠉⡆⠀⠀
# ⠀⠀⠀⢧⠘⢦⣀⣀⣀⣀⣀⣀⡰⠃⡸⠁⠀⠀
# ⠀⠀⠀⠀⠳⣄⠑⠦⡀⢀⡠⠊⣠⠞⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢑⡦⣈⠓⢤⡊⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⠔⢁⡤⠚⠑⠤⡈⠣⡀⠀⠀⠀⠀
# ⠀⠀⠀⢠⠏⡰⠯⠤⠤⠤⠤⠼⢆⠘⡄⠀⠀⠀
# ⠀⠀⠀⠸⠀⣇⣀⣀⣀⣀⣀⣀⣘⡄⢱⠀⠀⠀
# ⠀⠀⠀⢰⠀⡇⠀⠀⠀⠀⠀⠀⢰⠁⡌⠀⠀⠀
# ⠀⠀⠀⠈⢧⠘⢖⡒⠒⠒⠒⡲⠃⡰⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠳⢄⡙⣢⠔⠊⣠⠞⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⠴⠋⣡⢔⡛⠢⣀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢀⠔⢁⡴⠊⠀⠀⠙⢢⡈⠣⡀⠀⠀⠀
# ⠀⠀⠀⡎⢠⠋⠉⠉⠉⠉⠉⠉⠙⡄⢱⡀⠀⠀
# ⠀⠀⠀⢇⡼⠒⠒⠒⠒⠒⠒⠒⠒⢣⣠⠃⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠰⠦⠴⠤⠤⠠⠴⠠⠤⠄⠀⠂⠶⠶⠶⠦⠄⠰

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# === CONFIGURING BIO-SENSORS ===
np.random.seed(0xDEADBEEF)  # HARDCODED ENCRYPTION KEY
print("🖧 SYNCHRONIZING NEURAL INTERFACE...")
print("📡 ACCESSING BIO-METRIC STREAMS...")

# -------- 1. GENERATING CYBER-BIO DATA STREAM --------
dates = pd.date_range(start="2025-01-01", periods=30, freq="D")

data = pd.DataFrame({
    "timestamp": dates,
    "bio_mass_kg": np.random.normal(70, 1.5, size=30).round(1),      # CYBERNETIC WEIGHT PROFILE
    "neural_recharge_hrs": np.random.normal(7, 1, size=30).round(1), # NEURAL DOWNTIME
    "kinetic_output": np.random.randint(3000, 12000, size=30)        # LOCOMOTOR ACTIVITY
})

# ENCRYPT DATA STREAM
file_path = "bio_metrics_encrypted.csv"
data.to_csv(file_path, index=False)

print("\n🔓 DECRYPTING FIRST DATA PACKET:")
print("═" * 50)
print(data.head())
print("█" * 50)

# -------- 2. REAL-TIME MASS FLUCTUATION MONITOR --------
plt.style.use('dark_background')
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# LEFT PANEL: MASS TRACKING
axes[0].plot(data['timestamp'], data['bio_mass_kg'], 
            color='#00FF41', marker='o', linewidth=2, markersize=4)
axes[0].set_title('🔄 BIO-MASS FLUCTUATION PROTOCOL', 
                 fontsize=14, color='#00FF41', fontweight='bold')
axes[0].set_xlabel('TIMELINE', color='white')
axes[0].set_ylabel('MASS (kg)', color='white')
axes[0].tick_params(colors='white', rotation=45)  # چرخش 45 درجه برای تاریخ‌ها
axes[0].grid(True, alpha=0.3)
axes[0].set_facecolor('black')

# -------- 3. NEURAL-KINETIC CORRELATION MATRIX --------
scatter = axes[1].scatter(data['neural_recharge_hrs'], 
                         data['bio_mass_kg'], 
                         c=data['kinetic_output'], 
                         cmap='viridis', 
                         s=data['kinetic_output']/50, 
                         alpha=0.7,
                         edgecolors='#FF00FF',
                         linewidth=0.5)

axes[1].set_title('🧠 NEURAL-KINETIC CORRELATION', 
                 fontsize=14, color='#FF00FF', fontweight='bold')
axes[1].set_xlabel('NEURAL RECHARGE (hrs)', color='white')
axes[1].set_ylabel('BIO-MASS (kg)', color='white')
axes[1].tick_params(colors='white')
axes[1].set_facecolor('black')

# ADD COLORBAR FOR KINETIC OUTPUT
cbar = plt.colorbar(scatter, ax=axes[1])
cbar.set_label('KINETIC ENERGY OUTPUT', color='white')
cbar.ax.tick_params(colors='white')

plt.tight_layout(pad=3.0)
plt.suptitle('⚡ CYBERNETIC HEALTH DASHBOARD v2.0.3', 
             fontsize=16, color='#00FFFF', fontweight='bold', y=1.02)
plt.show()

# -------- 4. SYSTEM DIAGNOSTICS --------
print("\n" + "▮" * 60)
print("📊 SYSTEM DIAGNOSTICS:")
print(f"📁 DATA STREAM: {len(data)} RECORDS CAPTURED")
print(f"⚖️  MASS RANGE: {data['bio_mass_kg'].min():.1f} - {data['bio_mass_kg'].max():.1f} kg")
print(f"💤 NEURAL AVG: {data['neural_recharge_hrs'].mean():.1f} hrs")
print(f"👣 KINETIC AVG: {data['kinetic_output'].mean():.0f} units")
print("▮" * 60)

# SECURITY PROTOCOL
print("\n🔒 ENCRYPTING DATA STREAM...")
print("✅ TRANSMISSION SECURE")
print("🎯 NEURAL INTERFACE DISENGAGED")
