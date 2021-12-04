#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tGenericID, tUUID
from typing import List

class tID(tGenericID.tGenericID, tUUID.tUUID):
	"""use UUID if your system supports this functionality, otherwise use GenericID (xs:ID)"""
	def __init__(self):
		super().__init__()
