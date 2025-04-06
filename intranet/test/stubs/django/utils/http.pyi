# Stubs for django.utils.http (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from binascii import Error as BinasciiError

ETAG_MATCH = ...  # type: Any
MONTHS = ...  # type: Any
RFC1123_DATE = ...  # type: Any
RFC850_DATE = ...  # type: Any
ASCTIME_DATE = ...  # type: Any
RFC3986_GENDELIMS = ...  # type: Any
RFC3986_SUBDELIMS = ...  # type: Any
PROTOCOL_TO_PORT = ...  # type: Any

def urlquote(url, safe=''): ...

def urlquote_plus(url, safe=''): ...

def urlunquote(quoted_url): ...

def urlunquote_plus(quoted_url): ...

def urlencode(query, doseq=0): ...
def cookie_date(epoch_seconds=None): ...
def http_date(epoch_seconds=None): ...
def parse_http_date(date): ...
def parse_http_date_safe(date): ...
def base36_to_int(s): ...
def int_to_base36(i): ...
def urlsafe_base64_encode(s): ...
def urlsafe_base64_decode(s): ...
def parse_etags(etag_str): ...
def quote_etag(etag): ...
def unquote_etag(etag): ...
def is_same_domain(host, pattern): ...
def is_safe_url(url, host=None): ...
