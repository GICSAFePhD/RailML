#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tTrainRadioSystemExt
from Infrastructure import tTrainRadioNetworkSelectionExt
from Infrastructure import FunctionalInfrastructureEntity
from typing import List

class TrainRadio(FunctionalInfrastructureEntity):
	def setSupportsBroadcastCalls(self, aSupportsBroadcastCalls : long):
		self.___supportsBroadcastCalls = aSupportsBroadcastCalls

	def getSupportsBroadcastCalls(self) -> long:
		return self.___supportsBroadcastCalls

	def setSupportsDirectMode(self, aSupportsDirectMode : long):
		self.___supportsDirectMode = aSupportsDirectMode

	def getSupportsDirectMode(self) -> long:
		return self.___supportsDirectMode

	def setSupportsPublicEmergency(self, aSupportsPublicEmergency : long):
		self.___supportsPublicEmergency = aSupportsPublicEmergency

	def getSupportsPublicEmergency(self) -> long:
		return self.___supportsPublicEmergency

	def setSupportsPublicNetworkRoaming(self, aSupportsPublicNetworkRoaming : long):
		self.___supportsPublicNetworkRoaming = aSupportsPublicNetworkRoaming

	def getSupportsPublicNetworkRoaming(self) -> long:
		return self.___supportsPublicNetworkRoaming

	def setRadioSystem(self, aRadioSystem : tTrainRadioSystemExt):
		self.___radioSystem = aRadioSystem

	def getRadioSystem(self) -> tTrainRadioSystemExt:
		return self.___radioSystem

	def setSupportsTextMessageService(self, aSupportsTextMessageService : long):
		self.___supportsTextMessageService = aSupportsTextMessageService

	def getSupportsTextMessageService(self) -> long:
		return self.___supportsTextMessageService

	def setNetworkSelection(self, aNetworkSelection : tTrainRadioNetworkSelectionExt):
		self.___networkSelection = aNetworkSelection

	def getNetworkSelection(self) -> tTrainRadioNetworkSelectionExt:
		return self.___networkSelection

	def __init__(self):
		self.___supportsBroadcastCalls : long = None
		"""defines whether broadcast call functionality is available"""
		self.___supportsDirectMode : long = None
		"""defines whether direct mode train radio is available"""
		self.___supportsPublicEmergency : long = None
		"""defines whether public emergency calls are available"""
		self.___supportsPublicNetworkRoaming : long = None
		"""defines whether roaming via public networks is available"""
		self.___radioSystem : tTrainRadioSystemExt = None
		# @AssociationType Infrastructure.tTrainRadioSystemExt
		# """the train radio system, e.g. 'GSM-R'"""
		self.___supportsTextMessageService : long = None
		"""defines whether text message service (SMS) is available"""
		self.___networkSelection : tTrainRadioNetworkSelectionExt = None
		# @AssociationType Infrastructure.tTrainRadioNetworkSelectionExt
		# """defines the procedure of train radio network selection"""

