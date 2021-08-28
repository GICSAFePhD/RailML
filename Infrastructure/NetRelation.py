#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tNavigability, tUsage
from RailML.RailTopoModel import RTM_NetworkResource
from typing import List

class NetRelation(RTM_NetworkResource.RTM_NetworkResource):
	"""The NetRelation type is derived from the RailTopoModel class PositionedRelation."""    
	def __init__(self):
		pass