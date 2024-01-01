import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employee = pd.DataFrame(employees)
    bonus = employee['salary'] * 2
    employee['bonus'] = bonus
    return employee