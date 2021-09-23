#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from typing import List

class PositioningSystemCoordinate(object):  
	@property
	def PositioningSystemRef(self) -> tRef:
		return self.___positioningSystemRef

	@PositioningSystemRef.setter
	def PositioningSystemRef(self, aPositioningSystemRef : tRef):
		self.___positioningSystemRef = aPositioningSystemRef

	def create_PositioningSystemRef(self):
		self.PositioningSystemRef = tRef.tRef()
    
	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef