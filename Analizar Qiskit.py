%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()

circuit = QuantumCircuit(3, 3)

circuit.h(0)
circuit.cx(0,1)
circuit.cx(1,2)

circuit.measure(0,0)
circuit.measure(1,1)
circuit.measure(2,2)

circuit.draw()

backend = Aer.get_backend('qasm_simulator')

result = execute([circuit], backend).result()

plot_histogram(resut.get_counts(circuit))
