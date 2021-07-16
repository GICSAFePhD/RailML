#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class LogicalDevice(TrackAsset):
	"""The logical device applies any number of Boolean equations. It represents e.g. a complex relay circuit or PLC that converts high/low electric input signals from any source into Boolean true/false outputs. It can exchange binary i/o with the interlocking. The description attribute can contain textual description of the field elements and Boolean relations that produce the Boolean output. Use this for ancillary equipment connected to the interlocking, e.g. bascule bridges, tunnel equipment, detectors such as earthquake and flooding detectors. Finally it provides a state which is considered in interlocking operation."""
	__metaclass__ = ABCMeta
	@classmethod
	def setDescription(self, aDescription : str):
		self.___description = aDescription

	@classmethod
	def getDescription(self) -> str:
		return self.___description

	@classmethod
	def setTakesControlOf(self, aTakesControlOf : EntityILref):
		self._takesControlOf = aTakesControlOf

	@classmethod
	def getTakesControlOf(self) -> EntityILref:
		return self._takesControlOf

	@classmethod
	def setHasInterface(self, aHasInterface : EntityILref):
		self._hasInterface = aHasInterface

	@classmethod
	def getHasInterface(self) -> EntityILref:
		return self._hasInterface

	@classmethod
	def setRefersTo(self, *aRefersTo : EntityILref):
		self._refersTo = aRefersTo

	@classmethod
	def getRefersTo(self) -> EntityILref:
		return self._refersTo

	@classmethod
	def __init__(self):
		self.___description : str = None
		"""Description of the logic."""
		self._takesControlOf : EntityILref = None
		"""The reference to one or more track assets which are controlled by this logical object."""
		self._hasInterface : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the physical I/O-interface from interlocking to the locking device to control it."""
		self._refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the physical device in the infrastructure."""

