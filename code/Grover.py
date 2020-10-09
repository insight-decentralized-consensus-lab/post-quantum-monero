"""Python implementation of Grovers algorithm through use of the Qiskit library to find the value 3 (|11>) 
out of four possible values."""

#import numpy and plot library

import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.providers.ibmq import least_busy
from qiskit.quantum_info import Statevector

# import basic plot tools
from qiskit.visualization import plot_histogram

# define variables, 1) initialize qubits to zero
n = 2
grover_circuit = QuantumCircuit(n)

#define initialization function 
def initialize_s(qc, qubits):
    '''Apply a H-gate to 'qubits' in qc'''
    for q in qubits:
        qc.h(q)
    return qc

### begin grovers circuit ###

#2) Put qubits in equal state of superposition
grover_circuit = initialize_s(grover_circuit, [0,1])

# 3) Apply oracle reflection to marked instance x_0 = 3,  (|11>) 
grover_circuit.cz(0,1)
statevec = job_sim.result().get_statevector()
from qiskit_textbook.tools import vector2latex
vector2latex(statevec, pretext="|\\psi\\rangle =")

# 4) apply additional reflection (diffusion operator)
grover_circuit.h([0,1])
grover_circuit.z([0,1])
grover_circuit.cz(0,1)
grover_circuit.h([0,1])


# 5) measure the qubits
grover_circuit.measure_all()

# Load IBM Q account and get the least busy backend device
provider = IBMQ.load_account()
device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 3 and 
                                   not x.configuration().simulator and x.status().operational==True))
print("Running on current least busy device: ", device)


from qiskit.tools.monitor import job_monitor
job = execute(grover_circuit, backend=device, shots=1024, optimization_level=3)
job_monitor(job, interval = 2)

results = job.result()
answer = results.get_counts(grover_circuit)
plot_histogram(answer)

#highest amplitude should correspond with marked value x_0 (|11>)
