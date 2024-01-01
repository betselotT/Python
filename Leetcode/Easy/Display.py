import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    employee = pd.DataFrame(employees)
    answer = employee.head(3)
    return answer