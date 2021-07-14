#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Infrastructure.CrossedElement import CrossedElement
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class XCrossing(FunctionalInfrastructureEntity):
	__metaclass__ = ABCMeta
	@classmethod
	def setCrossesElement(self, *aCrossesElement : CrossedElement):
		self._crossesElement = aCrossesElement

	@classmethod
	def getCrossesElement(self) -> CrossedElement:
		return self._crossesElement

	@classmethod
	def __init__(self):
		self._crossesElement : CrossedElement = None
		# @AssociationType Infrastructure.CrossedElement*
		# @AssociationMultiplicity 0..*

