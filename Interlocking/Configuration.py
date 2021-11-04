#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tIxlTechnologyTypeListExt, EntityIL
from typing import List

class Configuration(EntityIL.EntityIL):
	"""general attributes of interlocking configuration"""
	@property
	def Model(self) -> str:
		return self.___model
	@property
	def TechnologyType(self) -> tIxlTechnologyTypeListExt:
		return self.___technologyType
	@property
	def SWversion(self) -> str:
		return self.___sWversion
	@property
	def SignalSystem(self) -> str:
		return self.___signalSystem

	@Model.setter
	def Model(self, aModel : str):
		self.___model = aModel
	@TechnologyType.setter
	def TechnologyType(self, aTechnologyType : tIxlTechnologyTypeListExt):
		self.___technologyType = aTechnologyType
	@SWversion.setter
	def SWversion(self, aSWversion : str):
		self.___sWversion = aSWversion
	@SignalSystem.setter
	def SignalSystem(self, aSignalSystem : str):
		self.___signalSystem = aSignalSystem

	def __init__(self):
		super().__init__()
		self.___model : str = None
		"""The vendor specific model of the interlocking."""
		self.___technologyType : tIxlTechnologyTypeListExt = None
		# @AssociationType Interlocking.tIxlTechnologyTypeListExt
		# """The basic technology type of the interlocking"""
		self.___sWversion : str = None
		"""The software version used by this interlocking."""
		self.___signalSystem : str = None
		"""The name of the signal system used with this interlocking, e.g. Hl or Ks system of Deutsche Bahn."""