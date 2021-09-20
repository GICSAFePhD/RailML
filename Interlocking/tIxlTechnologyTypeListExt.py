#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tIxlTechnologyTypeList
from typing import List

class tIxlTechnologyTypeListExt(tIxlTechnologyTypeList.tIxlTechnologyTypeList):
	"""The list of possible interlocking technologies with extension point."""
	def __init__(self):
		super().__init__()