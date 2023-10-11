import csv, pandas

WEATHER_DATA = "weather_data.csv"


def read_temp_from_csv_without_panda(file_name):
    with open(file_name) as data_file:
        data = csv.reader(data_file)
        temperature = []
        for row in data:
            if row[1] != "temp":
                temperature.append(row[1])
    print(temperature)


# Pandas know the header contain columns name
# s
def read_temp_from_csv_with_panda(file_name):
    data = pandas.read_csv(WEATHER_DATA)
    temp_list = data["temp"].to_list()
    print(temp_list)

def get_average_min_max(file_name):
    data = pandas.read_csv(WEATHER_DATA)
    print(f"\nAverage temperature with Panda: {data['temp'].mean()}")
    print(f"Max temperature with Panda: {data['temp'].max()}")
    print(f"Min temperature with Panda: {data.temp.min()}")


def read_from_to_dictionnary(file_name):
    data = pandas.read_csv(WEATHER_DATA)
    data_dictionary = data.to_dict()
    print(data_dictionary)


def get_data_in_row(file_name):
    data = pandas.read_csv(WEATHER_DATA)
    print(data[data.day == "Monday"])


def get_data_in_row_where_temp_max(file_name):
    data = pandas.read_csv(WEATHER_DATA)
    print(data[data.temp == data.temp.max()])


def create_dataframe_from_scratch():
    data_dict = {
        "students": ["Teayeon", "Seohyun", "Sooyung"],
        "scores": [56, 89, 68]
    }
    # Initialise Dataframe with new datas
    data = pandas.DataFrame(data_dict)
    data.to_csv("new_data.csv")

def main():
    read_temp_from_csv_without_panda(WEATHER_DATA)
    read_temp_from_csv_with_panda(WEATHER_DATA)
    read_from_to_dictionnary(WEATHER_DATA)
    get_average_min_max(WEATHER_DATA)
    get_data_in_row(WEATHER_DATA)
    get_data_in_row_where_temp_max(WEATHER_DATA)
    create_dataframe_from_scratch()


if __name__ == "__main__":
    main()


