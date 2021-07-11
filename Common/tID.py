#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tGenericID, tUUID
from typing import List

#class tID(tGenericID, tUUID): #TODO CON ESTA HERENCIA SE ROMPE!
class tID():
	"""use UUID if your system supports this functionality, otherwise use GenericID (xs:ID)"""
	pass
