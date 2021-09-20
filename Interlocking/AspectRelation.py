#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour
from RailML.Interlocking import SignalAndAspect, EntityILref, EntityIL
from typing import List, NewType
Duration = NewType("Duration", int)

class AspectRelation(EntityIL.EntityIL):
	"""One aspect relation has a) one master signal showing a given aspect b) one or more slaves showing a given aspect. The slave aspect depends on the master aspect. c) an optional overlap when the master aspect is at danger. The path from slave to master may contain switches. The switch positions are given in order to unequivocally determine the path."""
	@property
	def PassingSpeed(self) -> tSpeedKmPerHour:
		return self.___passingSpeed
	@property
	def ExpectingSpeed(self) -> tSpeedKmPerHour:
		return self.___expectingSpeed
	@property
	def EndSectionTime(self) -> Duration:
		return self.___endSectionTime
	@property
	def MasterAspect(self) -> SignalAndAspect:
		return self.___masterAspect
	@property
	def SlaveAspect(self) -> SignalAndAspect:
		return self.___slaveAspect
	@property
	def DistantAspect(self) -> SignalAndAspect:
		return self.___distantAspect
	@property
	def SignalsSpeedProfile(self) -> EntityILref:
		return self.___signalsSpeedProfile
	@property
	def AppliesToRoute(self) -> EntityILref:
		return self.___appliesToRoute

	@PassingSpeed.setter
	def PassingSpeed(self, aPassingSpeed : tSpeedKmPerHour):
		self.___passingSpeed = aPassingSpeed
	@ExpectingSpeed.setter
	def ExpectingSpeed(self, aExpectingSpeed : tSpeedKmPerHour):
		self.___expectingSpeed = aExpectingSpeed
	@EndSectionTime.setter
	def EndSectionTime(self, aEndSectionTime : Duration):
		self.___endSectionTime = aEndSectionTime
	@MasterAspect.setter
	def MasterAspect(self, aMasterAspect : SignalAndAspect):
		self.___masterAspect = aMasterAspect
	@SlaveAspect.setter
	def SlaveAspect(self, aSlaveAspect : SignalAndAspect):	# TODO *aSlaveAspect
		self.___slaveAspect = aSlaveAspect
	@DistantAspect.setter
	def DistantAspect(self, aDistantAspect : SignalAndAspect):
		self.___distantAspect = aDistantAspect
	@SignalsSpeedProfile.setter
	def SignalsSpeedProfile(self, aSignalsSpeedProfile : EntityILref):	# TODO *aSignalsSpeedProfile
		self.___signalsSpeedProfile = aSignalsSpeedProfile
	@AppliesToRoute.setter
	def AppliesToRoute(self, aAppliesToRoute : EntityILref):
		self.___appliesToRoute = aAppliesToRoute

	def create_MasterAspect(self):
		self.MasterAspect = SignalAndAspect.SignalAndAspect()
	def create_SlaveAspect(self):
		self.SlaveAspect = SignalAndAspect.SignalAndAspect()
	def create_DistantAspect(self):
		if self.DistantAspect == None:
			self.DistantAspect = []
		self.DistantAspect.append(SignalAndAspect.SignalAndAspect())
	def create_SignalsSpeedProfile(self):
		if self.SignalsSpeedProfile == None:
			self.SignalsSpeedProfile = []
		self.SignalsSpeedProfile.append(EntityILref.EntityILref())
	def create_AppliesToRoute(self):
		if self.AppliesToRoute == None:
			self.AppliesToRoute = []
		self.AppliesToRoute.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___passingSpeed : tSpeedKmPerHour = None
		"""The speed in km/h signalled by the slave aspect, i.e. the speed that the train must respect when passing the slave signal (at route entry)."""
		self.___expectingSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		# """Maximum signalled speed in km/h at master signal (aka target speed)."""
		self.___endSectionTime : Duration = 0
		"""The end-section of a route is the section between the closed route exit signal and the previous slave signal. Commonly, the interlocking revokes (part of) the route when this time period is passed."""
		self.___masterAspect : SignalAndAspect = None
		"""The combination of the master signal (at route exit) and the aspect it is showing."""
		self.___slaveAspect : SignalAndAspect = None
		# @AssociationType Interlocking.SignalAndAspect*
		# @AssociationMultiplicity 0..*
		# """The combination of the slave signal (at route entry) and the aspect it is showing."""
		self.___distantAspect : SignalAndAspect = None
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 0..1
		# """The combination of the master's distant signal (within the route or its start) and the aspect it is showing. This includes also any repeaters."""
		self.___signalsSpeedProfile : EntityILref = None
		"""The reference to a SpeedSection in infrastructure applicable for the signalled section."""
		self.___appliesToRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the related routes using the particular aspect relation."""