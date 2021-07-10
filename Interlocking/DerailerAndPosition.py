#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tDerailingPosition
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class DerailerAndPosition(AssetAndState):
	"""A tuple (derailer, position). Refers to a derailer and a position. Used for expressing concepts like: the derailer has to be in the non-derailing/passable position."""
	def setInPosition(self, aInPosition : tDerailingPosition):
		self.___inPosition = aInPosition

	def getInPosition(self) -> tDerailingPosition:
		return self.___inPosition

	def setRefersToDerailer(self, aRefersToDerailer : EntityILref):
		self._refersToDerailer = aRefersToDerailer

	def getRefersToDerailer(self) -> EntityILref:
		return self._refersToDerailer

	def __init__(self):
		self.___inPosition : tDerailingPosition = None
		# @AssociationType Interlocking.tDerailingPosition
		# """The position the derailer is in."""
		self._refersToDerailer : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the derailer."""

