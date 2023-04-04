from aline_itf import AlineInterface

class BanksInterface:
  """
  Creates dummy banks (Locations/Branches) for Aline Financial.
  """
  def __init__(self, itf):
    self.interface = itf
  
  