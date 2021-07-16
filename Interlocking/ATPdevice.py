#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class ATPdevice(TrackAsset):
	"""a minimal stub that merely creates a link between ATP and signals. The ATP state mostly derives from a signal at the entry of the ATP section. In some cases, the state can be a function of the aspect of both entry- and exit-signal. Note the need to include virtual signals where ATP changes the signalled speed. A changed speed is often accompanied by a passive trackside speed sign in order to synchronise wayside speed signalling with cabin speed signalling.
	Not with railML3.1"""
	__metaclass__ = ABCMeta
	@classmethod
	def setAtpType(self, aAtpType : EntityILref):
		self._atpType = aAtpType

	@classmethod
	def getAtpType(self) -> EntityILref:
		return self._atpType

	@classmethod
	def setDevice(self, *aDevice : EntityILref):
		self._device = aDevice

	@classmethod
	def getDevice(self) -> EntityILref:
		return self._device

	@classmethod
	def setExitSignal(self, *aExitSignal : EntityILref):
		self._exitSignal = aExitSignal

	@classmethod
	def getExitSignal(self) -> EntityILref:
		return self._exitSignal

	@classmethod
	def setEntrySignal(self, aEntrySignal : EntityILref):
		self._entrySignal = aEntrySignal

	@classmethod
	def getEntrySignal(self) -> EntityILref:
		return self._entrySignal

	@classmethod
	def __init__(self):
		self._atpType : EntityILref = None
		self._device : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self._exitSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self._entrySignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1

