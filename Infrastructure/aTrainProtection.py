#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tTrainProtectionMedium import tTrainProtectionMedium
from RailML.Infrastructure.tTrainProtectionMonitoring import tTrainProtectionMonitoring
#from RailML.Infrastructure.TrainProtectionElement import TrainProtectionElement #TODO CIRCULAR!
from typing import List

class aTrainProtection(object):
	def setTrainProtectionSystem(self, aTrainProtectionSystem : str):
		self.___trainProtectionSystem = aTrainProtectionSystem

	def getTrainProtectionSystem(self) -> str:
		return self.___trainProtectionSystem

	def setMedium(self, aMedium : tTrainProtectionMedium):
		self.___medium = aMedium

	def getMedium(self) -> tTrainProtectionMedium:
		return self.___medium

	def setMonitoring(self, aMonitoring : tTrainProtectionMonitoring):
		self.___monitoring = aMonitoring

	def getMonitoring(self) -> tTrainProtectionMonitoring:
		return self.___monitoring

	def __init__(self):
		self.___trainProtectionSystem : str = None
		"""definition of the national train protection system, which is installed at the track;
		use value from the separate codelist file 'TrainProtectionSystems.xml'/trainProtectionSystemsAtTrack"""
		self.___medium : tTrainProtectionMedium = None
		# @AssociationType Infrastructure.tTrainProtectionMedium
		# """the medium for transferring the control command from the interlocking unit to the train protection field element, e.g. "inductive" for magnets"""
		self.___monitoring : tTrainProtectionMonitoring = None
		# @AssociationType Infrastructure.tTrainProtectionMonitoring
		# """the way how the train protection field element is communicating with the monitoring central interlocking unit"""
		#self._unnamed_TrainProtectionElement_ : TrainProtectionElement = None	#TODO CIRCULAR!

