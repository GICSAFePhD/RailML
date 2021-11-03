#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import EntityILref
from RailML.Interlocking import EntityIL
from typing import List, NewType

Duration = NewType("Duration", int)

class PartialRoute(EntityIL.EntityIL):
	"""A partial route is a subset of TVD sections within the route. This subset can be used, e.g. for release if the conditions prescribed by the IM rules are fulfilled."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	@property
	def TypicalDelay(self) -> Duration:
		return self.___typicalDelay
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection

	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay
	@TypicalDelay.setter
	def TypicalDelay(self, aTypicalDelay : Duration):
		self.___typicalDelay = aTypicalDelay
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):	# *HasTvdSection
		self.___hasTvdSection = aHasTvdSection

	def __init__(self):
		super().__init__()
		self.___delay : Duration = None
		"""Duration after which the IL releases the partial route. Starts counting from the moment that all the conditions for release are fulfilled. This delay is engineered in static data. If not defined, the IL releases the group without delay.
		If the route has only one route release group then the set of TVD sections in the route is released en bloc with the delay given here."""
		self.___typicalDelay : Duration = None
		"""Duration after which the partial route is typically released. Use this delay for simulation purposes. Starts counting from the moment that the interlocking has received all conditions for the release. E.g. TVD sections in the group have been vacated, timers expired."""
		self.___hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Referral to the TVD sections in this part of the route."""