#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tTrackType, tExtendedDirection, Length, FunctionalInfrastructureEntity
from typing import List

class Track(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	"""A Track is defined by a railway section between two switches/crossings or between a switch/crossing and a buffer stop."""
	@property
	def Type(self) -> tTrackType:
		return self.___type
	@property
	def InfrastructureManagerRef(self) -> tRef:
		return self.___infrastructureManagerRef
	@property
	def MainDirection(self) -> tExtendedDirection:
		return self.___mainDirection
	@property
	def TrackBegin(self) -> tElementWithIDref:
		return self.___trackBegin
	@property
	def TrackEnd(self) -> tElementWithIDref:
		return self.___trackEnd
	@property
	def Length(self) -> Length:
		return self.___length

	@Type.setter
	def Type(self, aType : tTrackType):
		self.___type = aType
	@InfrastructureManagerRef.setter
	def InfrastructureManagerRef(self, aInfrastructureManagerRef : tRef):
		self.___infrastructureManagerRef = aInfrastructureManagerRef
	@MainDirection.setter
	def MainDirection(self, aMainDirection : tExtendedDirection):
		self.___mainDirection = aMainDirection
	@TrackBegin.setter
	def TrackBegin(self, aTrackBegin : tElementWithIDref):
		self.___trackBegin = aTrackBegin
	@TrackEnd.setter
	def TrackEnd(self, aTrackEnd : tElementWithIDref):
		self.___trackEnd = aTrackEnd
	@Length.setter
	def Length(self, *aLength : Length):
		self.___length = aLength

	def __init__(self):
		self.___type : tTrackType = tTrackType.tTrackType()
		# @AssociationType Infrastructure.tTrackType
		# """type of the track defining the general functionality of the track"""
		self.___infrastructureManagerRef : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to the infrastructure manager who owns the track (see <organizationalUnits> in <common>)"""
		self.___mainDirection : tExtendedDirection = tExtendedDirection.tExtendedDirection()
		# @AssociationType Infrastructure.tExtendedDirection
		# """predominant direction of operation on this track;
		# use this attribute to define the default direction of train operations, especially on double track lines"""
		self.___trackBegin : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		"""reference to a track node (buffer stop, switch, etc.) that marks the begin of the track"""
		self.___trackEnd : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to a track node (buffer stop, switch, etc.) that marks the end of the track"""
		self.___length : Length = Length.Length()
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 1..*
		# """length of track in metres"""

