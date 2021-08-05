#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, AssetAndState
from typing import List

class SignalAndAspect(AssetAndState.AssetAndState):
	"""A tuple (signal, aspect). Refers to a signal and an aspect. Used for expressing concepts like signal 1105 shows yellow flashing."""
	@property
	def RefersToSignal(self) -> EntityILref:
		return self.___refersToSignal
	@property
	def ShowsAspect(self) -> EntityILref:
		return self.___showsAspect

	@RefersToSignal.setter
	def RefersToSignal(self, *aRefersToSignal : EntityILref):
		self.___refersToSignal = aRefersToSignal
	@ShowsAspect.setter
	def ShowsAspect(self, aShowsAspect : EntityILref):
		self.___showsAspect = aShowsAspect

	def __init__(self):
		self.___refersToSignal : EntityILref = EntityILref.EntityILref()
		"""The reference to the signal."""
		self.___showsAspect : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The aspect the signal is showing."""

