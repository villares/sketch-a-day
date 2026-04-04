#! /home/villares/thonny-env/bin/python

from dreamhost_deploy import deploy, OVERWRITE_HTML, SKIP_IMAGES, OVERWRITE_ASSETS

deploy(
    repo_keys=["sketch-a-day"],
    newer_than=1,
    overwrite_html=OVERWRITE_HTML,
    overwrite_assets=True,
)