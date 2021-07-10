#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import ControlledAssets
from Interlocking import Itineraries
from Interlocking import EntityIL
from typing import List

class Controller(EntityIL):
	"""A controller is an individual terminal, commonly a workstation, that can control the interlocking. The controller is normally situated in a control centre. railML provides a logical link between an interlocking and the individual controller. The user can attach useful data to this link, such as addresses that may be granted control over this IL. railML will not define the nature of the addresses, i.e IP-addresses or hexadecimal address of terminals that communicate with the IL via some serial bus. The protocol (IP, UDP, serial, parallel) is irrelevant to railML. Note that a Control Centre (DE: Leitstelle, FR: Poste de controle, NL: VL-post) is likely to control multiple interlockings and vice versa, one interlocking can be controlled from multiple control centres, an n:m relation. This implies that a control centre can have multiple controllers, defined as a terminal from which a signal man controls an interlocking. The IL is unaware of the Control Centre but aware of the controller."""
	def setControlledAssets(self, aControlledAssets : ControlledAssets):
		self._controlledAssets = aControlledAssets

	def getControlledAssets(self) -> ControlledAssets:
		return self._controlledAssets

	def setItineraries(self, aItineraries : Itineraries):
		self._itineraries = aItineraries

	def getItineraries(self) -> Itineraries:
		return self._itineraries

	def __init__(self):
		self._controlledAssets : ControlledAssets = None
		# @AssociationType Interlocking.ControlledAssets
		# @AssociationMultiplicity 1
		# """The container of references to all signalBox (interlocking) and system assets controlled from this unit."""
		self._itineraries : Itineraries = None
		# @AssociationType Interlocking.Itineraries
		# @AssociationMultiplicity 0..1
		# """The container of all itineraries as a combination of single routes defining the path from A to B independent of involved signalBoxes (interlockings)."""

