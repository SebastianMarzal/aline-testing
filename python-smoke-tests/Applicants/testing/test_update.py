from aline_itf import AlineInterface
from ..applicants import ApplicantsInterface

def test_update():
  applicant_before = {
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

  applicant_after = {
    "firstName": "Barry",
    "middleName": "Hussein",
    "lastName": "Obama",
    "dateOfBirth": "1961-08-04",
    "gender": "MALE",
    "email": "barryobama@gmail.com",
    "phone": "123 456 7892",
    "socialSecurity": "123 55 6789",
    "driversLicense": "123452BC",
    "income": 1000001,
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

  user_id = applicants.create(applicant_before)
  created_applicant = applicants.get(user_id)
  c_a_items = created_applicant.items()
  for tup in applicant_before.items():
    assert tup in c_a_items

  applicants.update(user_id, applicant_after)
  created_applicant_after = applicants.get(user_id)
  c_a_items_after = created_applicant_after.items()
  for tup in applicant_after.items():
    assert tup in c_a_items_after
