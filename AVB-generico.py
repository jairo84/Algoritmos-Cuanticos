#!/usr/bin/env python
# coding: utf-8

# In[1]:
from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram

# In[2]:
numero_secreto='1010101'
# In[4]:
circuit=QuantumCircuit(len(numero_secreto)+1,len(numero_secreto))

#aplicamos transformada de Hadamard al registro de entrada
circuit.h(range(len(numero_secreto)))

circuit.x(len(numero_secreto))
circuit.h(len(numero_secreto))

circuit.barrier()

for i, val in enumerate(reversed(numero_secreto)):
    if val=='1':
        circuit.cx(i,len(numero_secreto))

        
circuit.barrier()

circuit.h(range(len(numero_secreto)))

circuit.barrier()

circuit.measure(range(len(numero_secreto)),range(len(numero_secreto)))
# In[5]:
circuit.draw(output='mpl')
# In[6]:
simulador=Aer.get_backend('qasm_simulator')
res=execute(circuit,backend=simulador,shots=1).result()
plot_histogram(res.get_counts(circuit))
# In[8]:
IBMQ.load_account()
# In[9]:
provider=IBMQ.get_provider('ibm-q')
# In[10]:
qcomp=provider.get_backend('ibmq_16_melbourne')
# In[11]:
job=execute(circuit,backend=qcomp)
# In[12]:
from qiskit.tools.monitor import job_monitor
# In[13]:
job_monitor(job)
# In[14]:
resultado1=job.result()
# In[15]:
plot_histogram(resultado1.get_counts(circuit))
# In[16]:
job2=execute(circuit,backend=qcomp,shots=1)
# In[17]:
job_monitor(job2)
# In[18]:
resultado2=job2.result()
# In[19]:
plot_histogram(resultado2.get_counts(circuit))
