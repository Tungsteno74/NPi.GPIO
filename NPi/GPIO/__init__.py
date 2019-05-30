from NPi._GPIO import *

def pkg_metadata (*args):
  from pkg_resources import get_distribution
  pkg = get_distribution(args[0])
  return getattr(pkg, args[1])

__version__ = pkg_metadata("NPi.GPIO", "version")
