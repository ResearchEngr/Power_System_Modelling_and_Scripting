# -*- coding: utf-8 -*-
# Settings
from settings.settings import settings
from settings.sssa import sssa
from settings.cpf import cpf
from settings.opf import opf
# Variables
from variables.dae import dae
from variables.device import device
from variables.varout import varout
# Devices
from devices.bus import bus
from devices.line import line
from devices.pv import pv, slack
from devices.pq import pq
from devices.shunt import shunt
from devices.fault import fault
from devices.breaker import breaker
from devices.zone import zone
from devices.synchronous import syn2, syn3, syn4, syn5a, syn5b
from devices.synchronous import syn5c, syn5d, syn6a, syn6b
from devices.avr import avr1, avr2, avr3
from devices.turbine import tg1, tg2
from devices.pss import pss1, pss2, pss3

# list of all active devices
device_list = ['Bus', 'Area', 'Region', 'System', 'Line',
                'Shunt', 'Breaker', 'Fault', 'PV', 'SW', 'Syn2',
                'Syn3', 'Syn4', 'Syn5a', 'Syn5b', 'Syn5c', 'Syn5d',
                'Syn6a', 'Syn6b', 'Avr1', 'Avr2', 'Avr3', 'Tg1',
                'Tg2', 'Pss1', 'Pss2', 'Pss3']
                
# settings
Settings = settings() # power flow and time domain settings
SSSA = sssa()         # eigenvalue analysis settings
CPF = cpf()           # continuation power flow settings
OPF = opf()           # optimal power flow settings

# variables
DAE = dae()
Varname = varname()
Varout = varout()
Device = device(device_list)

# D E V I C E S

# basis power flow devices
Bus = bus()
Line = line()
SW = slack()
PV = pv()
PQ = pq()
Shunt = shunt()
Area = zone('Area')
Region = zone('Region')
System = zone('System')

# switches
Fault = fault()
Breaker = breaker()

# synchronous machines
Syn2 = syn2()       # machine models
Syn3 = syn3()
Syn4 = syn4()
Syn5a = syn5a()
Syn5b = syn5b()
Syn5c = syn5c()
Syn5d = syn5d()
Syn6a = syn6a()
Syn6b = syn6b()

# synchronous machines controls
Avr1 = avr1()       # automatic voltage regulators
Avr2 = avr2()
Avr3 = avr3()
Tg1 = tg1()         #turbine governors
Tg2 = tg2()
Pss1 = pss1()       # power system stabilizers
Pss2 = pss2()
Pss3 = pss3()