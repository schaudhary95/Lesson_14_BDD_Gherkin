Feature: Full Retirement Calculator
  As a citizen, I want to use Retirement calculator to calculate
  when I will reach my retirement,
  so I can make plans after I retired.


  Scenario: Calculate Retire Age
    Given the year and month of birth "1982", "1"
    When the retire age is returned
    Then verify the age is equals '67'


  Scenario: Calculate the Year of Retirement
    Given the year and month of birth '2000', '5'
    When the year of retirement is returned
    Then verify the year is equals '2067'

  Scenario: Calculate Additional Months for Full Retirement Age
    Given the year and month of birth '1942', '3'
    When the additional months returned
    Then verify the additional months is equals '10'

  Scenario Outline: Calculate Full Retirement Age with Different Year and Month
    Given the year and month of birth "<year>", "<month>"
    Then verify "<retireAge>", "<addMonths>", "<retireMonth>", and "<retireYear>"

    Examples: Years, Months, Retire Age, Additional Months, Retire Month, and Retire Year
      | year | month | retireAge | addMonths | retireMonth | retireYear |
      | 1954 | 9     | 66        | 0        | September   | 2020       |
      | 1959 | 6     | 10        | 10       | April       | 2026       |
      | 1955 | 7     | 2         | 2        | September   | 2021       |
      | 1937 | 5     | 65        | 0        | May         | 2002       |
