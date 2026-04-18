#  Total Marks
def total(data):
    try:
        return sum(s.marks for s in data.values())
    except:
        return 0


#  Average Marks
def average(data):
    if not data:
        return 0
    return total(data) / len(data)


#  Topper
def topper(data):
    if not data:
        return None
    return max(data.values(), key=lambda x: x.marks)


# Lowest scorer
def lowest(data):
    if not data:
        return None
    return min(data.values(), key=lambda x: x.marks)


#  Pass count
def pass_count(data):
    return sum(1 for s in data.values() if s.marks >= 40)


#  Fail count
def fail_count(data):
    return sum(1 for s in data.values() if s.marks < 40)


#  Grade distribution
def grade_distribution(data):
    grades = {"A+":0, "A":0, "B":0, "C":0, "F":0}

    for s in data.values():
        m = s.marks

        if m >= 90: grades["A+"] += 1
        elif m >= 75: grades["A"] += 1
        elif m >= 60: grades["B"] += 1
        elif m >= 40: grades["C"] += 1
        else: grades["F"] += 1

    return grades


#  Search student by name
def search_by_name(data, name):
    result = []
    for s in data.values():
        if s.name.lower() == name.lower():
            result.append(s)
    return result