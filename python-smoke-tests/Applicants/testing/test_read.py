import pytest
from aline_itf import AlineInterface
from ..applicants import ApplicantsInterface

def test_get():
  applicant = {
    "firstName": "Barack",
    "middleName": "Hussein",
    "lastName": "Obama",
    "dateOfBirth": "1961-08-04",
    "gender": "MALE",
    "email": "barackobama@gmail.com",
    "phone": "123 456 7890",
    "socialSecurity": "123 45 6789",
    "driversLicense": "12345ABC",
    "income": 1000000,
    "address": "123 Obama Dr",
    "city": "Honolulu",
    "state": "HI",
    "zipcode": "12345",
    "mailingAddress": "123 Obama Dr",
    "mailingCity": "Honolulu",
    "mailingState": "HI",
    "mailingZipcode": "12345"
  }

  a_itf = AlineInterface("8070", "admin1", "P@ssword1")
  applicants = ApplicantsInterface(a_itf, "8071")
  applicants.delete_all()
  user_id = applicants.create(applicant)
  created_applicant = applicants.get(user_id)
  c_a_items = created_applicant.items()
  for tup in applicant.items():
    assert tup in c_a_items

def test_get_all():
  a_itf = AlineInterface("8070", "admin1", "P@ssword1")
  applicants = ApplicantsInterface(a_itf, "8071")
  applicants.delete_all()
  assert applicants.get_all() == []
  for _ in range(10):
    applicants.create_random()
  assert len(applicants.get_all()) == 10

def test_get_invalid():
  applicant = {
    "firstName": "Barack",
    "middleName": "Hussein",
    "lastName": "Obama",
    "dateOfBirth": "1961-08-04",
    "gender": "MALE",
    "email": "barackobama@gmail.com",
    "phone": "123 456 7890",
    "socialSecurity": "123 45 6789",
    "driversLicense": "12345ABC",
    "income": 1000000,
    "address": "123 Obama Dr",
    "city": "Honolulu",
    "state": "HI",
    "zipcode": "12345",
    "mailingAddress": "123 Obama Dr",
    "mailingCity": "Honolulu",
    "mailingState": "HI",
    "mailingZipcode": "12345"
  }

  a_itf = AlineInterface("8070", "admin1", "P@ssword1")
  applicants = ApplicantsInterface(a_itf, "8071")
  applicants.delete_all()
  user_id = applicants.create(applicant)
  with pytest.raises(ValueError):
    applicants.get(user_id + 1)
