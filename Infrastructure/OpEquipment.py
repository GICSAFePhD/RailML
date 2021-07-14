#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tElementWithIDref import tElementWithIDref
from typing import List

class OpEquipment(object):
	def setNumberOfStationTracks(self, aNumberOfStationTracks : int): #TODO DEFINED AS POSITIVEINTEGER
		self.___numberOfStationTracks = aNumberOfStationTracks

	def getNumberOfStationTracks(self) -> int:	#TODO DEFINED AS POSITIVEINTEGER
		return self.___numberOfStationTracks

	def setOwnsPlatform(self, *aOwnsPlatform : tElementWithIDref):
		self._ownsPlatform = aOwnsPlatform

	def getOwnsPlatform(self) -> tElementWithIDref:
		return self._ownsPlatform

	def setOwnsTrack(self, *aOwnsTrack : tElementWithIDref):
		self._ownsTrack = aOwnsTrack

	def getOwnsTrack(self) -> tElementWithIDref:
		return self._ownsTrack

	def setOwnsSignal(self, *aOwnsSignal : tElementWithIDref):
		self._ownsSignal = aOwnsSignal

	def getOwnsSignal(self) -> tElementWithIDref:
		return self._ownsSignal

	def setOwnsStoppingPlace(self, *aOwnsStoppingPlace : tElementWithIDref):
		self._ownsStoppingPlace = aOwnsStoppingPlace

	def getOwnsStoppingPlace(self) -> tElementWithIDref:
		return self._ownsStoppingPlace

	def setOwnsServiceSection(self, *aOwnsServiceSection : tElementWithIDref):
		self._ownsServiceSection = aOwnsServiceSection

	def getOwnsServiceSection(self) -> tElementWithIDref:
		return self._ownsServiceSection

	def __init__(self):
		self.___numberOfStationTracks : int = None	#TODO DEFINED AS POSITIVEINTEGER
		"""number of tracks that are available for operation within the operational point"""
		self._ownsPlatform : tElementWithIDref = None
		"""reference to a platform element that belongs to the operational point"""
		self._ownsTrack : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a track element that belongs to the operational point"""
		self._ownsSignal : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a signal element that belongs to the operational point"""
		self._ownsStoppingPlace : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a stopping place element that belongs to the operational point"""
		self._ownsServiceSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a service section element that belongs to the operational point"""

