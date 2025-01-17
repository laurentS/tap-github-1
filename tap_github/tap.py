"""GitHub tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_github.streams import RepositoryStream, IssuesStream, IssueCommentsStream


class TapGitHub(Tap):
    """GitHub tap class."""

    name = "tap-github"

    config_jsonschema = th.PropertiesList(
        th.Property("user_agent", th.StringType),
        th.Property("metrics_log_level", th.StringType),
        th.Property("auth_token", th.StringType),
        th.Property(
            "searches",
            th.ArrayType(
                th.ObjectType(
                    th.Property("name", th.StringType, required=True),
                    th.Property("query", th.StringType, required=True),
                )
            ),
            required=True,
        ),
        th.Property("start_date", th.DateTimeType),
        th.Property("stream_maps", th.ObjectType()),
        th.Property("stream_map_config", th.ObjectType()),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            RepositoryStream(tap=self),
            IssuesStream(tap=self),
            IssueCommentsStream(tap=self),
        ]


# CLI Execution:

cli = TapGitHub.cli
