def pkg_metadata (pkg_name, pkg_attr):
  from pkg_resources import get_distribution
  pkg = get_distribution(pkg_name)
  return getattr(pkg,pkg_attr)


# __variables__ with double-quoted values will be available in setup.py
__version__ = pkg_metadata("NPi.GPIO", "version")

from NPi._GPIO import *

