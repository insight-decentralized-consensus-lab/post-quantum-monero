"""The following is python code utilizing the qiskit library that can be run on extant quantum 
hardware using 5 qubits for factoring the integer 15 into 3 and 5. Using period finding, 
for a^r mod N = 1, where a = 11 and N = 15 (the integer to be factored) the problem is to find
r values for this identity such that one can find the prime factors of N. For 11^r mod(15) =1,
results (as shown in fig 1.) correspond with period r = 4 (|00100>) and r = 0 (|00000>).
To find the factor, use the equivalence a^r mod 15. From this:
(a^r -1) mod 15 = (a^(r/2) + 1)(a^(r/2) - 1) mod 15.In this case, a = 11. Plugging in the two r
values for this a value yields (11^(0/2) +1)(11^(4/2) - 1) mod 15 = 2*(11 +1)(11-1) mod 15 
Thus, we find (24)(20) mod 15. By finding the greatest common factor between the two coefficients,
gcd(24,15) and gcd(20,15), yields 3 and 5 respectively. These are the prime factors of 15,
so the result of running shors algorithm to find the prime factors of an integer using quantum
hardware are demonstrated. Note, this is not the same as the technical implementation of shor's
algorithm described in this section for breaking the discrete log hardness assumption, 
though the proof of concept remains."""

# Import libraries

from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from numpy import pi
from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.providers.ibmq import least_busy
from qiskit.visualization import plot_histogram

# Initialize qubit registers
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.reset(qreg_q[2])
circuit.reset(qreg_q[3])
circuit.reset(qreg_q[4])

# Apply Hadamard transformations to qubit registers
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[2])

# Apply first QFT, modular exponentiation, and another QFT
circuit.h(qreg_q[1])
circuit.cx(qreg_q[2], qreg_q[3])
circuit.crx(pi/2, qreg_q[0], qreg_q[1])
circuit.ccx(qreg_q[2], qreg_q[3], qreg_q[4])
circuit.h(qreg_q[0])
circuit.rx(pi/2, qreg_q[2])
circuit.crx(pi/2, qreg_q[1], qreg_q[2])
circuit.crx(pi/2, qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])

# Measure the qubit registers 0-2
circuit.measure(qreg_q[2], creg_c[2])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])

# Get least busy quantum hardware backend to run on
provider = IBMQ.load_account()
device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 3 and 
                                   not x.configuration().simulator and x.status().operational==True))
print("Running on current least busy device: ", device)

# Run the circuit on available quantum hardware and plot histogram
from qiskit.tools.monitor import job_monitor
job = execute(circuit, backend=device, shots=1024, optimization_level=3)
job_monitor(job, interval = 2)

results = job.result()
answer = results.get_counts(circuit)
plot_histogram(answer)

#largest amplitude results correspond with r values used to find the prime factor of N. 
