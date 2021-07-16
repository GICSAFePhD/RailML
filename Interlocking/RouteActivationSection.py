#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class RouteActivationSection(EntityIL):
	"""The route is locked, i.e. activated, when this sections turns from vacant to occupied. If the delayForLock timer isn't given (or zero) the lock applies immediately."""
	def setDelayForLock(self, aDelayForLock : int):	#TODO DEFINED AS duration
		self.___delayForLock = aDelayForLock

	def getDelayForLock(self) -> int:	#TODO DEFINED AS duration
		return self.___delayForLock

	def setAutomaticReleaseDelay(self, aAutomaticReleaseDelay : int):	#TODO DEFINED AS duration
		self.___automaticReleaseDelay = aAutomaticReleaseDelay

	def getAutomaticReleaseDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___automaticReleaseDelay

	def setActivationSection(self, *aActivationSection : EntityILref):
		self._activationSection = aActivationSection

	def getActivationSection(self) -> EntityILref:
		return self._activationSection

	def __init__(self):
		self.___delayForLock : int = None	#TODO DEFINED AS duration
		"""The delay in seconds between the moment the approach section changes from vacant to occupied and the moment the route the interlocking locks the route."""
		self.___automaticReleaseDelay : int = None	#TODO DEFINED AS duration
		"""Delay in seconds between the moment that the route is locked on the ground that the approach section turned occupied, and the release of the route. This delay for automatic release would typically be used when an approach train stops in an approach section but fails to enter the route."""
		self._activationSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """This is the reference to the TVD section activating the route when this section turns from vacant to occupied."""

