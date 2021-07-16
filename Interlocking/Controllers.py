#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.Controller import Controller
from typing import List

class Controllers(object):
	"""container element for all controller elements"""
	def setController(self, *aController : Controller):
		self._controller = aController

	def getController(self) -> Controller:
		return self._controller

	def __init__(self):
		self._controller : Controller = None
		# @AssociationType Interlocking.Controller*
		# @AssociationMultiplicity 1..*
		# """Container with reference to connected interlockings and system assets controlled by this operational terminal."""

