# Experiment with golden ratio delay

from src.symbolic_echo import SymbolicEchoSystem
from src.simulation_engine import SimulationEngine
from src.metrics import MetricsEngine
import math
import os

# Golden ratio as delay
golden_ratio = (1 + math.sqrt(5)) / 2

# Setup
system = SymbolicEchoSystem(
    state_length=64,
    delay=golden_ratio * 64,  # scaling it to state length
    gamma=2.5,
    threshold_theta=0.3
)

metrics = MetricsEngine()
engine = SimulationEngine(system, metrics)

# Run simulation
engine.run(steps=1000)

# Save results
os.makedirs("src/results", exist_ok=True)
metrics.save_to_file("src/results/phi_delay_metrics.json")

print("Simulation complete. Results saved to src/results/phi_delay_metrics.json")
