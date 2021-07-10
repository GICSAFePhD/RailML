#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import SpeedSection
from typing import List

class Speeds(object):
	def setSpeedSection(self, *aSpeedSection : SpeedSection*):
		self._speedSection = aSpeedSection

	def getSpeedSection(self) -> SpeedSection*:
		return self._speedSection

	def __init__(self):
		self._speedSection : SpeedSection = None
		# @AssociationType Infrastructure.SpeedSection*
		# @AssociationMultiplicity 1..*

