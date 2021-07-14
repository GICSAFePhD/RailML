#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.aTrackbed import aTrackbed
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class TrackBed(FunctionalInfrastructureEntity):
	def __init__(self):
		self._unnamed_aTrackbed_ : aTrackbed = None

