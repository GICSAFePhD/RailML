#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import AssetsForIL, Controllers, SignalBoxes, GenericIMs
from typing import List

class Interlocking(object):
	"""This is the top level element for the interlocking model. It is the home of several elements (classes) containing the particular aspects of the information."""
	@property
	def AssetsForIL(self) -> AssetsForIL:
		return self.___assetsForIL
	@property
	def Controllers(self) -> Controllers:
		return self.___controllers
	@property
	def SignalBoxes(self) -> SignalBoxes:
		return self.___signalBoxes
	@property
	def GenericIMs(self) -> GenericIMs:
		return self.___specificIMs

	@AssetsForIL.setter
	def AssetsForIL(self, aAssetsForIL : AssetsForIL):
		self.___assetsForIL = aAssetsForIL
	@Controllers.setter
	def Controllers(self, aControllers : Controllers):
		self.___controllers = aControllers
	@SignalBoxes.setter
	def SignalBoxes(self, aSignalBoxes : SignalBoxes):
		self.___signalBoxes = aSignalBoxes
	@GenericIMs.setter
	def GenericIMs(self, aGenericIMs : GenericIMs):
		self.___specificIMs = aGenericIMs

	def create_AssetsForIL(self):
		if self.AssetsForIL == None:
			self.AssetsForIL = []
		self.AssetsForIL.append(AssetsForIL.AssetsForIL())
	def create_Controllers(self):
		if self.Controllers == None:
			self.Controllers = []
		self.Controllers.append(Controllers.Controllers())
	def create_SignalBoxes(self):
		if self.SignalBoxes == None:
			self.SignalBoxes = []
		self.SignalBoxes.append(SignalBoxes.SignalBoxes())
	def create_GenericIMs(self):
		if self.GenericIMs == None:
			self.GenericIMs = []
		self.GenericIMs.append(GenericIMs.GenericIMs())

	def __init__(self):
		self.___assetsForIL : AssetsForIL = None	# TODO DONE
		# @AssociationType Interlocking.AssetsForIL
		# @AssociationMultiplicity 0..1
		# """container for all asset elements needed for interlocking purpose"""
		self.___controllers : Controllers = None	# TODO DONE
		# @AssociationType Interlocking.Controllers
		# @AssociationMultiplicity 0..1
		# """container for all Controller elements"""
		self.___signalBoxes : SignalBoxes = None
		# @AssociationType Interlocking.SignalBoxes
		# @AssociationMultiplicity 0..1
		# """container for all SignalBox elements"""
		self.___specificIMs : GenericIMs = None
		# @AssociationType Interlocking.GenericIMs
		# @AssociationMultiplicity 0..1
		# """container for all SpecificIM elements"""