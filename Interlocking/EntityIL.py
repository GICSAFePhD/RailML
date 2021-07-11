#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute
from RailML.Interlocking import tElementWithIDandDesignator
from typing import List

#class EntityIL(tElementWithIDandDesignator): #TODO CON HERENCIA SE ROMPE
class EntityIL():
	"""base type for normal elements in IL providing attributes @id and @name plus the possibility to add an anyAttribute"""
	def __init__(self):
		self._unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_anyAttribute_ : anyAttribute = None

