from datetime import date


class RetirementAgeCalculator:
    def __init__(self, year_of_birth, month_of_birth):
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.current_year = date.today().year
        self.retire_age = 0
        self.retire_months = 0
        self.month_of_retirement = ""
        self.year_of_retirement = 0
        self.set_retire_age_and_months()
        self.set_year_of_retirement()
        self.set_month_of_retirement()

    # calculate the age of the user
    def get_current_age(self):
        age = self.current_year - self.year_of_birth
        return age

    # get month of the year
    def get_month(self, month):
        months = [0, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        return months[month]

    # use NRA form to set retire age and months depending on user's year of birth
    def set_retire_age_and_months(self):
        if self.year_of_birth < 1943:
            self.retire_age = 65
            if self.year_of_birth == 1938:
                self.retire_months = 2
            elif self.year_of_birth == 1939:
                self.retire_months = 4
            elif self.year_of_birth == 1940:
                self.retire_months = 6
            elif self.year_of_birth == 1941:
                self.retire_months = 8
            elif self.year_of_birth == 1942:
                self.retire_months = 10
        elif self.year_of_birth < 1960:
            self.retire_age = 66
            if self.year_of_birth == 1955:
                self.retire_months = 2
            elif self.year_of_birth == 1956:
                self.retire_months = 4
            elif self.year_of_birth == 1957:
                self.retire_months = 6
            elif self.year_of_birth == 1958:
                self.retire_months = 8
            elif self.year_of_birth == 1959:
                self.retire_months = 10
        else:
            self.retire_age = 67

    # set month of the year of retirement
    def set_month_of_retirement(self):
        birth_and_retirement_month = self.month_of_birth + self.retire_months
        if birth_and_retirement_month > 12:
            self.year_of_retirement += 1
        if birth_and_retirement_month == 12:
            self.month_of_retirement = self.get_month(birth_and_retirement_month)
        else:
            self.month_of_retirement = self.get_month(birth_and_retirement_month % 12)

    # set year of the retirement
    def set_year_of_retirement(self):
        self.year_of_retirement = self.retire_age - self.get_current_age() + self.current_year
