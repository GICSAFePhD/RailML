#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import EntityILref, TrackAsset
from typing import List

class ATPdevice(TrackAsset.TrackAsset):
	"""a minimal stub that merely creates a link between ATP and signals. The ATP state mostly derives from a signal at the entry of the ATP section. In some cases, the state can be a function of the aspect of both entry- and exit-signal. Note the need to include virtual signals where ATP changes the signalled speed. A changed speed is often accompanied by a passive trackside speed sign in order to synchronise wayside speed signalling with cabin speed signalling.
	Not with railML3.1"""
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

	def create_AtpType(self):
		self.AtpType = EntityILref.EntityILref()
	def create_Device(self):
		self.Device = EntityILref.EntityILref()
	def create_ExitSignal(self):
		if self.ExitSignal == None:
			self.ExitSignal = []
		self.ExitSignal.append(EntityILref.EntityILref())
	def create_EntrySignal(self):
		if self.EntrySignal == None:
			self.EntrySignal = []
		self.EntrySignal.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___atpType : EntityILref = None
		self.___device : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self.___exitSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..2
		self.___entrySignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1