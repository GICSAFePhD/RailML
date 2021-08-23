#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_AssociatedPositioningSystem, RTM_CompositionNetElement
from typing import List

class RTM_PositioningNetElement(RTM_CompositionNetElement.RTM_CompositionNetElement):
	def __init__(self):
		self._associatedPositioningSystem : RTM_AssociatedPositioningSystem = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedPositioningSystem*
		# @AssociationMultiplicity 1..*

