#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.elementsGroup import elementsGroup
from typing import List

class elementContainer(object):
	"""This complexType is included as a convenience for schema authors who need to define a root
	    		or container element for all of the DC elements."""
	def __init__(self):
		self.___elementsGroup : elementsGroup = None
		"""# @AssociationKind Aggregation"""

