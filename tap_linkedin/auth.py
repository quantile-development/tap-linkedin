"""Linkedin Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator


class LinkedinAuthenticator(OAuthAuthenticator):
    """Authenticator class for Linkedin."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the Linkedin API."""
        # TODO: Define the request body needed for the API.
        return {
            'scope': self.oauth_scopes,
            'client_id': self.config["client_id"],
            'grant_type': 'code',
        }

    @classmethod
    def create_for_stream(cls, stream) -> "LinkedinAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="https://www.linkedin.com/oauth/v2/authorization",
            oauth_scopes="rw_organization_admin",
        )
