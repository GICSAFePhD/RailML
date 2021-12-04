#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tUUID, tGenericRef
from typing import List

class tRef(tUUID.tUUID, tGenericRef.tGenericRef):     
	"""reference an object using its UUID or GenericID (xs:ID)"""
	def __init__(self):
		super().__init__()
		#pass
