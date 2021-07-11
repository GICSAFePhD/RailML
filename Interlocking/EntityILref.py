#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute, tElementWithIDref
from typing import List

#class EntityILref(tElementWithIDref): #TODO CON HERENCIA SE ROMPE
class EntityILref():
	"""base type for referring elements in other parts of the schema providing just attribute @ref plus the possibility to add an anyAttribute"""
	def __init__(self):
		self._unnamed_anyAttribute_ : anyAttribute = None

