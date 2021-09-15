from sqlalchemy import Column, String, Integer, ForeignKey

from ..base import Base


class UserFavoriteFilm(Base):
    __tablename__ = "user_favorite_films"

    user_login = Column(String(20), ForeignKey("users.login", ondelete="CASCADE"), primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id", ondelete="Cascade"), primary_key=True)
