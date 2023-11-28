import random
import pandas

names = ["Alexandra", "Stéphanie", "Sophie", "Cécile"]

def list_comprehension():
    numbers = [1, 2, 3]
    new_numbers = [n+1 for n in numbers]
    print(numbers)
    print(new_numbers)

    name = input("Enter your name: ")
    letters = [letter for letter in name]
    print(letters)

    range_list = [num * 2 for num in range(1, 7)]
    print(range_list)


def list_comprehension_with_condition():
    even_numbers = [number for number in range(0, 100) if number % 2 == 0]
    print(even_numbers)
    short_names = [ name.upper() for name in names if len(name) >=6]
    print(short_names)


def dictionary_comprehension_with_condition():
    students_scores = {name: random.randint(5,20) for name in names}
    passed_student ={name:score for name, score in students_scores.items() if score >= 10}
    print(students_scores)
    print(passed_student)


def iterate_over_pandas_dataframe():
    student_dict = {
        "students": ["Alexandra", "Stéphanie", "Sophie", "Cécile"],
        "score": [54, 89, 46, 89]
    }
    # loop over dictionnary
    for (key, value) in student_dict.items():
        print(f"key: {key}")
        print(f"value: {value}")

    student_dataframe = pandas.DataFrame(student_dict)
    print(student_dataframe)
    # loop over Dataframe
    print(f"\nkey:")
    for (key, value) in student_dataframe.items():
        print(key)
        print(f"\nvalue:")
    for (key, value) in student_dataframe.items():
        print(value)

    # loop through rows
    print("row.students:")
    for (index, row) in student_dataframe.iterrows():
        print(row.students)
    print("row.score")
    for (index, row) in student_dataframe.iterrows():
        print(row.score)

def main():
    list_comprehension()
    list_comprehension_with_condition()
    dictionary_comprehension_with_condition()
    iterate_over_pandas_dataframe()


if __name__ == '__main__':
    main()
