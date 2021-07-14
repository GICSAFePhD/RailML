#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.MaxTrainCurrent import MaxTrainCurrent
from typing import List

class EnergyCatenary(object):
	def setAllowsRegenerativeBraking(self, aAllowsRegenerativeBraking : int): #TODO DEFINED AS LONG
		self.___allowsRegenerativeBraking = aAllowsRegenerativeBraking

	def getAllowsRegenerativeBraking(self) -> int: #TODO DEFINED AS LONG
		return self.___allowsRegenerativeBraking

	def setMaxTrainCurrent(self, *aMaxTrainCurrent : MaxTrainCurrent):
		self._maxTrainCurrent = aMaxTrainCurrent

	def getMaxTrainCurrent(self) -> MaxTrainCurrent:
		return self._maxTrainCurrent

	def __init__(self):
		self.___allowsRegenerativeBraking : int = None #TODO DEFINED AS LONG
		"""flag, whether the use of regenerative braking is allowed"""
		self._maxTrainCurrent : MaxTrainCurrent = None
		# @AssociationType Infrastructure.MaxTrainCurrent*
		# @AssociationMultiplicity 0..*
		# """maximum current that can be accessed in the described electrification section"""

