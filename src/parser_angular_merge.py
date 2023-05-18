from semantic_release.history import angular_parser
from semantic_release.history.parser_helpers import ParsedCommit


def parse_commit_message(message: str) -> ParsedCommit:
    """Extends the `angular_parser` function to work with merge commits.

    Merge commits are not processed by `angular_parser` as they don't adhere to the conventional commit format. Given
    that we enforce pull request titles to follow this format, this custom parser is required to ensure these PR titles
    are usable by `python-semantic-release`.

    If a commit message starts with "Merge pull request" then it's considered a merge commit and the last line of the
    commit message will be extracted (this should be the original PR title) and sent to `angular_parser`.

    Example merge commit message:

    ```
    Merge pull request #553 from h2gopower/feature/shared-action-vulnerability-scanning

    feat: create shared action for vulnerability scanning
    ```

    Args:
        message: A git commit message.

    Returns:
        A `ParsedCommit` object containing semantic release versioning and changelog information.
    """
    message = message.strip()  # remove leading/trailing blank lines
    if message.startswith("Merge pull request"):
        message = message.splitlines()[-1]
    message = message.strip()  # remove leading/trailing whitespace
    return angular_parser(message)
