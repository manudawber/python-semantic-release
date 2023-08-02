Workflow file: [semantic_release.yaml](semantic_release.yaml)

## Description

Uses `python-semantic-release` to automate a number of release-related tasks including:

- bumping the version number following the semantic versioning specification
- creating a GitHub release using the latest version number
- generating a changelog based on commit messages since the last release that use conventional commits

This should be used in conjunction with the `amannn/action-semantic-pull-request` actions to ensure PR commits appear as conventional commits.

Default configurations are stored in [setup.cfg](../../setup.cfg) under the `[semantic_release]' section.

## Usage

In the calling repo's root directory, ensure a `pyproject.toml` exists in that contains configuration for `python-semantic-release`, e.g.:

```toml
[tool.semantic_release]
# Releases
branch = "main"
version_variable = "src/parsely/__init__.py:__version__"
version_source = "tag"
# Commits
commit_version_number = true
commit_subject = "Release v{version}"
# Distributions
upload_to_pypi = false
upload_to_repository = false
upload_to_release = false
```

Then add the following job to a deployment workflow, i.e. a workflow that's run when changes are pushed to a release branch:

```yaml
name: Deploy
on:
  push:
    branches:
      - main
    paths-ignore:
      - src/parsely/__init__.py
      - CHANGELOG.md
jobs:
  release:
    uses: h2gopower/github-actions/.github/workflows/semantic_release.yml@v1
    with:
      branch: main
    secrets:
      release_token: ${{ secrets.HYBB8_PAT_READONLY }}
```
