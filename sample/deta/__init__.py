"""
Deta Base & Drive API wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Asynchronous Python wrapper for Deta Base & Drive HTTP API.

:copyright: (c) 2022-present Sougata Jana
:license: MIT, see LICENSE for more details.

"""

__title__ = "deta"
__license__ = "MIT"
__copyright__ = "Copyright 2022-present Sougata Jana"
__author__ = "Sougata Jana"
__version__ = "0.0.7a"

from .deta import Deta, Base, Drive
from .errors import (
    Unauthorized,
    NotFound,
    BadRequest,
    PayloadTooLarge,
    KeyConflict,
    DetaUnknownError,
    IncompleteUpload
)
from .utils import Record, Updater, Query
