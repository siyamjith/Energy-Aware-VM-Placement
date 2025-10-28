# energy_aware_vm.py
# Simple Energy-Aware VM Placement Simulator
# SDG 7 – Affordable and Clean Energy

import random
import matplotlib.pyplot as plt

class Host:
    def __init__(self, name, capacity=1.0, idle_power=100, max_power=250):
        self.name = name
        self.capacity = capacity
        self.idle = idle_power
        self.max = max_power
        self.vms = []

    def utilization(self):
        used = sum(self.vms)
        return used / self.capacity

    def can_host(self, vm):
        return sum(self.vms) + vm <= self.capacity

    def power(self):
        if not self.vms:
            return 0
        u = self.utilization()
        return self.idle + (self.max - self.idle) * u

def first_fit(hosts, vm):
    for h in hosts:
        if h.can_host(vm):
            h.vms.append(vm)
            return True
    return False

def energy_aware(hosts, vm):
    best_host = None
    best_increase = float('inf')
    for h in hosts:
        if h.can_host(vm):
            before = h.power()
            new_util = (sum(h.vms) + vm) / h.capacity
            after = h.idle + (h.max - h.idle) * new_util
            inc = after - before
            if inc < best_increase:
                best_increase = inc
                best_host = h
    if best_host:
        best_host.vms.append(vm)
        return True
    return False

def simulate(strategy, label):
    hosts = [Host(f"H{i}") for i in range(5)]
    vms = [random.uniform(0.1, 0.5) for _ in range(20)]  # 20 random VMs

    for vm in vms:
        strategy(hosts, vm)

    total_power = sum(h.power() for h in hosts)
    active_hosts = sum(1 for h in hosts if h.vms)
    print(f"{label}: Active Hosts = {active_hosts}, Total Power = {total_power:.2f}W")

    return label, total_power, active_hosts

# --- Run both strategies ---
ff_label, ff_power, ff_hosts = simulate(first_fit, "First-Fit")
ea_label, ea_power, ea_hosts = simulate(energy_aware, "Energy-Aware")

# --- Compare and visualize ---
labels = [ff_label, ea_label]
powers = [ff_power, ea_power]

plt.bar(labels, powers, color=["orange", "green"])
plt.ylabel("Total Power (Watts)")
plt.title("Energy Comparison of VM Placement Strategies")
plt.savefig("results/energy_comparison.png")
plt.show()

print("\nConclusion:")
if ea_power < ff_power:
    print("✅ Energy-Aware placement uses less power → supports SDG 7 (Clean Energy).")
else:
    print("❌ No improvement found — try more VMs.")
