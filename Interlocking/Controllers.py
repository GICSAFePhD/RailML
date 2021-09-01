#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Controller
from typing import List

class Controllers(object):
	"""container element for all controller elements"""
	@property
	def Controller(self) -> Controller:
		return self.___controller
	
	@Controller.setter
	def Controller(self, *aController : Controller):
		self.___controller = aController

	def __init__(self):
		self.___controller : Controller = None
		# @AssociationType Interlocking.Controller*
		# @AssociationMultiplicity 1..*
		# """Container with reference to connected interlockings and system assets controlled by this operational terminal."""

