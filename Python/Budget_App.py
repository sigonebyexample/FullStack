def create_spend_chart(categories):
    withdrawals = []
    total_spent = 0
    for cat in categories:
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(spent)
        total_spent += spent

    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        percentages = [(w / total_spent) * 100 for w in withdrawals]
        percentages = [int(p // 10) * 10 for p in percentages]
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for p in percentages:
            if p >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n" 
    dashes = "-" * (3 * len(categories) + 1)
    chart += "    " + dashes + "\n"
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "    "
        for name in names:
            if i < len(name):
                chart += " " + name[i] + " "
            else:
                chart += "   "
        chart += " \n"
    chart = chart.rstrip('\n')
    return chart
