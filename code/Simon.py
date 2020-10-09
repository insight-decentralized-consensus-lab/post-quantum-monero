"""Qiskit code for running Simon's algorithm on quantum hardware for 2 qubits and b = '11' """

# importing Qiskit
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, execute

# import basic plot tools
from qiskit.visualization import plot_histogram
from qiskit_textbook.tools import simon_oracle

#set b equal to '11'
b = '11'

#1) initialize qubits
n = 2
simon_circuit_2 = QuantumCircuit(n*2, n)

#2) Apply Hadamard gates before querying the oracle
simon_circuit_2.h(range(n))

#3) Query oracle
simon_circuit_2 += simon_oracle(b)

#5) Apply Hadamard gates to the input register
simon_circuit_2.h(range(n))

#3) and 6) Measure qubits
simon_circuit_2.measure(range(n), range(n))

# Load saved IBMQ accounts and get the least busy backend device
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= n and 
                                   not x.configuration().simulator and x.status().operational==True))
print("least busy backend: ", backend)

# Execute and monitor the job
from qiskit.tools.monitor import job_monitor
shots = 1024
job = execute(simon_circuit_2, backend=backend, shots=shots, optimization_level=3)
job_monitor(job, interval = 2)

# Get results and plot counts
device_counts = job.result().get_counts()
plot_histogram(device_counts)

#additionally, function for calculating dot product of results
def bdotz(b, z):
    accum = 0
    for i in range(len(b)):
        accum += int(b[i]) * int(z[i])
    return (accum % 2)

print('b = ' + b)
for z in device_counts:
    print( '{}.{} = {} (mod 2) ({:.1f}%)'.format(b, z, bdotz(b,z), device_counts[z]*100/shots))
    
#the most significant results are those for which  b dot z=0(mod 2).

'''b = 11
11.00 = 0 (mod 2) (45.0%)
11.01 = 1 (mod 2) (6.2%)
11.10 = 1 (mod 2) (6.4%)
11.11 = 0 (mod 2) (42.4%)'''
