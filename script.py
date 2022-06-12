import random

from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid, Subject


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2, 3]).update(
        points=5)
    return


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid.id).delete()
    return


def create_commendation(schoolkid, subject):
    commendations = (
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    )

    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
    ).order_by("-date").first()

    Commendation.objects.update_or_create(
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        defaults={"text": random.choice(commendations)}
    )
    return


def main():
    schoolkid_name = input("Введите ФИО ученика: ")
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено более одного совпадения, необходимо вводить ФИО полностью")
        return
    except Schoolkid.DoesNotExist:
        print("По введенным данным учеников не найдено")
        return

    subject = input("Введите предмет по которому необходима похвала: ")
    try:
        subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study).title
    except Subject.DoesNotExist:
        print("Предмет не найден")
        return

    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject)
    print(f"Скрипт успешно завершил работу, оценки 2 и 3 исправлены на 5,"
          f"жалобы удалены и добавлена похвала по предмету: {subject}")


if __name__ == '__main__':
    main()
