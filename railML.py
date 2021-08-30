import sys
sys.path.append('.')
from RailML.Common import Metadata
from RailML.Common import Common
from RailML.Infrastructure import Infrastructure
from RailML.Interlocking import Interlocking
from RailML import aRailML
#from typing import List

class railML():
	"""This is the root element of any railML file."""
	@property
	def Metadata(self):
		return self.___metadata
	@property
	def Common(self):
		return self.___common
	@property
	def Infrastructure(self):
		return self.___infrastructure
	@property
	def Interlocking(self):
		return self.___interlocking
	@property
	def aRailML(self):
		return self.___aRailML

	@Metadata.setter
	def Metadata(self, aMetadata : Metadata):
		self.___metadata = aMetadata
	@Common.setter
	def Common(self, aCommon : Common):
		self.___common = aCommon
	@Infrastructure.setter
	def Infrastructure(self, aInfrastructure : Infrastructure):
		self.___infrastructure = aInfrastructure
	@Interlocking.setter
	def Interlocking(self, aInterlocking : Interlocking):
		self.___interlocking = aInterlocking
	@aRailML.setter
	def aRailML(self, aaRailML : aRailML):
		self.___aRailML = aaRailML
	
	def create_metadata(self):
		self.Metadata = Metadata.Metadata()
	def create_common(self):
		self.Common = Common.Common()
	def create_infrastructure(self):
		self.Infrastructure = Infrastructure.Infrastructure()
	def create_interlocking(self):
		self.Interlocking = Interlocking.Interlocking()

	def __init__(self):
		self.___metadata : Metadata = None
		# @AssociationType Common.Metadata
		# @AssociationMultiplicity 0..1
		self.___common : Common = None
		# @AssociationType Common.Common
		# @AssociationMultiplicity 0..1
		# """root element for railML3 common model"""
		self.___infrastructure : Infrastructure = None
		# @AssociationType Infrastructure.Infrastructure
		# @AssociationMultiplicity 0..1
		# """root element for railML3 infrastructure model"""
		self.___interlocking : Interlocking = None
		# @AssociationType Interlocking.Interlocking
		# @AssociationMultiplicity 0..1
		# """root element for railML3 interlocking model"""
		self.___aRailML : aRailML = None
		"""# @AssociationKind Aggregation"""