#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tTrainRadioSystemExt, tTrainRadioNetworkSelectionExt, FunctionalInfrastructureEntity
from typing import List, NewType

Long = NewType("Long", int)

class TrainRadio(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def SupportsBroadcastCalls(self) -> Long:
		return self.___supportsBroadcastCalls
	@property
	def SupportsDirectMode(self) -> Long:
		return self.___supportsDirectMode
	@property
	def SupportsPublicEmergency(self) -> Long:
		return self.___supportsPublicEmergency
	@property
	def SupportsPublicNetworkRoaming(self) -> Long:
		return self.___supportsPublicNetworkRoaming
	@property
	def RadioSystem(self) -> tTrainRadioSystemExt:
		return self.___radioSystem
	@property
	def SupportsTextMessageService(self) -> Long:
		return self.___supportsTextMessageService
	@property
	def NetworkSelection(self) -> tTrainRadioNetworkSelectionExt:
		return self.___networkSelection

	@SupportsBroadcastCalls.setter
	def SupportsBroadcastCalls(self, aSupportsBroadcastCalls : Long):
		self.___supportsBroadcastCalls = aSupportsBroadcastCalls
	@SupportsDirectMode.setter
	def SupportsDirectMode(self, aSupportsDirectMode : Long):
		self.___supportsDirectMode = aSupportsDirectMode
	@SupportsPublicEmergency.setter
	def SupportsPublicEmergency(self, aSupportsPublicEmergency : Long):
		self.___supportsPublicEmergency = aSupportsPublicEmergency
	@SupportsPublicNetworkRoaming.setter
	def SupportsPublicNetworkRoaming(self, aSupportsPublicNetworkRoaming : Long):
		self.___supportsPublicNetworkRoaming = aSupportsPublicNetworkRoaming
	@RadioSystem.setter
	def RadioSystem(self, aRadioSystem : tTrainRadioSystemExt):
		self.___radioSystem = aRadioSystem
	@SupportsTextMessageService.setter
	def SupportsTextMessageService(self, aSupportsTextMessageService : Long):
		self.___supportsTextMessageService = aSupportsTextMessageService
	@NetworkSelection.setter
	def NetworkSelection(self, aNetworkSelection : tTrainRadioNetworkSelectionExt):
		self.___networkSelection = aNetworkSelection

	def __init__(self):
		self.___supportsBroadcastCalls : Long = 0
		"""defines whether broadcast call functionality is available"""
		self.___supportsDirectMode : Long = 0
		"""defines whether direct mode train radio is available"""
		self.___supportsPublicEmergency : Long = 0
		"""defines whether public emergency calls are available"""
		self.___supportsPublicNetworkRoaming : Long = 0
		"""defines whether roaming via public networks is available"""
		self.___radioSystem : tTrainRadioSystemExt = None
		# @AssociationType Infrastructure.tTrainRadioSystemExt
		# """the train radio system, e.g. 'GSM-R'"""
		self.___supportsTextMessageService : Long = 0
		"""defines whether text message service (SMS) is available"""
		self.___networkSelection : tTrainRadioNetworkSelectionExt = None
		# @AssociationType Infrastructure.tTrainRadioNetworkSelectionExt
		# """defines the procedure of train radio network selection"""

