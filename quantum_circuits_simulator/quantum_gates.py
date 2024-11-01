from qiskit import QuantumCircuit

def apply_hadamard(circuit, qubit):
    circuit.h(qubit)

def apply_pauli_x(circuit, qubit):
    circuit.x(qubit)

def apply_cnot(circuit, control, target):
    circuit.cx(control, target)
