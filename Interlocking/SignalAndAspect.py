#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class SignalAndAspect(AssetAndState):
	"""A tuple (signal, aspect). Refers to a signal and an aspect. Used for expressing concepts like signal 1105 shows yellow flashing."""
	def setRefersToSignal(self, *aRefersToSignal : EntityILref*):
		self._refersToSignal = aRefersToSignal

	def getRefersToSignal(self) -> EntityILref*:
		return self._refersToSignal

	def setShowsAspect(self, aShowsAspect : EntityILref):
		self._showsAspect = aShowsAspect

	def getShowsAspect(self) -> EntityILref:
		return self._showsAspect

	def __init__(self):
		self._refersToSignal : EntityILref = None
		"""The reference to the signal."""
		self._showsAspect : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The aspect the signal is showing."""

