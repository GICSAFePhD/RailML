#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import anyAttribute, tElementWithIDandName
from typing import List

class VisualizationBaseElement(tElementWithIDandName.tElementWithIDandName):

	def __init__(self):
		super().__init__()
		self._unnamed_any_ = None
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_anyAttribute_ : anyAttribute = None