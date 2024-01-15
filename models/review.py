#!/usr/bin/python3
from models.base_model import BaseModel
"""Class that
represents
the review"""


class Review(BaseModel):

    """Initializing the reviewed class
    instance
    of basemodel class"""
    place_id = ''
    user_id = ''
    text = ''
