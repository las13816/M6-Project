from schedule import Schedule


def menu():
    print("\nCourse Schedule System")
    print("1. Display all courses")
    print("2. Search by subject")
    print("3. Search by subject and catalog")
    print("4. Search by instructor last name")
    print("5. Quit")


def main():
    schedule = Schedule()
    schedule.load_from_csv("courses.csv")

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter subject (e.g., BIO): ")
            results = schedule.find_by_subject(subject)
            schedule.print(results)

        elif choice == "3":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")
            results = schedule.find_by_subject_catalog(subject, catalog)
            schedule.print(results)

        elif choice == "4":
            name = input("Enter instructor last name: ")
            results = schedule.find_by_instructor_last_name(name)
            schedule.print(results)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()