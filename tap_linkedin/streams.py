"""Stream type classes for tap-linkedin."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_linkedin.client import LinkedinStream


class FollowersStream(LinkedinStream):
    """Follower statistics of the defined company."""
    name = "followers"
    path = "/v2/organizationalEntityFollowerStatistics"
    replication_key = "date"
    primary_keys = ["date"]

    schema = th.PropertiesList(
        th.Property("followerGains", th.ObjectType(
            th.Property("organicFollowerGain", th.IntegerType),
            th.Property("paidFollowerGain", th.IntegerType)
        )),
        th.Property("organizationalEntity", th.StringType),
        th.Property("date", th.DateTimeType)
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


class PageStream(LinkedinStream):
    """Statistics of the company page."""
    name = "page"
    path = "/v2/organizationPageStatistics"
    replication_key = "date"
    primary_keys = ["date"]

    schema = th.PropertiesList(
        th.Property("totalPageStatistics", th.ObjectType(
            th.Property("clicks", th.ObjectType(
                th.Property("mobileCustomButtonClickCounts", th.ArrayType(
                    th.ObjectType(
                        th.Property("customButtonType", th.StringType),
                        th.Property("clicks", th.IntegerType))
                    )
                ),
                th.Property("desktopCustomButtonClickCounts", th.ArrayType(
                    th.ObjectType(
                        th.Property("customButtonType", th.StringType),
                        th.Property("clicks", th.IntegerType))
                    )
                ),
            ))
        )),
        th.Property("views", th.ObjectType(
            th.Property("allDesktopPageViews", th.ObjectType(
                th.Property("pageViews", th.IntegerType),
                th.Property("uniquePageViews", th.IntegerType)
            )),
            th.Property("allMobilePageViews", th.ObjectType(
                th.Property("pageViews", th.IntegerType),
                th.Property("uniquePageViews", th.IntegerType)
            )),
            th.Property("allPageViews", th.ObjectType(
                th.Property("pageViews", th.IntegerType),
                th.Property("uniquePageViews", th.IntegerType)
            )),
        )),
        th.Property("organization", th.StringType),
        th.Property("date", th.DateTimeType)
    ).to_dict()

    @property
    def default_params(self):
        """Default parameters for the page stream"""

        return {
            "q": "organization",
            "organization": f"urn:li:organization:{self.config['company_id']}",
            "timeIntervals.timeGranularityType": "DAY",
            "timeIntervals.timeRange.start": 1615420800000,
            "timeIntervals.timeRange.end": 1627730899113,
        }

class PostsStream(LinkedinStream):
    """Statistics of the posts made by the company"""
    name = "posts"
    path = "/v2/organizationalEntityShareStatistics"
    replication_key = "date"
    primary_keys = ["date"]

    schema = th.PropertiesList(
        th.Property("totalShareStatistics", th.ObjectType(
            th.Property("shareCount", th.IntegerType),
            th.Property("likeCount", th.IntegerType),
            th.Property("engagement", th.NumberType),
            th.Property("clickCount", th.IntegerType),
            th.Property("impressionCount", th.IntegerType),
            th.Property("commentCount", th.IntegerType),
        )),
        th.Property("organizationalEntity", th.StringType),
        th.Property("date", th.DateTimeType)
    ).to_dict()

    @property
    def default_params(self):
        """Default parameters for the page stream"""

        return {
            "q": "organizationalEntity",
            "organizationalEntity": f"urn:li:organization:{self.config['company_id']}",
            "timeIntervals.timeGranularityType": "DAY",
            "timeIntervals.timeRange.start": 1615420800000,
            "timeIntervals.timeRange.end": 1627730899113,
        }
