class Bank:
    def __init__(self, Bank_Name, No_of_cust):
        self.name = Bank_Name
        self.No_of_cust = No_of_cust

    def display(self):
        print(f"Bank name is {self.name} and no of cust are {self.No_of_cust}")


class GOVT_BANK(Bank):
    def __init__(self, Bank_Name, No_of_cust, Branch_Name, IIFC_COde):
        super().__init__(Bank_Name, No_of_cust)
        self.branch_name = Branch_Name
        self.iifc_code = IIFC_COde

    def display(self):
        super().display()
        print(f"Branch name is {self.branch_name} and iifc code is {self.iifc_code}")


class PRIVATE_BANK(Bank):
    def __init__(self, Bank_Name, No_of_cust, Branch_Name, IIFC_COde):
        super().__init__(Bank_Name, No_of_cust)
        self.branch_name = Branch_Name
        self.iifc_code = IIFC_COde

    def display(self):
        super().display()
        print(f"branch name is{self.branch_name} and iifc code is {self.iifc_code}")


def main():
    govt_bank = GOVT_BANK("Public Bank", 5000, "Main Branch", "GOV123")
    private_bank = PRIVATE_BANK("Private Bank", 3000, "City Branch", "PVT456")

    print("\nDetails of Government Bank:")
    govt_bank.display()

    print("\nDetails of Private Bank:")
    private_bank.display()


if __name__ == "__main__":
    main()
