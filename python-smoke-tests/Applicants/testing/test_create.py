import pytest
from aline_itf import AlineInterface
from ..applicants import ApplicantsInterface

def test_create_valid():
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

def test_create_invalid_400():
  applicant = {
    "firstName": "Barack",
    "middleName": "Hussein",
    "lastName": "Obama",
    "dateOfBirth": "1961-08-04",
    "gender": "MALE",
    "email": "barackobama@gmail.com",
    "phone": "123 456 212327890",
    "socialSecurity": "123 45 6789",
    "driversLicense": "12345ABC",
    "income": 10,
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
  with pytest.raises(Exception):
    applicants.create(applicant)

def test_create_invalid_403():
  applicant = {
    "firstName": "Barack",
    "middleName": "Hussein",
    "lastName": "Obama",
    "dateOfBirth": "1961-08-04",
    "gender": "MALE",
    "email": "barackobama@gmail.com",
    "phone": "123 456 212327890",
    "socialSecurity": "123 45 6789",
    "driversLicense": "12345ABC",
    "income": 10,
    "address": "123 Obama Dr",
    "city": "Honolulu",
    "state": "HI",
    "zipcode": "12345",
    "mailingAddress": "1232132asdObamar",
    "mailingCity": "Honolulu",
    "mailingState": "HI",
    "mailingZipcode": "12345"
  }

  a_itf = AlineInterface("8070", "admin1", "P@ssword1")
  applicants = ApplicantsInterface(a_itf, "8071")
  applicants.delete_all()
  with pytest.raises(Exception):
    applicants.create(applicant)

def test_create_invalid_409():
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
    "income": 10,
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
  applicants.create(applicant)
  with pytest.raises(Exception):
    applicants.create(applicant)

def test_create_random():
  a_itf = AlineInterface("8070", "admin1", "P@ssword1")
  applicants = ApplicantsInterface(a_itf, "8071")
  user_id = applicants.create_random()
  created_applicant = applicants.get(user_id)
  assert isinstance(created_applicant, dict)
