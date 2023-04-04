from aline_itf import AlineInterface
from ..applicants import ApplicantsInterface

def test_delete():
  a_itf = AlineInterface('8070', 'admin1', 'P@ssword1')
  applicants = ApplicantsInterface(a_itf, '8071')
  applicants.delete_all()
  id_1 = applicants.create_random()
  id_2 = applicants.create_random()
  assert applicants.num_applicants() == 2
  applicants.delete(id_1)
  applicants.delete(id_2)
  assert applicants.num_applicants() == 0

def test_delete_all():
  a_itf = AlineInterface('8070', 'admin1', 'P@ssword1')
  applicants = ApplicantsInterface(a_itf, '8071')
  applicants.delete_all()
  applicants.create_random()
  applicants.create_random()
  assert applicants.num_applicants() == 2
  applicants.delete_all()
  assert applicants.num_applicants() == 0
