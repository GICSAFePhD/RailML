#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import EntityIS
from Infrastructure import VisualizationBaseElement
from Interlocking import EntityIL
from Interlocking import EntityILref
from typing import List

class anyAttribute(object):
	"""provide an extension point for non-railML 'any attribute' in a foreign namespace"""
	def __init__(self):
		self._unnamed_EntityIS_ : EntityIS = None
		self._unnamed_VisualizationBaseElement_ : VisualizationBaseElement = None
		self._unnamed_EntityIL_ : EntityIL = None
		self._unnamed_EntityILref_ : EntityILref = None
