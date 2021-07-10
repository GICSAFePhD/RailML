#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tGenericID
from Common import tUUID
from typing import List

class tID(tGenericID, tUUID):
	"""use UUID if your system supports this functionality, otherwise use GenericID (xs:ID)"""
	pass
