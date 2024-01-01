import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employee = pd.DataFrame(employees)
    employee['salary'] = employee['salary'] * 2
    return employee