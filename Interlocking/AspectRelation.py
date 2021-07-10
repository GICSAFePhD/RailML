#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tSpeedKmPerHour
from Interlocking import SignalAndAspect
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class AspectRelation(EntityIL):
	"""One aspect relation has a) one master signal showing a given aspect b) one or more slaves showing a given aspect. The slave aspect depends on the master aspect. c) an optional overlap when the master aspect is at danger. The path from slave to master may contain switches. The switch positions are given in order to unequivocally determine the path."""
	def setPassingSpeed(self, aPassingSpeed : tSpeedKmPerHour):
		self.___passingSpeed = aPassingSpeed

	def getPassingSpeed(self) -> tSpeedKmPerHour:
		return self.___passingSpeed

	def setExpectingSpeed(self, aExpectingSpeed : tSpeedKmPerHour):
		self.___expectingSpeed = aExpectingSpeed

	def getExpectingSpeed(self) -> tSpeedKmPerHour:
		return self.___expectingSpeed

	def setEndSectionTime(self, aEndSectionTime : duration):
		self.___endSectionTime = aEndSectionTime

	def getEndSectionTime(self) -> duration:
		return self.___endSectionTime

	def setMasterAspect(self, aMasterAspect : SignalAndAspect):
		self._masterAspect = aMasterAspect

	def getMasterAspect(self) -> SignalAndAspect:
		return self._masterAspect

	def setSlaveAspect(self, *aSlaveAspect : SignalAndAspect*):
		self._slaveAspect = aSlaveAspect

	def getSlaveAspect(self) -> SignalAndAspect*:
		return self._slaveAspect

	def setDistantAspect(self, aDistantAspect : SignalAndAspect):
		self._distantAspect = aDistantAspect

	def getDistantAspect(self) -> SignalAndAspect:
		return self._distantAspect

	def setSignalsSpeedProfile(self, *aSignalsSpeedProfile : EntityILref*):
		self._signalsSpeedProfile = aSignalsSpeedProfile

	def getSignalsSpeedProfile(self) -> EntityILref*:
		return self._signalsSpeedProfile

	def setAppliesToRoute(self, aAppliesToRoute : EntityILref):
		self._appliesToRoute = aAppliesToRoute

	def getAppliesToRoute(self) -> EntityILref:
		return self._appliesToRoute

	def __init__(self):
		self.___passingSpeed : tSpeedKmPerHour = None
		"""The speed in km/h signalled by the slave aspect, i.e. the speed that the train must respect when passing the slave signal (at route entry)."""
		self.___expectingSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		# """Maximum signalled speed in km/h at master signal (aka target speed)."""
		self.___endSectionTime : duration = None
		"""The end-section of a route is the section between the closed route exit signal and the previous slave signal. Commonly, the interlocking revokes (part of) the route when this time period is passed."""
		self._masterAspect : SignalAndAspect = None
		"""The combination of the master signal (at route exit) and the aspect it is showing."""
		self._slaveAspect : SignalAndAspect = None
		# @AssociationType Interlocking.SignalAndAspect*
		# @AssociationMultiplicity 0..*
		# """The combination of the slave signal (at route entry) and the aspect it is showing."""
		self._distantAspect : SignalAndAspect = None
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 0..1
		# """The combination of the master's distant signal (within the route or its start) and the aspect it is showing. This includes also any repeaters."""
		self._signalsSpeedProfile : EntityILref = None
		"""The reference to a SpeedSection in infrastructure applicable for the signalled section."""
		self._appliesToRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the related routes using the particular aspect relation."""

