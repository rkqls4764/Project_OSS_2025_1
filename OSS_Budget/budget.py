import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # 태그별 지출 합계 조회 함수
    def tag_spent(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        tag_totals = {}
        for e in self.expenses:
            if e.category not in tag_totals:
                tag_totals[e.category] = 0
            tag_totals[e.category] += e.amount
        
        print("\n[태그별 지출 합계]")
        for tag, total in tag_totals.items():
            print(f"{tag}: {total}원")
        print()

