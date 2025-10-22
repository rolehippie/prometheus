import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_running_and_enabled(host):
    svc = host.service("prometheus")
    assert svc.is_running
    assert svc.is_enabled

def test_docker_is_enabled(host):
    docker = host.docker("prometheus")
    assert docker.is_running
