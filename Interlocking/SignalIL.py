#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tSpeedKmPerHour import tSpeedKmPerHour
from RailML.Interlocking.tSignalFunctionListExt import tSignalFunctionListExt
from RailML.Common.tLengthM import tLengthM
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class SignalIL(TrackAsset):
	"""A signal has an identity attribute, a reference to a signal or sign defined in the RTM scheme. A sign (or ETCS markerboard) indicating a speed change may well be modelled as a signal because the interlocking is likely to issue a different speed code at that sign"""
	def setReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed

	def getReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed

	def setMalfunctionSpeed(self, aMalfunctionSpeed : tSpeedKmPerHour):
		self.___malfunctionSpeed = aMalfunctionSpeed

	def getMalfunctionSpeed(self) -> tSpeedKmPerHour:
		return self.___malfunctionSpeed

	def setApproachSpeed(self, aApproachSpeed : tSpeedKmPerHour):
		self.___approachSpeed = aApproachSpeed

	def getApproachSpeed(self) -> tSpeedKmPerHour:
		return self.___approachSpeed

	def setPassingSpeed(self, aPassingSpeed : tSpeedKmPerHour):
		self.___passingSpeed = aPassingSpeed

	def getPassingSpeed(self) -> tSpeedKmPerHour:
		return self.___passingSpeed

	def setReleaseDelay(self, aReleaseDelay : int):	#TODO DEFINED AS duration
		self.___releaseDelay = aReleaseDelay

	def getReleaseDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___releaseDelay

	def setFunction(self, aFunction : tSignalFunctionListExt):
		self.___function = aFunction

	def getFunction(self) -> tSignalFunctionListExt:
		return self.___function

	def setIsVirtual(self, aIsVirtual : int):	#TODO DEFINED AS LONG
		self.___isVirtual = aIsVirtual

	def getIsVirtual(self) -> int:	#TODO DEFINED AS LONG
		return self.___isVirtual

	def setCallOnAspectTime(self, aCallOnAspectTime : int):	#TODO DEFINED AS duration
		self.___callOnAspectTime = aCallOnAspectTime

	def getCallOnAspectTime(self) -> int:	#TODO DEFINED AS duration
		return self.___callOnAspectTime

	def setSightDistance(self, aSightDistance : tLengthM):
		self.___sightDistance = aSightDistance

	def getSightDistance(self) -> tLengthM:
		return self.___sightDistance

	def setRefersTo(self, aRefersTo : EntityILref):
		self._refersTo = aRefersTo

	def getRefersTo(self) -> EntityILref:
		return self._refersTo

	def setProtectsBlockExit(self, aProtectsBlockExit : EntityILref):
		self._protectsBlockExit = aProtectsBlockExit

	def getProtectsBlockExit(self) -> EntityILref:
		return self._protectsBlockExit

	def __init__(self):
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
		self.___releaseDelay : int = None	#TODO DEFINED AS duration
		"""Time to elapse between receiving the revocation command and before route release."""
		self.___function : tSignalFunctionListExt = None
		# @AssociationType Interlocking.tSignalFunctionListExt
		# """Function of the signal for usage by the interlocking. This is in addition to signalType in infrastructure."""
		self.___isVirtual : int = None	#TODO DEFINED AS LONG
		"""Often, users label signals virtual. A virtual signal can be a dummy-signal that is a software object in the interlocking but has no physical trackside presence. Such virtual signals can be useful for modelling speed steps; there need not be a physical signal but the interlocking enforces a different speed at the position of the virtual signal. The other way round, stand-alone boards that are not wired to the interlocking can be labelled virtual. Such stand-alone signals are of interest to simulations because when they affect driver behaviour thus influence train runs."""
		self.___callOnAspectTime : int = None	#TODO DEFINED AS duration
		"""time for duration to show call-on aspect on this signal"""
		self.___sightDistance : tLengthM = None
		# @AssociationType Common.tLengthM
		# """The distance in metres the signal is visible in advance by the train driver. This might influence reaction times on changing aspects for simulation."""
		self._refersTo : EntityILref = None
		"""The reference to the physical trackside signal."""
		self._protectsBlockExit : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1

