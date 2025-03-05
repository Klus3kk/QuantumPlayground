import pennylane as qml
from pennylane import numpy as np 

dev = qml.device("default.qubit", wires = [2,0,1])

@qml.qnode(dev)
def my_first_quantum_function(theta):
    qml.RX(theta, wires = 0)
    qml.PauliY(wires = 1)
    qml.Hadamard(wires = 0)
    qml.Hadamard(wires = 1)

    return qml.state()

my_first_qnode = qml.QNode(my_first_quantum_function, dev)
print(my_first_qnode(np.pi/4))
# print(my_first_quantum_function(np.pi/4))