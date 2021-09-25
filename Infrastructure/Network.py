#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_Network
from typing import List

class Network(RTM_Network.RTM_Network):
	"""The Network type is derived from the RailTopoModel class Network."""

	def __init__(self):	
		super().__init__()
		#self.___level : RTM_LevelNetwork = None
		# @AssociationType Infrastructure.RTM.RTM_LevelNetwork*
		# @AssociationMultiplicity 1..*