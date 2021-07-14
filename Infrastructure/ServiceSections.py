#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.ServiceSection import ServiceSection
from typing import List

class ServiceSections(object):
	def setServiceSection(self, *aServiceSection : ServiceSection):
		self._serviceSection = aServiceSection

	def getServiceSection(self) -> ServiceSection:
		return self._serviceSection

	def __init__(self):
		self._serviceSection : ServiceSection = None
		# @AssociationType Infrastructure.ServiceSection*
		# @AssociationMultiplicity 1..*

