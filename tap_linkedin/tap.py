"""Linkedin tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_linkedin.streams import (
    FollowersStream,
    PageStream,
    PostsStream
)

STREAM_TYPES = [
    FollowersStream,
    PageStream,
    PostsStream
]


class TapLinkedin(Tap):
    """Linkedin tap class."""
    name = "tap-linkedin"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("access_token", th.StringType, required=True),
        th.Property("company_id", th.IntegerType, required=True),
        th.Property("start_date", th.DateTimeType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
