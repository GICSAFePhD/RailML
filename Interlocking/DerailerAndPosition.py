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

	def create_InPosition(self):
		if self.InPosition == None:
			self.InPosition = []
		self.InPosition.append(tDerailingPosition.tDerailingPosition())

	def create_RefersToDerailer(self):
		if self.RefersToDerailer == None:
			self.RefersToDerailer = []
		self.RefersToDerailer.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___inPosition : tDerailingPosition = None
		# @AssociationType Interlocking.tDerailingPosition
		# """The position the derailer is in."""
		self.___refersToDerailer : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the derailer."""

