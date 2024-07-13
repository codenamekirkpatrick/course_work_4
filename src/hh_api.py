import requests

from src.get_vacancies import GetVacanciesAPI
from src.vacancy import Vacancy


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self, keyword, per_page):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": keyword, "per_page": per_page}
        self.vacancies = []

    def get_response(self, keyword, per_page):
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword, per_page):
        return self.get_response(keyword, per_page).json()["items"]

    def get_filter_vacancies(self, keyword, per_page):
        filter_vacancies = []
        vacancies = self.get_vacancies(keyword, per_page)
        for vacancy in vacancies:
            # filter_vacancies.append({
            #     "name": vacancy.get("name"),
            #     "alternate_url": vacancy.get("alternate_url"),
            #     "salary_from": vacancy.get("salary").get("from") if vacancy.get("salary") else "Нет информации",
            #     "salary_to": vacancy.get("salary").get("to") if vacancy.get("salary") else "Нет информации",
            #     "area_name": vacancy.get("area").get("name"),
            #     "requirement": vacancy.get("snippet").get("requirement"),
            #     "responsibility": vacancy.get("snippet").get("responsibility")
            # })
            filter_vacancies.append(Vacancy.vacancies_lst(vacancy))
        return filter_vacancies