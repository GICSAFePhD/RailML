#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Platform
from typing import List

class Platforms(object):
	@property
	def Platform(self) -> Platform:
		return self.___platform
	
	@Platform.setter
	def Platform(self, aPlatform : Platform):
		self.___platform = aPlatform

	def __init__(self):
		self.___platform : Platform = Platform.Platform()
		# @AssociationType Infrastructure.Platform*
		# @AssociationMultiplicity 1..*

