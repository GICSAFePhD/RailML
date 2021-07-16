#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class RouteEntry(EntityIL):
	"""The route entry is normally a (virtual) signal."""
	def setRefersTo(self, *aRefersTo : EntityILref):
		self._refersTo = aRefersTo

	def getRefersTo(self) -> EntityILref:
		return self._refersTo

	def setNonReplacement(self, aNonReplacement : EntityILref):
		self._nonReplacement = aNonReplacement

	def getNonReplacement(self) -> EntityILref:
		return self._nonReplacement

	def __init__(self):
		self._refersTo : EntityILref = None
		"""The reference to the track asset representing the start point of the route. In most cases this is a signal."""
		self._nonReplacement : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to any TVD section in advance to the start signal which sequential occupation will not cause the signal closure."""

