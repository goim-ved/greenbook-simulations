from collections import Counter

dates = [
    ("Mar", 4), ("Mar", 5), ("Mar", 8),
    ("Jun", 4), ("Jun", 7),
    ("Sep", 1), ("Sep", 5),
    ("Dec", 1), ("Dec", 2), ("Dec", 8)
]

print("All dates:")
print(dates)
print()

day_list = []

for month, day in dates:
    day_list.append(day)

day_counts = Counter(day_list)

unique_days = []

for day in day_counts:
    if day_counts[day] == 1:
        unique_days.append(day)

print("Unique days (if C got these, he'd instantly know):")
print(unique_days)
print()

print("You say: I don't know and I know C doesn't know")
print()

valid_after_you = []

for m, d in dates:
    days_in_this_month = []

    for m2, d2 in dates:
        if m2 == m:
            days_in_this_month.append(d2)

    has_unique = False
    for day in days_in_this_month:
        if day in unique_days:
            has_unique = True

    if not has_unique:
        valid_after_you.append((m, d))

print("After your first statement (removed June & Decemeber):")
print(valid_after_you)
print()

print("Now C says: Now I know")
print()

day_to_dates = {}

for m, d in valid_after_you:
    if d not in day_to_dates:
        day_to_dates[d] = []
    day_to_dates[d].append((m, d))

valid_after_c = []

for d in day_to_dates:
    if len(day_to_dates[d]) == 1:
        valid_after_c.append(day_to_dates[d][0])

print("After C's statement (removed all 5s):")
print(valid_after_c)
print()

print("Now you say: Now I also know")
print()

month_to_dates = {}

for m, d in valid_after_c:
    if m not in month_to_dates:
        month_to_dates[m] = []
    month_to_dates[m].append((m, d))

final_answer = []

for m in month_to_dates:
    if len(month_to_dates[m]) == 1:
        final_answer.append(month_to_dates[m][0])

print("Final answer:")
print(final_answer)