import cirq
import matplotlib.pyplot as plt
import numpy as np

qubits = cirq.LineQubit.range(10)
c =cirq.Circuit()

q_qft =[qubits[0], qubits[1], qubits[2], qubits[3], qubits[4]]
c.append(cirq.H(qubits[0]))
c.append(cirq.H(qubits[1]))
c.append(cirq.H(qubits[2]))
c.append(cirq.H(qubits[3]))
c.append(cirq.H(qubits[4]))
c.append(cirq.X(qubits[5]))

c.append(cirq.CX(qubits[0],qubits[7]))

c.append(cirq.CCX(qubits[1], qubits[8],qubits[9]))
c.append(cirq.CCX(qubits[8],qubits[1], qubits[6]))
c.append(cirq.CSWAP(qubits[1],qubits[6], qubits[8]))
c.append(cirq.CSWAP(qubits[1],qubits[7], qubits[9]))
c.append(cirq.CSWAP(qubits[1],qubits[5], qubits[7]))

c.append(cirq.CSWAP(qubits[2],qubits[5], qubits[7]))
c.append(cirq.CSWAP(qubits[2],qubits[7], qubits[9]))
c.append(cirq.CSWAP(qubits[2],qubits[6], qubits[8]))
c.append(cirq.CCX(qubits[2], qubits[6],qubits[8]))
c.append(cirq.CCX(qubits[2],qubits[8], qubits[9]))

c.append(cirq.CCX(qubits[3], qubits[8],qubits[9]))
c.append(cirq.CCX(qubits[6],qubits[3], qubits[8]))
c.append(cirq.CSWAP(qubits[3],qubits[6], qubits[8]))
c.append(cirq.CSWAP(qubits[3],qubits[7], qubits[9]))
c.append(cirq.CSWAP(qubits[3],qubits[5], qubits[7]))

c.append(cirq.CSWAP(qubits[4],qubits[5], qubits[7]))
c.append(cirq.CSWAP(qubits[4],qubits[7], qubits[9]))
c.append(cirq.CSWAP(qubits[4],qubits[6], qubits[8]))
c.append(cirq.CCX(qubits[4], qubits[6],qubits[8]))
c.append(cirq.CCX(qubits[4],qubits[8], qubits[9]))

c.append(cirq.QFT(*q_qft,without_reverse=True, inverse=True))

c.append(cirq.measure(qubits[0], key='x0'))
c.append(cirq.measure(qubits[1], key='x1'))
c.append(cirq.measure(qubits[2], key='x2'))
c.append(cirq.measure(qubits[3], key='x3'))
c.append(cirq.measure(qubits[4], key='x4'))


result = cirq.Simulator().run(c, repetitions=100)

print(c)

cirq.plot_state_histogram(result)
