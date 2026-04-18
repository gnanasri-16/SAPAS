def clean_name( student_name):
    # Remove extra spaces
    student_name =  student_name.strip()

    #  Convert to proper format
    student_name =  student_name.title()

    # Check empty input
    if  student_name == "":
        raise ValueError("Name cannot be empty")

    #  Allow only alphabets and spaces
    if not all(ch.isalpha() or ch.isspace() for ch in  student_name):
        raise ValueError("Name must contain only letters")

    return  student_name