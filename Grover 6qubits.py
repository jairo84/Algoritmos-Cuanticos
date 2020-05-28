from qiskit import *
from qiskit.tools.visualization import plot_histogram;
import math;

q = QuantumRegister(6, 'q')
c = ClassicalRegister(6, 'c')
circuit = QuantumCircuit(q, c)

#inicializacion
for i in range(0,6):
    circuit.h(i)
circuit.barrier()

#oraculo |110010>
circuit.cz(4,5)
circuit.x(2)
circuit.x(3)
circuit.cz(2,3)
circuit.x(2)
circuit.x(3)
circuit.x(0)
circuit.cz(0,1)
circuit.x(0)
circuit.barrier()

#inversa sobre la media
for i in range(0,6):
    circuit.h(i)
    circuit.z(i)
    
circuit.cz(0,1)
circuit.cz(2,3)
circuit.cz(4,5)

for i in range(0,6):
    circuit.h(i)
circuit.barrier()

for i in range(0,6):
    circuit.measure(q[i],c[i])
    
%matplotlib inline
circuit.draw(output='mpl')
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit,backend=simulator).result()
plot_histogram(result.get_counts(circuit))
