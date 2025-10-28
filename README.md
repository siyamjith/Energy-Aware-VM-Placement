# 🌱 Energy-Aware VM Placement Simulator (SDG 7 – Clean Energy)

A mini project that simulates **energy-efficient Virtual Machine (VM) placement** in a cloud data center.  
It compares **First-Fit** and **Energy-Aware** algorithms to minimize power consumption, supporting **UN SDG 7 – Affordable and Clean Energy**.

---

## 🎯 Objective
To reduce total energy usage in cloud data centers through smart VM placement that efficiently utilizes host resources.

---

## 🧩 How It Works
- Each host (server) has limited CPU capacity and power range.  
- Virtual Machines (VMs) consume varying CPU resources.  
- The project tests two placement methods:
  1. **First-Fit (FF):** Places VMs sequentially without considering energy.
  2. **Energy-Aware (EA):** Chooses the host that increases power consumption the least.

The simulator shows which method consumes less energy overall.

---

## ⚙️ Requirements
Install dependencies:
```bash

pip install -r requirements.txt
▶️ Run the Simulation
python energy_aware_vm.py



After running, a graph comparing total power consumption will be saved as:

results/energy_comparison.png

📊 Sample Output
First-Fit: Active Hosts = 4, Total Power = 675.00W
Energy-Aware: Active Hosts = 3, Total Power = 522.50W

✅ Energy-Aware placement uses less power → supports SDG 7 (Clean Energy).

📂 Project Structure
Energy-Aware-VM-Placement/
├── energy_aware_vm.py
├── requirements.txt
├── README.md
├── LICENSE
└── results/
    └── energy_comparison.png
