#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Platform import Platform
from typing import List

class Platforms(object):
	def setPlatform(self, *aPlatform : Platform):
		self._platform = aPlatform

	def getPlatform(self) -> Platform:
		return self._platform

	def __init__(self):
		self._platform : Platform = None
		# @AssociationType Infrastructure.Platform*
		# @AssociationMultiplicity 1..*

