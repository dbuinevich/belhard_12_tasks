import datetime

from db import session_scope, tables

with session_scope() as session:
    # result = session.query(tables.UserType).all()
    # result = session.query(tables.UserType).order_by(desc(tables.UserType.id)).all()
    # result = session.query(tables.UserType).order_by(desc(tables.UserType.id)).limit(1).all()
    # result = (
    #     session.query(tables.User)
    #     .join(tables.UserType, tables.User.user_type_id == tables.UserType.id)
    #     .order_by(desc(tables.UserType.id)).limit(1).all()
    # )

    # person = tables.Person(name="Vasya", surname="Pupkin", birth_date=datetime.datetime.now())
    # session.add(person)
    # session.commit()
    # session.refresh(person)

    # person = session.query(tables.Person).filter_by(id=1).one()
    #
    # user = tables.User(login="loginjsnsjk", password="passjnbkjb")
    # user.user_type_id = "ADMIN"
    # user.person = person
    #
    # session.add(user)
    # session.commit()

    # result = (
    #     session.query(tables.Person)
    #         .join(tables.User)
    #         .join(tables.UserType)
    #         .filter(tables.UserType.id == "ADMIN")
    #         .all()
    # )
    # неправильно тут

    # person = session.query(tables.Person).filter_by(id=1).one()    #blyaaaaaa
    #
    # user = session.query(tables.User).first()
    film = tables.Film()
    film.duration = 123
    film.name = "knlknl"
    film.release_date = datetime.datetime.now()
    film.rating = 4.5
    film.director_id = 2
    session.add(film)
    session.commit()
    session.refresh(film)
    session.commit()

    film2 = tables.Film()
    film2.duration = 321
    film2.name = "film2"
    film2.release_date = datetime.datetime.now()
    film2.rating = 4.5
    film2.director_id = 6
    session.add(film2)
    session.commit()
    session.refresh(film2)
    session.commit()

    # new_character = tables.Character(name="char", film_id=)

    # вставка

    person = tables.Person(
        surname="some_surname3",
        name="some_name3",
        birth_date=datetime.datetime.now()
    )
    session.add(person)
    session.commit()

    # Удаление

    some_person = session.query(tables.Person).filter_by(id=3).one()
    print(some_person)
    session.delete(some_person)
    session.commit()

    # Обновление

    new_user_id = session.query(tables.UserType).filter(tables.UserType.id == "ADMIN").one()
    new_user_id.name = "Администратор"
    session.commit()

    user = session.query(tables.User).filter_by(login="login3").one()
    user.password = "new_pass"
    session.commit()
    print(user.password)

    # Сортировка
    result = (
        session.query(tables.User)
        .join(tables.UserType, tables.User.user_type_id == tables.UserType.id)
        .filter(tables.UserType.name == "User").all()
    )

    result2 = session.query(tables.Genre).order_by(tables.Genre.id.desc()).all()

    result3 = (
        session.query(tables.Person)
        .join(tables.Film, tables.Person.id == tables.Film.director_id)
        .order_by(tables.Film.release_date.asc()).all()
    )

    print(result)
    print(result2)
    print(result3)
