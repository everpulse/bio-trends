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
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
     
# === CONFIGURING BIO-SENSORS ===
np.random.seed(0xDEADBEEF)  # Demo Results Locking
print("🖧 SYNCHRONIZING NEURAL INTERFACE...")
print("📡 ACCESSING BIO-METRIC STREAMS...")

# 𖨠──··· Generating Bio-Data ···──𖨠
dates = pd.date_range(start="2025-01-01", periods=30, freq="D")

data = pd.DataFrame({
    "timestamp": dates,
    "biomass": np.random.normal(70, 1.5, size=30).round(1),            # Bio-Mass Profile
    "mind_rest": np.random.normal(7, 1, size=30).round(1),   # NEURAL DOWNTIME
    "activity": np.random.randint(3000, 12000, size=30)          # LOCOMOTOR ACTIVITY
})

file_path = "bio_metrics_encrypted.csv"
data.to_csv(file_path, index=False)

print("\n🛰 Reading Bio-Signals Matrix ⤵︎ ")
print("❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯")
print(tabulate(data.head(), headers='keys', tablefmt='fancy_grid', showindex=False))
print("神经矩阵已激活 - 生物信号流解码：在时间网格中捕获5个网络有机体")

# ✦.── Mass Fluctuation Analysis ──.✦
plt.style.use('dark_background')
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# LEFT PANEL: MASS TRACKING
axes[0].plot(
    data['timestamp'],
    data['biomass'],
    color="#39FF14",
    marker='o',
    markersize=4,
    linewidth=2)

axes[0].set_title(
    '—̳͟͞͞═͟͞͞𝕎𝕖𝕚𝕘𝕙𝕥 𝕎𝕒𝕧𝕖 𝕄𝕠𝕟𝕚𝕥𝕠𝕣═̳͟͞͞—',
    fontsize=14,             
    color="#FF00FF",
    fontweight="bold"
    )

axes[0].tick_params(colors='#FFF', rotation=45)
axes[0].grid(True, alpha=0.3)
axes[0].set_facecolor('black')

# ✦•┈๑⋅⋯ Triad Bio-Interaction Chart ⋯⋅๑┈•✦  
scatter = axes[1].scatter(data['mind_rest'], 
                         data['biomass'], 
                         c=data['activity'], 
                         cmap='viridis', 
                         s=data['activity']/50, 
                         alpha=0.7,
                         edgecolors='#FF00FF',
                         linewidth=0.5)

axes[1].set_title('—̳͟͞͞═͟͞͞𝕊𝕎𝔸 ℂ𝕙𝕒𝕣𝕥═̳͟͞͞—', 
                 fontsize=14, color='#FF00FF', fontweight='bold')
axes[1].set_xlabel('NEURAL RECHARGE (hrs)', color='#CC66DA')
axes[1].set_ylabel('BIO-MASS (kg)', color='#CC66DA')
axes[1].tick_params(colors='white')
axes[1].set_facecolor('black')

# ADD COLORBAR FOR activity OUTPUT
cbar = plt.colorbar(scatter, ax=axes[1])
cbar.set_label('KINETIC ENERGY OUTPUT', color='#C5172E')
cbar.ax.tick_params(colors='#EB5B00')

plt.tight_layout(pad=3.0)
plt.suptitle('⚡ CYBERNETIC HEALTH DASHBOARD v2.0.3', 
             fontsize=16, color='#261FB3', fontweight='bold', y=1)
plt.show()

# -------- 4. SYSTEM DIAGNOSTICS --------
print("\n" + "▮" * 60)
print("📊 SYSTEM DIAGNOSTICS:")
print(f"📁 DATA STREAM: {len(data)} RECORDS CAPTURED")
print(f"⚖️  MASS RANGE: {data['biomass'].min():.1f} - {data['biomass'].max():.1f} kg")
print(f"💤 NEURAL AVG: {data['mind_rest'].mean():.1f} hrs")
print(f"👣 KINETIC AVG: {data['activity'].mean():.0f} units")
print("▮" * 60)

# SECURITY PROTOCOL
print("\n🔒 ENCRYPTING DATA STREAM...")
print("✅ TRANSMISSION SECURE")
print("🎯 NEURAL INTERFACE DISENGAGED")
