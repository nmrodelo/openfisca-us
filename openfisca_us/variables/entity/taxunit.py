from openfisca_core.model_api import *
from openfisca_us.entities import *


class taxunit_id(Variable):
    value_type = float
    entity = TaxUnit
    label = u"Unique reference for this tax unit"
    definition_period = ETERNITY


class person_taxunit_id(Variable):
    value_type = int
    entity = Person
    label = u"Unique reference for the tax unit of this person"
    definition_period = ETERNITY


class MARSType(Enum):
    SINGLE = "Single"
    JOINT = "Joint"
    SEPARATE = "Separate"
    HOUSEHOLD_HEAD = ("Head of household",)
    WIDOW = "Widow(er)"


class MARS(Variable):
    value_type = Enum
    entity = TaxUnit
    possible_values = MARSType
    default_value = MARSType.SINGLE
    definition_period = YEAR
    label = "MARS Status for the tax unit"
