#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.Name import Name
from abc import ABCMeta, abstractmethod
from RailML.RailTopoModel import RTM_LevelNetwork, RTM_NetworkResource, RTM_NamedResource
from typing import List

class RTM_Network(RTM_NamedResource.RTM_NamedResource):
	@property
	def Id(self) -> str:
		return self.___id
	@property
	def Level(self) -> RTM_LevelNetwork:
		return self.___level
	@property
	def NetworkResource(self) -> RTM_NetworkResource:
		return self.___networkResource

	@Id.setter
	def Id(self, aId : str):
		self.___id = aId
	@Level.setter
	def Level(self, aLevel : RTM_LevelNetwork):
		self.___level = aLevel
	@NetworkResource.setter
	def NetworkResource(self, aNetworkResource : RTM_NetworkResource):
		self.___networkResource = aNetworkResource
	
	def create_Level(self):
		if self.Level == None:
			self.Level = []
		self.Level.append(RTM_LevelNetwork.RTM_LevelNetwork())
	def create_NetworkResource(self):
		if self.NetworkResource == None:
			self.NetworkResource = []
		self.NetworkResource.append(RTM_NetworkResource.RTM_NetworkResource())

	def __init__(self):
		super().__init__()
		#self.___id : str = ""
		self.___level : RTM_LevelNetwork = None
		# @AssociationType Infrastructure.RTM.RTM_LevelNetwork*
		# @AssociationMultiplicity 1..*
		self.___networkResource : RTM_NetworkResource = None
		# @AssociationType Infrastructure.RTM.RTM_NetworkResource*
		# @AssociationMultiplicity 0..*