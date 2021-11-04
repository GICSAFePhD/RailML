#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref
from RailML.Interlocking import EntityIL
from typing import List, NewType

Duration = NewType("Duration", int)

class RouteActivationSection(EntityIL.EntityIL):
	"""The route is locked, i.e. activated, when this sections turns from vacant to occupied. If the delayForLock timer isn't given (or zero) the lock applies immediately."""
	@property
	def DelayForLock(self) -> Duration:
		return self.___delayForLock
	@property
	def AutomaticReleaseDelay(self) -> Duration:
		return self.___automaticReleaseDelay
	@property
	def ActivationSection(self) -> EntityILref:
		return self.___activationSection

	@DelayForLock.setter
	def DelayForLock(self, aDelayForLock : Duration):
		self.___delayForLock = aDelayForLock
	@AutomaticReleaseDelay.setter
	def AutomaticReleaseDelay(self, aAutomaticReleaseDelay : Duration):
		self.___automaticReleaseDelay = aAutomaticReleaseDelay
	@ActivationSection.setter
	def ActivationSection(self, aActivationSection : EntityILref):	# *aActivationSection
		self.___activationSection = aActivationSection

	def create_ActivationSection(self):
		if self.ActivationSection == None:
			self.ActivationSection = []
		self.ActivationSection.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___delayForLock : Duration = None
		"""The delay in seconds between the moment the approach section changes from vacant to occupied and the moment the route the interlocking locks the route."""
		self.___automaticReleaseDelay : Duration = None
		"""Delay in seconds between the moment that the route is locked on the ground that the approach section turned occupied, and the release of the route. This delay for automatic release would typically be used when an approach train stops in an approach section but fails to enter the route."""
		self.___activationSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """This is the reference to the TVD section activating the route when this section turns from vacant to occupied."""