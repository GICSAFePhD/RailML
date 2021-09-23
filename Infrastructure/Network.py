#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_Network,RTM_LevelNetwork
from typing import List

class Network(RTM_Network.RTM_Network):
	"""The Network type is derived from the RailTopoModel class Network."""
	@property
	def Level(self) -> RTM_LevelNetwork:
		return self.___level	

	@Level.setter
	def Level(self, aLevel : RTM_LevelNetwork):
		self.___level = aLevel

	def create_Level(self):
		if self.Level == None:
			self.Level = []
		self.Level.append(RTM_LevelNetwork.RTM_LevelNetwork())

	def __init__(self):	
		super().__init__()
		self.___level : RTM_LevelNetwork = None
		# @AssociationType Infrastructure.RTM.RTM_LevelNetwork*
		# @AssociationMultiplicity 1..*