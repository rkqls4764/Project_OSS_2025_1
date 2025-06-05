from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 관련")
        print("2. 수입 관련")
        print("3. 종료")
        choice = input("선택 > ")

        if choice == "1":
            while True:
                print("==== 지출 관련 ====")
                print("1. 추가")
                print("2. 목록 보기")
                print("3. 총합 보기")
                print("4. 뒤로 가기")
                choice = input("선택 > ")
                
                if choice == "1":
                    category = input("카테고리 (예: 식비, 교통 등): ")
                    description = input("설명: ")
                    try:
                        amount = int(input("금액(원): "))
                    except ValueError:
                        print("잘못된 금액입니다.\n")
                        continue
                    budget.add_expense(category, description, amount)

                elif choice == "2":
                    budget.list_expenses()

                elif choice == "3":
                    budget.total_spent()

                elif choice == "4":
                    break

                else:
                    print("잘못된 선택입니다.\n")

        elif choice == "2":
            while True:
                print("==== 수입 관련 ====")
                print("1. 추가")
                print("2. 목록 보기")
                print("3. 총합 보기")
                print("4. 뒤로 가기")
                choice = input("선택 > ")
                
                if choice == "1":
                    category = input("카테고리 (예: 식비, 교통 등): ")
                    description = input("설명: ")
                    try:
                        amount = int(input("금액(원): "))
                    except ValueError:
                        print("잘못된 금액입니다.\n")
                        continue
                    budget.add_income(category, description, amount)

                elif choice == "2":
                    budget.list_incomes()

                elif choice == "3":
                    budget.total_income()

                elif choice == "4":
                    break

                else:
                    print("잘못된 선택입니다.\n")

        elif choice == "3":
            print("가계부를 종료합니다.\n")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
