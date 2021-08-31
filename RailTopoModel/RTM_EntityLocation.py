#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_EntityLocation(RTM_BaseObject.RTM_BaseObject):
	def __init__(self):
		super().__init__()
