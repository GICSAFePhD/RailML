#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Common import anyAttribute
from Common import tElementWithIDandName
from typing import List

class VisualizationBaseElement(tElementWithIDandName):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_anyAttribute_ : anyAttribute = None

