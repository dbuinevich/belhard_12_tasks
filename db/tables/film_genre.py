from sqlalchemy import Column, String, Integer, ForeignKey

from ..base import Base


class FilmGenre(Base):
    __tablename__ = "films_genres"

    film_id = Column(Integer, ForeignKey("films.id", ondelete="Cascade"), primary_key=True)
    film_genre_id = Column(String(20), ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
