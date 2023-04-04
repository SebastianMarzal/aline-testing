from utils import dictionarize
import requests
from faker import Faker
import random

class ApplicantsInterface:
  """
  The Applicants producer generates random applicants
  based on Membership applications.
  """
  TIMEOUT=100
  def __init__(self, itf, port, host = "http://localhost"):
    self.interface = itf
    self.port = port
    self.host = host

  def create(self, applicant):
    headers = self.interface.authorized_headers()
    post_url = self.host + ":" + self.port + "/applicants"
    response = requests.post(post_url, json=applicant, headers=headers, timeout=self.TIMEOUT)
    if response.status_code == 201:
      response_contents = dictionarize(response.content, response.encoding)
      return response_contents["id"]
    if response.status_code == 400:
      raise ValueError("400: The applicant data is not valid.")
    elif response.status_code == 403:
      raise ValueError("403: More than one piece of data is invalid.")
    elif response.status_code == 409:
      raise ValueError("409: The applicant data conflicts with other data.")

  def get(self, user_id):
    headers = self.interface.authorized_headers()
    get_url = self.host + ":" + self.port + "/applicants/" + str(user_id)
    response = requests.get(get_url, headers=headers, timeout=self.TIMEOUT)
    if response.status_code == 200:
      return dictionarize(response.content, response.encoding)
    if response.status_code == 403:
      raise ValueError("403: Prohibited.")
    elif response.status_code == 404:
      raise ValueError("404: Applicant does not exist.")

  def get_all(self):
    headers = self.interface.authorized_headers()
    get_url = self.host + ":" + self.port + "/applicants"
    response = requests.get(get_url, headers=headers, timeout=self.TIMEOUT)
    if response.status_code == 200:
      return dictionarize(response.content, response.encoding)["content"]
    if response.status_code == 403:
      raise ValueError("403: Prohibited.")

  def num_applicants(self):
    return len(self.get_all())

  def update(self, user_id, applicant):
    """update
    Updates a user by id

    Args:
        id (int)
        applicant (dict)

    Returns:
        True: If update was succesful, else raises an error

    WARNING! DO NOT USE! The request will fail unless ALL unique identifiers
    (SSN, DL, Phone #, etc.) are changed.
    """
    headers = self.interface.authorized_headers()
    put_url = self.host + ":" + self.port + "/applicants/" + str(user_id)
    response = requests.put(put_url, json=applicant, headers=headers, timeout=self.TIMEOUT)
    if response.status_code == 204:
      return True
    if response.status_code == 400:
      raise ValueError("400: New values were not valid.")
    elif response.status_code == 403:
      raise ValueError("403: Prohibited.")
    elif response.status_code == 404:
      raise ValueError("404: Applicant to update was not found.")
    elif response.status_code == 409:
      raise ValueError("409: Unique identifiers remained the same.")

  def delete(self, user_id):
    headers = self.interface.authorized_headers()
    delete_url = self.host + ":" + self.port + "/applicants/" + str(user_id)
    response = requests.delete(delete_url, headers=headers, timeout=self.TIMEOUT)
    if response.status_code == 204:
      return True
    if response.status_code == 404:
      raise ValueError("404: Applicant was not found.")

  def delete_all(self):
    all_entries = self.get_all()
    for entry in all_entries:
      self.delete(entry["id"])

  def create_random(self):
    faker = Faker()
    dob = faker.date_of_birth(minimum_age=18)
    formatted_dob = str(dob.year) + "-"
    formatted_dob += str(dob.month) if dob.month > 9 else ("0" + str(dob.month))
    formatted_dob += "-"
    formatted_dob += str(dob.day) if dob.day > 9 else ("0" + str(dob.day))
    gender = random.choice(["MALE", "FEMALE"])
    address = faker.building_number() + " " + faker.street_name() + " " + faker.street_suffix()
    city = faker.city()
    state = faker.state_abbr()
    zipcode = faker.zipcode()
    phone = faker.msisdn()
    applicant = {
      "firstName": faker.first_name_male() if gender == "MALE" else faker.first_name_female(),
      "middleName": faker.first_name_male() if gender == "MALE" else faker.first_name_female(),
      "lastName": faker.last_name(),
      "dateOfBirth": formatted_dob,
      "gender": gender,
      "email": faker.email(),
      "phone": phone[:3] + " " + phone[3:6] + " " + phone[6:10],
      "socialSecurity": " ".join(faker.ssn().split("-")),
      "driversLicense": "".join(faker.license_plate().split()),
      "income": random.randint(4000, 100000),
      "address": address,
      "city": city,
      "state": state,
      "zipcode": zipcode,
      "mailingAddress": address,
      "mailingCity": city,
      "mailingState": state,
      "mailingZipcode": zipcode
    }
    return self.create(applicant)
