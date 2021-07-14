#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tTrackType import tTrackType
from RailML.Common.tRef import tRef
from RailML.Infrastructure.tExtendedDirection import tExtendedDirection
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.Length import Length
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class Track(FunctionalInfrastructureEntity):
	"""A Track is defined by a railway section between two switches/crossings or between a switch/crossing and a buffer stop."""
	def setType(self, aType : tTrackType):
		self.___type = aType

	def getType(self) -> tTrackType:
		return self.___type

	def setInfrastructureManagerRef(self, aInfrastructureManagerRef : tRef):
		self.___infrastructureManagerRef = aInfrastructureManagerRef

	def getInfrastructureManagerRef(self) -> tRef:
		return self.___infrastructureManagerRef

	def setMainDirection(self, aMainDirection : tExtendedDirection):
		self.___mainDirection = aMainDirection

	def getMainDirection(self) -> tExtendedDirection:
		return self.___mainDirection

	def setTrackBegin(self, aTrackBegin : tElementWithIDref):
		self._trackBegin = aTrackBegin

	def getTrackBegin(self) -> tElementWithIDref:
		return self._trackBegin

	def setTrackEnd(self, aTrackEnd : tElementWithIDref):
		self._trackEnd = aTrackEnd

	def getTrackEnd(self) -> tElementWithIDref:
		return self._trackEnd

	def setLength(self, *aLength : Length):
		self._length = aLength

	def getLength(self) -> Length:
		return self._length

	def __init__(self):
		self.___type : tTrackType = None
		# @AssociationType Infrastructure.tTrackType
		# """type of the track defining the general functionality of the track"""
		self.___infrastructureManagerRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to the infrastructure manager who owns the track (see <organizationalUnits> in <common>)"""
		self.___mainDirection : tExtendedDirection = None
		# @AssociationType Infrastructure.tExtendedDirection
		# """predominant direction of operation on this track;
		# use this attribute to define the default direction of train operations, especially on double track lines"""
		self._trackBegin : tElementWithIDref = None
		"""reference to a track node (buffer stop, switch, etc.) that marks the begin of the track"""
		self._trackEnd : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to a track node (buffer stop, switch, etc.) that marks the end of the track"""
		self._length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 1..*
		# """length of track in metres"""

