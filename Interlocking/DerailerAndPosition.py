#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tDerailingPosition, EntityILref, AssetAndState
from typing import List

class DerailerAndPosition(AssetAndState.AssetAndState):
	"""A tuple (derailer, position). Refers to a derailer and a position. Used for expressing concepts like: the derailer has to be in the non-derailing/passable position."""
	@property
	def InPosition(self) -> tDerailingPosition:
		return self.___inPosition
	@property
	def RefersToDerailer(self) -> EntityILref:
		return self.___refersToDerailer

	@InPosition.setter
	def InPosition(self, aInPosition : tDerailingPosition):
		self.___inPosition = aInPosition
	@RefersToDerailer.setter
	def RefersToDerailer(self, aRefersToDerailer : EntityILref):
		self.___refersToDerailer = aRefersToDerailer

	def __init__(self):
		self.___inPosition : tDerailingPosition = tDerailingPosition.tDerailingPosition()
		# @AssociationType Interlocking.tDerailingPosition
		# """The position the derailer is in."""
		self.___refersToDerailer : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the derailer."""

