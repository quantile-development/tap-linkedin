"""Stream type classes for tap-linkedin."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_linkedin.client import LinkedinStream


class FollowersStream(LinkedinStream):
    """Define custom stream."""
    name = "followers"
    path = "/organizationalEntityFollowerStatistics"
    replication_key = "date"

    schema = th.PropertiesList(
        th.Property("date", th.DateTimeType()),
        th.Property("organicFollowerGain", th.IntegerType()),
        th.Property("paidFollowerGain", th.IntegerType()),
    ).to_dict()

    @property
    def default_params(self):
        """Default parameters for the follower stream"""

        return {
            "q": "organizationalEntity",
            "organizationalEntity": f"urn:li:organization:{self.config['company_id']}",
            "timeIntervals.timeGranularityType": "DAY",
            "timeIntervals.timeRange.start": 1615420800000,
            "timeIntervals.timeRange.end": 1627730899113,
        }


class GroupsStream(LinkedinStream):
    """Define custom stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
