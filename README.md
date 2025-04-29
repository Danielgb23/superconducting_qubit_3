# Third research internship at LFDQ (quantum devices physics laboratory) UNICAMP
On this internship I measured  physical transmon superconducting qubits devices to caracterize their decoherence through finding estimates to their T<sub>1</sub> and T<sub>2</sub>. I also simulated the procedures of measurement to deepen my understanding of them and pinpoint the effects of each kind of fault of the system on the results of the caracterization, like noise on the qubit drive or the qubit's temperature.

You can read the partial report of the first semester [here](https://github.com/Danielgb23/superconducting_qubit_3/blob/main/Daniel_G_Benvenutti_partial_report.pdf). The partial report has more details on each measurement on the physical device that I had to take out of the final report because of the size constraints.

The TIIQx folders have the data and the notebooks used for the measurment (Measurement_pulsado.ipynb and Measurement_vna.ipynb) of each qubit sample I characterized on this internship as well as the notebook to generate the graphs for my report using this data (Qx Load_files.ipynb). The pyvisa scripts used in these notebooks to control the equipment can be found at the [laboratory's github](https://github.com/Rouxinol-Research-Lab/MeasurementsLFDQ). There's also [my fork](https://github.com/Danielgb23/MeasurementsLFDQ/tree/main) with some modifications.



The notebooks for the simulations are [measurement procedure with collapse operators](https://github.com/Danielgb23/superconducting_qubit_3/blob/main/Daniel-simulation-qubit.ipynb) where I simulate the process of caracterizing the qubit's relaxation and dephasing gaining insights on it and [noisy drive decoherence effects](https://github.com/Danielgb23/superconducting_qubit_3/blob/main/Daniel_simulation_qubit_drive_noise.ipynb) where I pinpoint the effects of a white background noise noise on the drive of the qubit.

## Samples from the work done:
### Simulation Rabi map:
![image](https://github.com/user-attachments/assets/eb94d3c3-6af3-45e0-8cba-cf311b76e200)

### Real qubit Rabi map:
![image](https://github.com/user-attachments/assets/86db4298-5832-4630-af4d-ffa4c359eeb7)


### Simulation Ramsey map:
![image](https://github.com/user-attachments/assets/8a878d19-0669-43c1-bd48-6917e2996799)

### Real qubit Ramsey map:
![image](https://github.com/user-attachments/assets/b1b75d5c-3ed6-4628-91de-09190169f7ac)



