from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_choice():
    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))

    hh_api = HeadHunterAPI(keyword, per_page)
    from_hh = hh_api.get_filter_vacancies(keyword, per_page=per_page)
    sorted_vacancies = sorted(from_hh, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted_vacancies:
        print(i)

    json_write = JSONSaver()
    a = json_write.get_data()
    vacancy = Vacancy.vacancies_dict(a)
    json_write.write_data(vacancy)
    print("Данные записаны в json файл")