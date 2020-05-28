from qiskit import *
from qiskit.tools.visualization import plot_histogram;
import math;
q = QuantumRegister(6, 'q')
c = ClassicalRegister(6, 'c')
circuit = QuantumCircuit(q, c)
#inicializar el registro a 1
circuit.x(q[0])
circuit.barrier()
#aplicar a^16 mod 21
circuit.h(q[5])
#8^16 mod 21 = 1
circuit.h(q[5])
#medir el estado de q5
circuit.measure(q[5],c[0])
#reiniciar el cubit q[5] a |0>
circuit.reset(q[5])
circuit.barrier()
#aplicar a^8 mod 21
circuit.h(q[5])
#8^8 mod 21 = 1
#   modificar en funcion del estado anterior
if c[0] == 1:
    circuit.u1(math.pi/2,q[5])
circuit.h(q[5])
#medir el estado de q5
circuit.measure(q[5],c[1])
#reiniciar el cubit q[5] a |0>
circuit.reset(q[5])
circuit.barrier()
#aplicar a^4 mod 21
circuit.h(q[5])
#8^4 mod 21 = 1
#   modificar en funcion del estado anterior
if c[1] == 1:
    circuit.u1(math.pi/2,q[5])
if c[0] == 1:
    circuit.u1(math.pi/4,q[5])
circuit.h(q[5])
#medir el estado de q5
circuit.measure(q[5],c[2])
circuit.reset(q[5])
circuit.barrier()
#aplicar a^2 mod 21
circuit.h(q[5])
#aplicar 8^2 mod 21=1
#   modificar en funcion del estado anterior
if c[2] == 1:
    circuit.u1(math.pi/2,q[5])
if c[1] == 1:
    circuit.u1(math.pi/4,q[5])
if c[0] == 1:
    circuit.u1(math.pi/8,q[5])
circuit.h(q[5])
#medir el estado de q5
circuit.measure(q[5],c[3])
circuit.reset(q[5])
circuit.barrier()
#aplicar a mod 21
circuit.h(q[5])
#aplicar X8
circuit.cswap(5,0,3)

#   modificar en funcion del estado anterior
if c[3] == 1:
    circuit.u1(math.pi/2,q[5])
if c[2] == 1:
    circuit.u1(math.pi/4,q[5])
if c[1] == 1:
    circuit.u1(math.pi/8,q[5])
if c[0] == 1:
    circuit.u1(math.pi/16,q[5])
circuit.h(q[5])
#medir el estado de q5
circuit.measure(q[5],c[4])
circuit.barrier()
backend = Aer.get_backend('qasm_simulator')
sim_job = execute([circuit], backend)
sim_result = sim_job.result()
sim_data = sim_result.get_counts(circuit) 
plot_histogram(sim_data)
circuit.draw(output='mpl')
