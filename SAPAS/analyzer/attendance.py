def attendance_percentage(present, total):
    try:
        #  Convert to numbers
        present = int(present)
        total = int(total)

        # Validate values
        if present < 0 or total < 0:
            raise ValueError("Values cannot be negative")

        if present > total:
            raise ValueError("Present days cannot exceed total days")

        #  Avoid division by zero
        if total == 0:
            return 0

        percentage = (present / total) * 100

        return round(percentage, 2)

    except Exception as e:
        print("Error:", e)
        return None