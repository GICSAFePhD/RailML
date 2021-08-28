#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Balise
from typing import List

class Balises(object):
	@property
	def Balise(self) -> Balise:
		return self.___balise
	
	@Balise.setter
	def Balise(self, aBalise : Balise):
		self.___balise = aBalise

	def __init__(self):
		self.___balise : Balise = None
		# @AssociationType Infrastructure.Balise*
		# @AssociationMultiplicity 0..*

