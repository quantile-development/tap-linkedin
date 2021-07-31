"""REST client handling, including LinkedinStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from datetime import datetime

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class LinkedinStream(RESTStream):
    """Linkedin stream class."""

    url_base = "https://api.linkedin.com"
    default_params: Optional[dict] = None

    records_jsonpath = "$.elements[*]"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {
            'Authorization': f"Bearer {self.config['access_token']}",
        }
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # # TODO: If pagination is required, return a token which can be used to get the
        # #       next page. If this is the final page, return "None" to end the
        # #       pagination loop.
        # if self.next_page_token_jsonpath:
        #     all_matches = extract_jsonpath(
        #         self.next_page_token_jsonpath, response.json()
        #     )
        #     first_match = next(iter(all_matches), None)
        #     next_page_token = first_match
        # else:
        #     next_page_token = response.headers.get("X-Next-Page", None)

        # return next_page_token
        return None

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""

        # TODO: Set the start date of the request.
        return {**self.default_params}

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def parse_date(self, date_millis: int) -> str:
        # Parse milliseconds sinc epoch to a datetime object.
        date = datetime.fromtimestamp(date_millis / 1000)

        # Transform to iso format.
        return date.isoformat()

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # Parse the dates if they are present.
        if "timeRange" in row:
            row["date"] = self.parse_date(date_millis=row["timeRange"]["end"])

        return row
