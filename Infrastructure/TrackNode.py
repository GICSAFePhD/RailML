#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class TrackNode(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	
	def __init__(self):
		super().__init__()
		