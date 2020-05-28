import cirq

qr = cirq.LineQubit.range(5)
c = cirq.Circuit()

c.append(cirq.H(qr[0]))
c.append(cirq.H(qr[1]))
c.append(cirq.H(qr[2]))

c.append(cirq.Z(qr[0]))
c.append(cirq.H(qr[2]))

c.append(cirq.H(qr[0]))
c.append(cirq.CX(qr[1], qr[2]))

c.append(cirq.measure(qr[0], key='x0'))

c.append(cirq.H(qr[1]))
c.append(cirq.H(qr[2]))

c.append(cirq.measure(qr[1], key='x1'))

c.append(cirq.H(qr[2]))

c.append(cirq.measure(qr[2], key='x2'))

result = cirq.Simulator().run(c, repetitions=1000)

print(c)

cirq.plot_state_histogram(result)
