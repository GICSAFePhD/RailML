#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tLengthM import tLengthM
from RailML.Common.tSpeedKmPerHour import tSpeedKmPerHour
from typing import List

class PantographSpacing(object):
	def setNumberPantographsRaised(self, aNumberPantographsRaised : int): #TODO DEFINED AS INTEGER
		self.___numberPantographsRaised = aNumberPantographsRaised

	def getNumberPantographsRaised(self) -> int:	#TODO DEFINED AS INTEGER
		return self.___numberPantographsRaised

	def setSpacingPantographsRaised(self, aSpacingPantographsRaised : tLengthM):
		self.___spacingPantographsRaised = aSpacingPantographsRaised

	def getSpacingPantographsRaised(self) -> tLengthM:
		return self.___spacingPantographsRaised

	def setSpeed4PantographSpacing(self, aSpeed4PantographSpacing : tSpeedKmPerHour):
		self.___speed4PantographSpacing = aSpeed4PantographSpacing

	def getSpeed4PantographSpacing(self) -> tSpeedKmPerHour:
		return self.___speed4PantographSpacing

	def __init__(self):
		self.___numberPantographsRaised : int = None	#TODO DEFINED AS INTEGER
		"""number of pantographs raised simultaneously on moving train"""
		self.___spacingPantographsRaised : tLengthM = None
		# @AssociationType Common.tLengthM
		# """minimum spacing between raised pantographs of a train, in [m]"""
		self.___speed4PantographSpacing : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """related maximum speed for the given pantograph spacing limit, in [km/h]"""

