#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ServiceSection
from typing import List

class ServiceSections(object):
	@property
	def ServiceSection(self) -> ServiceSection:
		return self.___serviceSection
	
	@ServiceSection.setter
	def ServiceSection(self, *aServiceSection : ServiceSection):
		self.___serviceSection = ServiceSection

	def __init__(self):
		self.___serviceSection : ServiceSection = ServiceSection.ServiceSection()
		# @AssociationType Infrastructure.ServiceSection*
		# @AssociationMultiplicity 1..*

