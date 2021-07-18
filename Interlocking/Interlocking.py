#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.AssetsForIL import AssetsForIL
from RailML.Interlocking.Controllers import Controllers
from RailML.Interlocking.SignalBoxes import SignalBoxes
from RailML.Interlocking.GenericIMs import GenericIMs
from typing import List

class Interlocking(object):
	"""This is the top level element for the interlocking model. It is the home of several elements (classes) containing the particular aspects of the information."""
	def setAssetsForIL(self, aAssetsForIL : AssetsForIL):
		self._assetsForIL = aAssetsForIL

	def getAssetsForIL(self) -> AssetsForIL:
		return self._assetsForIL

	def setControllers(self, aControllers : Controllers):
		self._controllers = aControllers

	def getControllers(self) -> Controllers:
		return self._controllers

	def setSignalBoxes(self, aSignalBoxes : SignalBoxes):
		self._signalBoxes = aSignalBoxes

	def getSignalBoxes(self) -> SignalBoxes:
		return self._signalBoxes

	def setSpecificIMs(self, aSpecificIMs : GenericIMs):
		self._specificIMs = aSpecificIMs

	def getSpecificIMs(self) -> GenericIMs:
		return self._specificIMs

	def __init__(self):
		self._assetsForIL : AssetsForIL = None
		# @AssociationType Interlocking.AssetsForIL
		# @AssociationMultiplicity 0..1
		# """container for all asset elements needed for interlocking purpose"""
		self._controllers : Controllers = None
		# @AssociationType Interlocking.Controllers
		# @AssociationMultiplicity 0..1
		# """container for all Controller elements"""
		self._signalBoxes : SignalBoxes = None
		# @AssociationType Interlocking.SignalBoxes
		# @AssociationMultiplicity 0..1
		# """container for all SignalBox elements"""
		self._specificIMs : GenericIMs = None
		# @AssociationType Interlocking.GenericIMs
		# @AssociationMultiplicity 0..1
		# """container for all SpecificIM elements"""

