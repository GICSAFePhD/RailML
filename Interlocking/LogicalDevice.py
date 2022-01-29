#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import EntityILref
from RailML.Interlocking import TrackAsset
from typing import List

class LogicalDevice(TrackAsset.TrackAsset):
	"""The logical device applies any number of Boolean equations. It represents e.g. a complex relay circuit or PLC that converts high/low electric input signals from any source into Boolean true/false outputs. It can exchange binary i/o with the interlocking. The description attribute can contain textual description of the field elements and Boolean relations that produce the Boolean output. Use this for ancillary equipment connected to the interlocking, e.g. bascule bridges, tunnel equipment, detectors such as earthquake and flooding detectors. Finally it provides a state which is considered in interlocking operation."""
	@property
	def Description(self) -> str:
		return self.___description
	@property
	def TakesControlOf(self) -> EntityILref:
		return self.___takesControlOf
	@property
	def HasInterface(self) -> EntityILref:
		return self.___hasInterface
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo

	@Description.setter
	def Description(self, aDescription : str):
		self.___description = aDescription
	@TakesControlOf.setter
	def TakesControlOf(self, aTakesControlOf : EntityILref):
		self.___takesControlOf = aTakesControlOf
	@HasInterface.setter
	def HasInterface(self, aHasInterface : EntityILref):
		self.___hasInterface = aHasInterface
	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref):
		self.___refersTo = aRefersTo	

	def __init__(self):
		super().__init__()
		self.___description : str = None
		"""Description of the logic."""
		self.___takesControlOf : EntityILref = None
		"""The reference to one or more track assets which are controlled by this logical object."""
		self.___hasInterface : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the physical I/O-interface from interlocking to the locking device to control it."""
		self.___refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the physical device in the infrastructure."""

