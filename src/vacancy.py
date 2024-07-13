class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.area_name = area_name
        self.requirement = requirement
        self.responsibility = responsibility

    def __str__(self):
        return (f"Наименование вакансии: {self.name},\n"
                f"Ссылка на вакансию: {self.alternate_url},\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to},\n"
                f"Место работы: {self.area_name},\n"
                f"Краткое описание: {self.requirement},\n"
                f"{self.responsibility}\n")

    def __lt__(self, other):

        if isinstance(self and other, int):
            return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)

    @staticmethod
    def vacancies_lst(vacancy_lst):
        """ Метод возвращает вакацнию в виде списка """

        return Vacancy(
            vacancy_lst["name"],
            vacancy_lst["alternate_url"],
            vacancy_lst["salary"]["from"] if vacancy_lst["salary"] else "Нет информации",
            vacancy_lst["salary"]["to"] if vacancy_lst["salary"] else "Нет информации",
            vacancy_lst["area"]["name"],
            vacancy_lst["snippet"]["requirement"],
            vacancy_lst["snippet"]["responsibility"],
        )

    @staticmethod
    def vacancies_dict(vacancy_dict):
        """ Метод возвращает вакацнию в виде словаря """

        return {
            vacancy_dict.get("name"),
            vacancy_dict.get("alternate_url"),
            vacancy_dict.get("salary").get("from") if vacancy_dict.get("salary") else "Нет информации",
            vacancy_dict.get("salary").get("to") if vacancy_dict.get("salary") else "Нет информации",
            vacancy_dict.get("area").get("name"),
            vacancy_dict.get("snippet").get("requirement"),
            vacancy_dict.get("snippet").get("responsibility"),
        }