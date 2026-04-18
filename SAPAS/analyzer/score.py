def highest(data):
    try:
        if not data:
            return None

        return max(data.values(), key=lambda x: x.marks)

    except Exception as e:
        print("Error finding highest:", e)
        return None


def lowest(data):
    try:
        if not data:
            return None

        return min(data.values(), key=lambda x: x.marks)

    except Exception as e:
        print("Error finding lowest:", e)
        return None