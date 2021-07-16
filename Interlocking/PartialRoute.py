#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class PartialRoute(EntityIL):
	"""A partial route is a subset of TVD sections within the route. This subset can be used, e.g. for release if the conditions prescribed by the IM rules are fulfilled."""
	__metaclass__ = ABCMeta
	@classmethod
	def setDelay(self, aDelay : int):	#TODO DEFINED AS duration
		self.___delay = aDelay

	@classmethod
	def getDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___delay

	@classmethod
	def setTypicalDelay(self, aTypicalDelay : int):	#TODO DEFINED AS duration
		self.___typicalDelay = aTypicalDelay

	@classmethod
	def getTypicalDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___typicalDelay

	@classmethod
	def setHasTvdSection(self, *aHasTvdSection : EntityILref):
		self._hasTvdSection = aHasTvdSection

	@classmethod
	def getHasTvdSection(self) -> EntityILref:
		return self._hasTvdSection

	@classmethod
	def __init__(self):
		self.___delay : int = None	#TODO DEFINED AS duration
		"""Duration after which the IL releases the partial route. Starts counting from the moment that all the conditions for release are fulfilled. This delay is engineered in static data. If not defined, the IL releases the group without delay.
		If the route has only one route release group then the set of TVD sections in the route is released en bloc with the delay given here."""
		self.___typicalDelay : int = None	#TODO DEFINED AS duration
		"""Duration after which the partial route is typically released. Use this delay for simulation purposes. Starts counting from the moment that the interlocking has received all conditions for the release. E.g. TVD sections in the group have been vacated, timers expired."""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Referral to the TVD sections in this part of the route."""

