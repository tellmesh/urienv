from __future__ import annotations

from pathlib import Path

from uri_control.edge.manifest import register_manifest_file


def register(runtime):
    register_manifest_file(runtime, Path(__file__).with_name("manifest.yaml"))
