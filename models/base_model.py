#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import environ

Base = declarative_base()

s = "HBNB_TYPE_STORAGE"

class BaseModel:
    """A base class for all hbnb models"""

    if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
        id = Column(
            String(60),
            unique=True,
            nullable=False,
            primary_key=True,
            default=str(
                uuid.uuid4()))
        created_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow())
        updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        cs = "HBNB_TYPE_STORAGE"
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        elif cs not in environ.keys() or environ["HBNB_TYPE_STORAGE"] != "db":
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict.keys():
            del my_dict["_sa_instance_state"]
            models.storage.save()
        return my_dict

    def delete(self):
        models.storage.delete(self)
        models.storage.save()
