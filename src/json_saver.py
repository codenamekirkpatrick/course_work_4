import json

from config import VACANCIES_PATH
from src.hh_api import HeadHunterAPI
from src.saver import Saver
from src.vacancy import Vacancy


class JSONSaver(Saver):

    def write_data(self, data_json):

        try:
            data = json.load(open(VACANCIES_PATH))
        except FileNotFoundError:
            data = []

        data.append(data_json)

        with open(VACANCIES_PATH, "w") as file:
            json.dump(data_json, file, indent=7, ensure_ascii=False)

    def get_data(self):
        with open(VACANCIES_PATH, encoding="utf-8") as file:
            data = json.load(file)
            vacancies = []
            for vacancy in data:
                vacancies.append(Vacancy(
                    name=vacancy.get("name"),
                    alternate_url=vacancy.get("alternate_url"),
                    salary_from=vacancy.get("salary").get("from") if vacancy.get("salary") else "Нет информации",
                    salary_to=vacancy.get("salary").get("to") if vacancy.get("salary") else "Нет информации",
                    area_name=vacancy.get("area").get("name"),
                    requirement=vacancy.get("snippet").get("requirement"),
                    responsibility=vacancy.get("snippet").get("responsibility")
                ))
            return vacancies

    def del_data(self, data_json):
        del data_json


if __name__ == "__main__":
    saver = JSONSaver()
    hh = HeadHunterAPI("Курьер", 5)
    saver.write_data(hh.get_filter_vacancies("Курьер", 5))