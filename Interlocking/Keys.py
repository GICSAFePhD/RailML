#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Key
from typing import List

class Keys(object):
	"""container element for all Key elements"""
	@property
	def Key(self) -> Key:
		return self.___key
	
	@Key.setter
	def Key(self, aKey : Key):
		self.___key = aKey

	def create_Key(self):
		if self.Key == None:
			self.Key = []
		self.Key.append(Key.Key())

	def __init__(self):
		self.___key : Key = None
		# @AssociationType Interlocking.Key*
		# @AssociationMultiplicity 1..*
		# """An ancillary element used for operation of a specific locking device."""