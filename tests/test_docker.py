import subprocess
from sysconfig import get_python_version

import pytest


@pytest.mark.parametrize("dockerfile", ["tests/test-alpine.Dockerfile", "tests/test-debian.Dockerfile"])
def test_main(dockerfile):
    subprocess.check_call(["docker", "build", ".", "-f", dockerfile, "--build-arg", f"PYTHON={get_python_version()}"])
