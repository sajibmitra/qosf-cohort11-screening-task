from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a 2-qubit Bell circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Build a local simulator
simulator = AerSimulator()

# Transpile the circuit for the simulator
tqc = transpile(qc, simulator)

# Run the simulation (shots=1000)
job = simulator.run(tqc, shots=1000)
result = job.result()
counts = result.get_counts()

print("Counts:", counts)
