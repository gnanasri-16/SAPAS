def parser_log(text):
    try:
        #  Clean input
        text = text.strip()

        if not text:
            return []

        #  Split words
        words = text.split()

        #  Remove special characters
        cleaned = []
        for w in words:
            w = ''.join(ch for ch in w if ch.isalnum())
            if w:
                cleaned.append(w.lower())

        return cleaned

    except Exception as e:
        print("Error parsing log:", e)
        return []