#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from typing import List, NewType

PositiveInteger = NewType("PositiveInteger", int)

class OpEquipment(object):
	@property
	def NumberOfStationTracks(self) -> PositiveInteger:
		return self.___numberOfStationTracks
	@property
	def OwnsPlatform(self) -> tElementWithIDref:
		return self.___ownsPlatform
	@property
	def OwnsTrack(self) -> tElementWithIDref:
		return self.___ownsTrack
	@property
	def OwnsSignal(self) -> tElementWithIDref:
		return self.___ownsSignal
	@property
	def OwnsStoppingPlace(self) -> tElementWithIDref:
		return self.___ownsStoppingPlace
	@property
	def OwnsServiceSection(self) -> tElementWithIDref:
		return self.___ownsServiceSection

	@NumberOfStationTracks.setter
	def NumberOfStationTracks(self, aNumberOfStationTracks : PositiveInteger):
		self.___numberOfStationTracks = aNumberOfStationTracks
	@OwnsPlatform.setter
	def OwnsPlatform(self, aOwnsPlatform : tElementWithIDref):
		self.___ownsPlatform = aOwnsPlatform
	@OwnsTrack.setter
	def OwnsTrack(self, aOwnsTrack : tElementWithIDref):
		self.___ownsTrack = aOwnsTrack
	@OwnsSignal.setter
	def OwnsSignal(self, aOwnsSignal : tElementWithIDref):
		self.___ownsSignal = aOwnsSignal
	@OwnsStoppingPlace.setter
	def OwnsStoppingPlace(self, aOwnsStoppingPlace : tElementWithIDref):
		self.___ownsStoppingPlace = aOwnsStoppingPlace
	@OwnsServiceSection.setter
	def OwnsServiceSection(self, aOwnsServiceSection : tElementWithIDref):
		self.___ownsServiceSection = aOwnsServiceSection

	def create_OwnsPlatform(self):
		if self.OwnsPlatform == None:
			self.OwnsPlatform = []
		self.OwnsPlatform.append(tElementWithIDref.tElementWithIDref())
	def create_OwnsTrack(self):
		if self.OwnsTrack == None:
			self.OwnsTrack = []
		self.OwnsTrack.append(tElementWithIDref.tElementWithIDref())
	def create_OwnsSignal(self):
		if self.OwnsSignal == None:
			self.OwnsSignal = []
		self.OwnsSignal.append(tElementWithIDref.tElementWithIDref())
	def create_OwnsStoppingPlace(self):
		if self.OwnsStoppingPlace == None:
			self.OwnsStoppingPlace = []
		self.OwnsStoppingPlace.append(tElementWithIDref.tElementWithIDref())
	def create_OwnsServiceSection(self):
		if self.OwnsServiceSection == None:
			self.OwnsServiceSection = []
		self.OwnsServiceSection.append(tElementWithIDref.tElementWithIDref())

	def __init__(self):
		self.___numberOfStationTracks : PositiveInteger = None
		"""number of tracks that are available for operation within the operational point"""
		self.___ownsPlatform : tElementWithIDref =None
		"""reference to a platform element that belongs to the operational point"""
		self.___ownsTrack : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a track element that belongs to the operational point"""
		self.___ownsSignal : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a signal element that belongs to the operational point"""
		self.___ownsStoppingPlace : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a stopping place element that belongs to the operational point"""
		self.___ownsServiceSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a service section element that belongs to the operational point"""

