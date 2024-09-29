def check_availability(cur_amount: int, ordered_amount: int) -> bool:
    if cur_amount < ordered_amount:
        raise ValueError("Not enough products in stock")
    return True
