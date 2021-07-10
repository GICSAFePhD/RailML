#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tIxlTechnologyTypeListExt
from Interlocking import EntityIL
from typing import List

class Configuration(EntityIL):
	"""general attributes of interlocking configuration"""
	def setModel(self, aModel : str):
		self.___model = aModel

	def getModel(self) -> str:
		return self.___model

	def setTechnologyType(self, aTechnologyType : tIxlTechnologyTypeListExt):
		self.___technologyType = aTechnologyType

	def getTechnologyType(self) -> tIxlTechnologyTypeListExt:
		return self.___technologyType

	def setSWversion(self, aSWversion : str):
		self.___sWversion = aSWversion

	def getSWversion(self) -> str:
		return self.___sWversion

	def setSignalSystem(self, aSignalSystem : str):
		self.___signalSystem = aSignalSystem

	def getSignalSystem(self) -> str:
		return self.___signalSystem

	def __init__(self):
		self.___model : str = None
		"""The vendor specific model of the interlocking."""
		self.___technologyType : tIxlTechnologyTypeListExt = None
		# @AssociationType Interlocking.tIxlTechnologyTypeListExt
		# """The basic technology type of the interlocking"""
		self.___sWversion : str = None
		"""The software version used by this interlocking."""
		self.___signalSystem : str = None
		"""The name of the signal system used with this interlocking, e.g. Hl or Ks system of Deutsche Bahn."""

