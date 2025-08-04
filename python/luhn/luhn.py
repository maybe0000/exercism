class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        cleaned_str = self.card_num.replace(" ", "")
        if len(cleaned_str) <= 1 or not cleaned_str.isdigit():
            return False
        sum = 0
        for i, c in enumerate(reversed(cleaned_str)):
            n = int(c)
            if i % 2 == 1:
                doubled = n * 2
                sum += doubled - 9 if doubled > 9 else doubled
            else:
                sum += n
        return sum % 10 == 0
