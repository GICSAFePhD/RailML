#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import SpeedSection
from typing import List

class Speeds(object):
	@property
	def SpeedSection(self) -> SpeedSection:
		return self.___speedSection
	
	@SpeedSection.setter
	def SpeedSection(self, *aSpeedSection : SpeedSection):
		self.___speedSection = aSpeedSection

	def __init__(self):
		self.___speedSection : SpeedSection = SpeedSection.SpeedSection()
		# @AssociationType Infrastructure.SpeedSection*
		# @AssociationMultiplicity 1..*

