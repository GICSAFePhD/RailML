#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Common import Designator
from Common import External
from Infrastructure import EntityIS
from typing import List

class FunctionalInfrastructureEntity(EntityIS):
	__metaclass__ = ABCMeta
	@classmethod
	def setDesignator(self, *aDesignator : Designator*):
		self._designator = aDesignator

	@classmethod
	def getDesignator(self) -> Designator*:
		return self._designator

	@classmethod
	def setExternal(self, *aExternal : External*):
		self._external = aExternal

	@classmethod
	def getExternal(self) -> External*:
		return self._external

	@classmethod
	def __init__(self):
		self._designator : Designator = None
		# @AssociationType Common.Designator*
		# @AssociationMultiplicity 0..*
		self._external : External = None
		# @AssociationType Common.External*
		# @AssociationMultiplicity 0..*

