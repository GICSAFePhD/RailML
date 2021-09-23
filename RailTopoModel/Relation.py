#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tNavigability, tUsage
from RailML.RailTopoModel import RTM_NetworkResource
from typing import List

class Relation(RTM_NetworkResource.RTM_NetworkResource):
	@property
	def Ref(self) -> str:
		return self.___ref

	@Ref.setter
	def Ref(self, aRef : str):
		self.___ref = aRef

	def __init__(self):
		super().__init__()
		self.___ref : str = ""