#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tTrainRadioSystemExt import tTrainRadioSystemExt
from RailML.Infrastructure.tTrainRadioNetworkSelectionExt import tTrainRadioNetworkSelectionExt
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class TrainRadio(FunctionalInfrastructureEntity):
	def setSupportsBroadcastCalls(self, aSupportsBroadcastCalls : int):	#TODO DEFINED AS LONG
		self.___supportsBroadcastCalls = aSupportsBroadcastCalls

	def getSupportsBroadcastCalls(self) -> int:	#TODO DEFINED AS LONG
		return self.___supportsBroadcastCalls

	def setSupportsDirectMode(self, aSupportsDirectMode : int):	#TODO DEFINED AS LONG
		self.___supportsDirectMode = aSupportsDirectMode

	def getSupportsDirectMode(self) -> int:	#TODO DEFINED AS LONG
		return self.___supportsDirectMode

	def setSupportsPublicEmergency(self, aSupportsPublicEmergency : int):	#TODO DEFINED AS LONG
		self.___supportsPublicEmergency = aSupportsPublicEmergency

	def getSupportsPublicEmergency(self) -> int:	#TODO DEFINED AS LONG
		return self.___supportsPublicEmergency

	def setSupportsPublicNetworkRoaming(self, aSupportsPublicNetworkRoaming : int):	#TODO DEFINED AS LONG
		self.___supportsPublicNetworkRoaming = aSupportsPublicNetworkRoaming

	def getSupportsPublicNetworkRoaming(self) -> int:	#TODO DEFINED AS LONG
		return self.___supportsPublicNetworkRoaming

	def setRadioSystem(self, aRadioSystem : tTrainRadioSystemExt):
		self.___radioSystem = aRadioSystem

	def getRadioSystem(self) -> tTrainRadioSystemExt:
		return self.___radioSystem

	def setSupportsTextMessageService(self, aSupportsTextMessageService : int):		#TODO DEFINED AS LONG
		self.___supportsTextMessageService = aSupportsTextMessageService

	def getSupportsTextMessageService(self) -> int:	#TODO DEFINED AS LONG
		return self.___supportsTextMessageService

	def setNetworkSelection(self, aNetworkSelection : tTrainRadioNetworkSelectionExt):
		self.___networkSelection = aNetworkSelection

	def getNetworkSelection(self) -> tTrainRadioNetworkSelectionExt:
		return self.___networkSelection

	def __init__(self):
		self.___supportsBroadcastCalls : int = None	#TODO DEFINED AS LONG
		"""defines whether broadcast call functionality is available"""
		self.___supportsDirectMode : int = None	#TODO DEFINED AS LONG
		"""defines whether direct mode train radio is available"""
		self.___supportsPublicEmergency : int = None	#TODO DEFINED AS LONG
		"""defines whether public emergency calls are available"""
		self.___supportsPublicNetworkRoaming : int = None	#TODO DEFINED AS LONG
		"""defines whether roaming via public networks is available"""
		self.___radioSystem : tTrainRadioSystemExt = None
		# @AssociationType Infrastructure.tTrainRadioSystemExt
		# """the train radio system, e.g. 'GSM-R'"""
		self.___supportsTextMessageService : int = None	#TODO DEFINED AS LONG
		"""defines whether text message service (SMS) is available"""
		self.___networkSelection : tTrainRadioNetworkSelectionExt = None
		# @AssociationType Infrastructure.tTrainRadioNetworkSelectionExt
		# """defines the procedure of train radio network selection"""

