#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import Balise
from typing import List

class Balises(object):
	def setBalise(self, *aBalise : Balise*):
		self._balise = aBalise

	def getBalise(self) -> Balise*:
		return self._balise

	def __init__(self):
		self._balise : Balise = None
		# @AssociationType Infrastructure.Balise*
		# @AssociationMultiplicity 0..*

