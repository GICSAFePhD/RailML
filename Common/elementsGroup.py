#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import any
from typing import List

class elementsGroup(object):
	"""This group is included as a convenience for schema authors
	            who need to refer to all the elements in the 
	            http://purl.org/dc/elements/1.1/ namespace."""
            
	def __init__(self):
		self._any : any = None
		# @AssociationType Common.any
		# @AssociationMultiplicity 1

