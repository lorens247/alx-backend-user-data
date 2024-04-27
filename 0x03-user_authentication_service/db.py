#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database
        """
        try:
            user_to_add = User(email=email, hashed_password=hashed_password)
            self._session.add(user_to_add)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user_to_add = None
        return user_to_add

    def find_user_by(self, **kwargs) -> User:
        """Finds a user in the database based on the provided keyword arguments
        """
        filter_fields = []
        filter_values = []
        for filter_key, filter_value in kwargs.items():
            if hasattr(User, filter_key):
                filter_fields.append(getattr(User, filter_key))
                filter_values.append(filter_value)
            else:
                raise InvalidRequestError()
        query_result = self._session.query(User).filter(
            tuple_(*filter_fields).in_([tuple(filter_values)])
        ).first()

        if query_result is None:
            raise NoResultFound()
        return query_result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user in the database based on the provided user_id
        """
        user_to_update = self.find_user_by(id=user_id)

        if user_to_update is None:
            return

        update_data = {}
        for field, value in kwargs.items():
            if hasattr(User, field):
                update_data[getattr(User, field)] = value
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            update_data,
            synchronize_session=False,
        )
        self._session.commit()
