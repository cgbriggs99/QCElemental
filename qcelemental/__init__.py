"""
Main init for QCElemental
"""

# Handle singletons, not their classes or modules
from . import (
    covalent_radii,
    dft_functional_info,
    models,
    molparse,
    molutil,
    periodic_table,
    physical_constants,
    util,
    vanderwaals_radii,
)
from .datum import Datum
from .exceptions import ChoicesError, DataUnavailableError, MoleculeFormatError, NotAnElementError, ValidationError

# Handle versioneer
from .extras import get_information

# from .physical_constants import PhysicalConstantsContext, constants
from .testing import compare, compare_recursive, compare_values

# Expose singletons from the modules
periodictable = periodic_table.periodictable
PhysicalConstantsContext = physical_constants.PhysicalConstantsContext
constants = physical_constants.constants
CovalentRadii = covalent_radii.CovalentRadii
covalentradii = covalent_radii.covalentradii
VanderWaalsRadii = vanderwaals_radii.VanderWaalsRadii
vdwradii = vanderwaals_radii.vdwradii
dftfunctionalinfo = dft_functional_info.dftfunctionalinfo
DFTFunctionalInfo = dft_functional_info.DFTFunctionalInfo

# Remove singleton-providing modules from known imported objects
del periodic_table
del physical_constants
del covalent_radii
del vanderwaals_radii
del dft_functional_info

__version__ = get_information("version")
__git_revision__ = get_information("git_revision")
del get_information
