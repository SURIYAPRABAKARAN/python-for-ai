def main():
    print("hi")
    finalSalaryResult,bonusResult = salaryCal(100,200)
    # print("finalSalaryResult",finalSalaryResult,"bonusResult",bonusResult)
    print(f"finalSalaryResult : {finalSalaryResult} , bonusResult : {bonusResult}")


def salaryCal(basic,bonus=100):
    finalSalary = basic + bonus
    print("finalSalary",finalSalary)
    return finalSalary,bonus + 1
    





if __name__ == "__main__":
    main()