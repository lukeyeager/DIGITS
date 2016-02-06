# Copyright (c) 2016, NVIDIA CORPORATION.  All rights reserved.
from __future__ import absolute_import

from .adapter import db
from .inference import Inference
from .utils import WithRepr


class InferenceFile(db.Model, WithRepr):
    REPR_FIELDS = ['key', 'path']

    id = db.Column(db.Integer, primary_key=True)
    inference_id = db.Column(db.Integer,
                         db.ForeignKey('%s.id' % Inference.__tablename__),
                         nullable=False,
                         )
    inference = db.relationship(Inference.__name__,
                                backref=db.backref('files', lazy='dynamic'))
    key = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
