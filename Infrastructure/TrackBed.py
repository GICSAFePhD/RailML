#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import aTrackbed, FunctionalInfrastructureEntity
from typing import List

class TrackBed(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def aTrackbed(self) -> aTrackbed:
		return self.___unnamed_aTrackbed
	
	@aTrackbed.setter
	def aTrackbed(self, aaTrackbed : aTrackbed):
		self.___unnamed_aTrackbed = aaTrackbed
    
    
	def __init__(self):
		self.___unnamed_aTrackbed : aTrackbed = None

