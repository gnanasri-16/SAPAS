def validate_marks(m):
    try:
        #  Convert to integer
        m = int(m)

        #  Range validation
        if m < 0 or m > 100:
            raise ValueError("Marks must be between 0 and 100")

        return m

    except ValueError:
        print("Invalid input! Enter marks between 0 and 100")
        return None