from qiskit import *
# Registro cuantico 3 qubits
qr=QuantumRegister(3)
# registro clasico donde almacenaremos los resultados
cr=ClassicalRegister(3)
circuit=QuantumCircuit(qr,cr)
# herramientas para la visuzaliacion
get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw()
# Transformada de Hadamard
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])

circuit.draw()
circuit.draw(output='mpl')

# aplicamos la query function
circuit.z(qr[0])
circuit.h(qr[2])
circuit.cx(qr[1],qr[2])
circuit.h(qr[2])

circuit.draw(output='mpl')
# transformada de hadamard
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])

circuit.draw(output='mpl')

circuit.measure(qr,cr)

circuit.draw(output='mpl')
# Procedemos a ejecutar en entorno ideal
simulator=Aer.get_backend('qasm_simulator')
result=execute(circuit,backend=simulator).result()
# visualizacion resultado
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))

from qiskit.tools.visualization import plot_bloch_multivector
plot_bloch_multivector(result.get_counts(circuit))

from qiskit.tools.visualization import plot_gate_map

plot_gate_map(result.get_counts(circuit))
# ejecucion en entorno real

IBMQ.load_account()
provider=IBMQ.get_provider('ibm-q')

qcomp=provider.get_backend('ibmq_london')

job=execute(circuit,backend=qcomp)

from qiskit.tools.monitor import job_monitor

job_monitor(job)
result=job.result()
plot_histogram(result.get_counts(circuit))
