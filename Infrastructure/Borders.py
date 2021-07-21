#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Border
from typing import List

class Borders(object):
	@property
	def Border(self) -> Border:
		return self.___border
	
	@Border.setter
	def Border(self, aBorder : Border):
		self.___border = aBorder

	def __init__(self):
		self.___border : Border = Border.Border()
		# @AssociationType Infrastructure.Border*
		# @AssociationMultiplicity 1..*

