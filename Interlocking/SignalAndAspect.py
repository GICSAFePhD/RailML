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
	def RefersToSignal(self, aRefersToSignal : EntityILref):	# TODO *aRefersToSignal
		self.___refersToSignal = aRefersToSignal
	@ShowsAspect.setter
	def ShowsAspect(self, aShowsAspect : EntityILref):
		self.___showsAspect = aShowsAspect

	def create_RefersToSignal(self):
		self.RefersToSignal  = EntityILref.EntityILref()
	def create_ShowsAspect(self):
		if self.ShowsAspect == None:
			self.ShowsAspect = []
		self.ShowsAspect.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___refersToSignal : EntityILref = None
		"""The reference to the signal."""
		self.___showsAspect : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The aspect the signal is showing."""