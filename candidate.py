class Candidate:

  def __init__(self, name):
    self.name = name
    self.experiences = []

  def add_experience(self, role, start_date, end_date, location,description=""):
    self.experiences.append({
      "role" : role,
      "start_date" : start_date,
      "end_date" : end_date,
      "location" : location,
      "description" :description 
      })

  def to_dict(self):
    return {
        "name": self.name,
        "experiences": self.experiences,
    }

  def __repr__(self):
    return f"Candidate({self.name}, {self.experiences})"
