#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour, tLengthM
from RailML.Interlocking import tSignalFunctionListExt, EntityILref, TrackAsset
from typing import List, NewType

Long = NewType("Long", int)
Duration = NewType("Duration", int)

class SignalIL(TrackAsset.TrackAsset):
	"""A signal has an identity attribute, a reference to a signal or sign defined in the RTM scheme. A sign (or ETCS markerboard) indicating a speed change may well be modelled as a signal because the interlocking is likely to issue a different speed code at that sign"""
	@property
	def ReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed
	@property
	def MalfunctionSpeed(self) -> tSpeedKmPerHour:
		return self.___malfunctionSpeed
	@property
	def ApproachSpeed(self) -> tSpeedKmPerHour:
		return self.___approachSpeed
	@property
	def PassingSpeed(self) -> tSpeedKmPerHour:
		return self.___passingSpeed
	@property
	def ReleaseDelay(self) -> Duration:
		return self.___releaseDelay
	@property
	def Function(self) -> tSignalFunctionListExt:
		return self.___function
	@property
	def IsVirtual(self) -> Long:
		return self.___isVirtual
	@property
	def CallOnAspectTime(self) -> Duration:
		return self.___callOnAspectTime
	@property
	def SightDistance(self) -> tLengthM:
		return self.___sightDistance
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo
	@property
	def ProtectsBlockExit(self) -> EntityILref:
		return self.___protectsBlockExit

	@ReleaseSpeed.setter
	def ReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed
	@MalfunctionSpeed.setter
	def MalfunctionSpeed(self, aMalfunctionSpeed : tSpeedKmPerHour):
		self.___malfunctionSpeed = aMalfunctionSpeed
	@ApproachSpeed.setter
	def ApproachSpeed(self, aApproachSpeed : tSpeedKmPerHour):
		self.___approachSpeed = aApproachSpeed
	@PassingSpeed.setter
	def PassingSpeed(self, aPassingSpeed : tSpeedKmPerHour):
		self.___passingSpeed = aPassingSpeed
	@ReleaseDelay.setter
	def ReleaseDelay(self, aReleaseDelay : Duration):
		self.___releaseDelay = aReleaseDelay
	@Function.setter
	def Function(self, aFunction : tSignalFunctionListExt):
		self.___function = aFunction
	@IsVirtual.setter
	def IsVirtual(self, aIsVirtual : Long):
		self.___isVirtual = aIsVirtual
	@CallOnAspectTime.setter
	def CallOnAspectTime(self, aCallOnAspectTime : Duration):
		self.___callOnAspectTime = aCallOnAspectTime
	@SightDistance.setter
	def SightDistance(self, aSightDistance : tLengthM):
		self.___sightDistance = aSightDistance
	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref):
		self.___refersTo = aRefersTo
	@ProtectsBlockExit.setter
	def ProtectsBlockExit(self, aProtectsBlockExit : EntityILref):
		self.___protectsBlockExit = aProtectsBlockExit

	def create_RefersTo(self):
		self.RefersTo = EntityILref.EntityILref()
	def create_ProtectsBlockExit(self):
		if self.ProtectsBlockExit == None:
			self.ProtectsBlockExit = []
		self.ProtectsBlockExit.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___releaseSpeed : tSpeedKmPerHour = None
		"""Release speed in km/h from controlled braking curve."""
		self.___malfunctionSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """This constant indicates the maximum speed in km/h with which a train may travel past a failed signal. The malfunctioning signal cannot be opened."""
		self.___approachSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """The maximum speed in km/h with which a train can approach the signal. This matches the Ka of the previous (=upstream) signal or speed sign. This is suitable for defining the line speed profile."""
		self.___passingSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		# """Maximum speed in km/h beyond the signal. This is suitable for defining the line speed profile."""
		self.___releaseDelay : Duration = None
		"""Time to elapse between receiving the revocation command and before route release."""
		self.___function : tSignalFunctionListExt = None
		# @AssociationType Interlocking.tSignalFunctionListExt
		# """Function of the signal for usage by the interlocking. This is in addition to signalType in infrastructure."""
		self.___isVirtual : Long = None
		"""Often, users label signals virtual. A virtual signal can be a dummy-signal that is a software object in the interlocking but has no physical trackside presence. Such virtual signals can be useful for modelling speed steps; there need not be a physical signal but the interlocking enforces a different speed at the position of the virtual signal. The other way round, stand-alone boards that are not wired to the interlocking can be labelled virtual. Such stand-alone signals are of interest to simulations because when they affect driver behaviour thus influence train runs."""
		self.___callOnAspectTime : Duration = None
		"""time for duration to show call-on aspect on this signal"""
		self.___sightDistance : tLengthM = None
		# @AssociationType Common.tLengthM
		# """The distance in metres the signal is visible in advance by the train driver. This might influence reaction times on changing aspects for simulation."""
		self.___refersTo : EntityILref = None
		"""The reference to the physical trackside signal."""
		self.___protectsBlockExit : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1