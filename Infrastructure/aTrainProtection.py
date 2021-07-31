#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tTrainProtectionMedium, tTrainProtectionMonitoring, TrainProtectionElement #TODO CIRCULAR!
from typing import List

class aTrainProtection(object):
	@property
	def TrainProtectionSystem(self) -> str:
		return self.___trainProtectionSystem
	@property
	def tTrainProtectionMedium(self) -> tTrainProtectionMedium:
		return self.___medium
	@property
	def tTrainProtectionMonitoring(self) -> tTrainProtectionMonitoring:
		return self.___monitoring
	@property
	def TrainProtectionElement(self) -> TrainProtectionElement:
		return self.___unnamed_TrainProtectionElement

	@TrainProtectionSystem.setter
	def TrainProtectionSystem(self, aTrainProtectionSystem : str):
		self.___trainProtectionSystem = aTrainProtectionSystem
	@tTrainProtectionMedium.setter
	def tTrainProtectionMedium(self, atTrainProtectionMedium : tTrainProtectionMedium):
		self.___medium = atTrainProtectionMedium
	@tTrainProtectionMonitoring.setter
	def tTrainProtectionMonitoring(self, atTrainProtectionMonitoring : tTrainProtectionMonitoring):
		self.___monitoring = atTrainProtectionMonitoring
	@TrainProtectionElement.setter
	def TrainProtectionElement(self, aTrainProtectionElement : TrainProtectionElement):
		self.___unnamed_TrainProtectionElement = aTrainProtectionElement

	def __init__(self):
		self.___trainProtectionSystem : str = ""
		"""definition of the national train protection system, which is installed at the track;
		use value from the separate codelist file 'TrainProtectionSystems.xml'/trainProtectionSystemsAtTrack"""
		self.___medium : tTrainProtectionMedium = tTrainProtectionMedium.tTrainProtectionMedium()
		# @AssociationType Infrastructure.tTrainProtectionMedium
		# """the medium for transferring the control command from the interlocking unit to the train protection field element, e.g. "inductive" for magnets"""
		self.___monitoring : tTrainProtectionMonitoring = tTrainProtectionMonitoring.tTrainProtectionMonitoring()
		# @AssociationType Infrastructure.tTrainProtectionMonitoring
		# """the way how the train protection field element is communicating with the monitoring central interlocking unit"""
		self.___unnamed_TrainProtectionElement : TrainProtectionElement = None	#TODO CIRCULAR!

