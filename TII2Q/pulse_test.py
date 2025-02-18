from measurements.waveforms.GaussianCosPulse import *
from measurements.DataChannelManager import * # Contém classe que gerencia os dados para serem carregados no AWG
from measurements.PulseSequence import * # Classe que estratura e sequencia os pulsos

# Diferentes tipos de pulsos que podem ser usados

from measurements.waveforms.SquarePulse import *
from measurements.waveforms.CosinePulse import *
from measurements.waveforms.SquareSideBandPulse import *
from measurements.waveforms.ZeroPulse import *
from measurements.waveforms.GaussianPulse import *
from measurements.waveforms.DragPulse import *
from measurements.waveforms.GaussianBorderCosPulse import *


# Define-se um pulso Zero
#p1 = GaussianBorderCosPulse(length = 1e-6, frequency = 4e9, amplitude = 1,sigma=1e-8,border_lenght=6)
p1 = GaussianCosPulse(length = 1e-6, frequency = 4e9, amplitude = 1,sigma=1e-7)
#p1 = CosinePulse(length = 1e-6, amplitude = 0.1)
#p1 = SquarePulse(length = 1e-6, amplitude = 1)
#p1 = GaussianPulse(length = 20e-6, amplitude = 1, sigma = 4e-6)
#p2 = ZeroPulse(length = RFMeasurementLength)

s1 = PulseSequence('Twotone', 10e-9)

s1.clear()

s1.add(p = p1, channel = 'I', delay = 0)
#s1.add(p = p2, channel = 'm')

PiPulse=0.7e-6

p1 = GaussianCosPulse(length = PiPulse/2,  amplitude = 0.4,sigma=0.15*PiPulse/2,frequency =4.4565e9 ,)
p1 = GaussianCosPulse(length = PiPulse/2,  amplitude = 0.4,sigma=0.15*PiPulse/2,frequency =4.4565e9 ,)

#p3 = SquareSideBandPulse(length = PiPulse/2, amplitude = 0.4,frequency=4.4565e9)
p3 = SquareSideBandPulse(length = PiPulse/2, amplitude = 0.4,frequency=4.4565e9)
#p3=p1
p2 = ZeroPulse(length = 5e-6)

s1 = PulseSequence('Twotone', 10e-9)
s1.clear()

s1.add(p = p3, channel = 'I', delay =5e-6)#+PiPulse/2)
s1.add(p = p3, channel = 'Q', delay = 7e-6)
s1.add(p = p2, channel = 'm')
s1.show_all()