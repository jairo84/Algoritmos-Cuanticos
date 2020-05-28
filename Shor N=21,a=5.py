from qiskit import *;
from qiskit.tools.visualization import plot_histogram;
import math;
circuit = QuantumCircuit(10,10)
for i in range(0,5):
    circuit.h(i)
circuit.x(5)
circuit.barrier()
#si el qbit 0 esta a 1 se realiza 1X5
circuit.cx(0,7)
circuit.barrier()
# 5^2mod21 = X4
circuit.ccx(1,8,9)
circuit.ccx(1,8,6)
circuit.cswap(1,8,6)
circuit.cswap(1,7,9)
circuit.cswap(1,5,7)
circuit.barrier()
# 5^4mod21 = x16
circuit.cswap(2,5,7)
circuit.cswap(2,7,9)
circuit.cswap(2,8,6)
circuit.ccx(2,8,6)
circuit.ccx(2,8,9)
circuit.barrier()
# 5^8mod21 = X4
circuit.ccx(3,8,9)
circuit.ccx(3,8,6)
circuit.cswap(3,8,6)
circuit.cswap(3,7,9)
circuit.cswap(3,5,7)
circuit.barrier()
# 5^16mod21 = X16
circuit.cswap(4,5,7)
circuit.cswap(4,7,9)
circuit.cswap(4,8,6)
circuit.ccx(4,8,6)
circuit.ccx(4,8,9)
circuit.barrier()
for j in range(4,-1,-1):
    circuit.h(j)
    for k in range(j-1,-1,-1):
        circuit.cu1(-1*math.pi/float(2**(j-k)), k, j)
circuit.barrier()
for i in range(5):
    circuit.measure(i,4-i)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit,backend=simulator).result()
plot_histogram(result.get_counts(circuit))
%matplotlib inline
circuit.draw(output='mpl')
