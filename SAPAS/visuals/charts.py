def show_graph(data):
    try:
        import matplotlib.pyplot as plt

        if not data:
            print("No data to display")
            return

        student_names = [s.name for s in data.values()]
        marks = [s.marks for s in data.values()]

        #  Bar graph
        plt.figure()
        plt.bar(student_names, marks)

        # Labels
        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.title("Student Marks Analysis")

        #  Show values on bars
        for i, m in enumerate(marks):
            plt.text(i, m, str(m), ha='center')

        plt.show()

    except ImportError:
        print("Matplotlib not installed")
    except Exception as e:
        print("Error:", e)