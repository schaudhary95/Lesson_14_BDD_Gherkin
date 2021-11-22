from pytest_bdd import scenarios, given, when, then, parsers
from retirementAgeCalculator import RetirementAgeCalculator

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'year': int,
    'month': int,
    'retireAge': int,
    'addMonths': int,
    'retireYear': int,
}


@scenarios("../features/retirement.feature", example_converters=CONVERTERS)
def test_retirement():
    pass


@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year_month1(year, month):
    return RetirementAgeCalculator(year, month)


@when("the retire age is returned")
def get_retire_age(birth_year_month1):
    return birth_year_month1.retire_age


@then(parsers.cfparse("verify the age is equals '{expected:number}'", extra_types=EXTRA_TYPES))
def verify_age(get_retire_age, expected):
    assert get_retire_age == 67


@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year_month2(year, month):
    return RetirementAgeCalculator(year, month)


@when("the year of retirement is returned")
def get_year_of_retirement(birth_year_month2):
    return birth_year_month2.year_of_retirement


@then(parsers.cfparse("verify the year is equals '{expected_year:number}'", extra_types=EXTRA_TYPES))
def verify_year_of_retirement(get_year_of_retirement, expected_year):
    assert get_year_of_retirement == expected_year


@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year_month3(year, month):
    return RetirementAgeCalculator(year, month)


@when("the additional months returned")
def get_add_months(birth_year_month3):
    return birth_year_month3.retire_months


@then(parsers.cfparse("verify the additional months is equals '{expected_add_month:number}'", extra_types=EXTRA_TYPES))
def verify_add_months(get_add_months, expected_add_month):
    assert get_add_months == expected_add_month


@given('the year and month of birth "<year>", "<month>"')
def birth_year_month4(year, month):
    return RetirementAgeCalculator(year, month)


@then('verify "<retireAge>", "<addMonths>", "<retireMonth>", and "<retireYear>"')
def verify_all(birth_year_month4, retireAge, addMonths, retireMonth, retireYear):
    obj = birth_year_month4
    assert obj.retire_age == retireAge
    assert obj.retire_months == addMonths
    assert obj.month_of_retirement == retireMonth
    assert obj.year_of_retirement == retireYear
