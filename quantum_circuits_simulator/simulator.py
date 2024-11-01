from qiskit import transpile, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
from quantum_gates import apply_hadamard, apply_pauli_x, apply_cnot
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


# Initialize a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply quantum gates
apply_hadamard(qc, 0)  # Apply Hadamard gate to qubit 0
apply_pauli_x(qc, 1)   # Apply Pauli-X gate to qubit 1
apply_cnot(qc, 0, 1)   # Apply CNOT gate with qubit 0 as control and qubit 1 as target

# Visualize the circuit
print("Quantum Circuit:")
print(qc)

# Simulate and visualize the final state
backend = AerSimulator.get_backend('statevector_simulator')
transpiled_circuit = transpile(qc, backend)
job = execute(transpiled_circuit, backend)
result = job.result()
statevector = result.get_statevector()

# Plot the Bloch sphere representation
plot_bloch_multivector(statevector)
plt.show()
