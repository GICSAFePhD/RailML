#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import EntityILref, TrackAsset
from typing import List

class ATPdevice(TrackAsset.TrackAsset):
	"""a minimal stub that merely creates a link between ATP and signals. The ATP state mostly derives from a signal at the entry of the ATP section. In some cases, the state can be a function of the aspect of both entry- and exit-signal. Note the need to include virtual signals where ATP changes the signalled speed. A changed speed is often accompanied by a passive trackside speed sign in order to synchronise wayside speed signalling with cabin speed signalling.
	Not with railML3.1"""
	#__metaclass__ = ABCMeta
	@property
	def AtpType(self) -> EntityILref:
		return self.___atpType
	@property
	def Device(self) -> EntityILref:
		return self.___device
	@property
	def ExitSignal(self) -> EntityILref:
		return self.___exitSignal
	@property
	def EntrySignal(self) -> EntityILref:
		return self.___entrySignal

	@AtpType.setter
	def AtpType(self, aAtpType : EntityILref):
		self.___atpType = aAtpType
	@Device.setter
	def Device(self, *aDevice : EntityILref):
		self.___device = aDevice
	@ExitSignal.setter
	def ExitSignal(self, *aExitSignal : EntityILref):
		self.___exitSignal = aExitSignal
	@EntrySignal.setter
	def EntrySignal(self, aEntrySignal : EntityILref):
		self.___entrySignal = aEntrySignal

	def __init__(self):
		self.___atpType : EntityILref = EntityILref.EntityILref()
		self.___device : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self.___exitSignal : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self.___entrySignal : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1

