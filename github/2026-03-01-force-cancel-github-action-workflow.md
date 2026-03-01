# Force cancelling a github action workflow

Force cancel a github actions workflow using the `gh` cli command.

`gh api repos/owner/repo_name/actions/runs/<id>/force-cancel -X POST`