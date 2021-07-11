#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import anyAttribute, tElementWithIDandName
from typing import List

#class VisualizationBaseElement(tElementWithIDandName): #TODO CON ESTA HERENCIA SE ROMPE
class VisualizationBaseElement():
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_anyAttribute_ : anyAttribute = None

