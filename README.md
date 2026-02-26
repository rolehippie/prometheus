# prometheus

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/prometheus)
[![General Workflow](https://github.com/rolehippie/prometheus/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/prometheus/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/prometheus/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/prometheus/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/prometheus/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/prometheus/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/prometheus)](https://github.com/rolehippie/prometheus/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.prometheus-blue)](https://galaxy.ansible.com/rolehippie/prometheus)

Ansible role to install and configure Prometheus.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [prometheus_alertmanagers](#prometheus_alertmanagers)
  - [prometheus_arch](#prometheus_arch)
  - [prometheus_cpu_shares](#prometheus_cpu_shares)
  - [prometheus_default_folders](#prometheus_default_folders)
  - [prometheus_default_labels](#prometheus_default_labels)
  - [prometheus_default_publish](#prometheus_default_publish)
  - [prometheus_default_rules](#prometheus_default_rules)
  - [prometheus_default_volumes](#prometheus_default_volumes)
  - [prometheus_domain](#prometheus_domain)
  - [prometheus_download](#prometheus_download)
  - [prometheus_enable_remote_write_receiver](#prometheus_enable_remote_write_receiver)
  - [prometheus_evaluation_interval](#prometheus_evaluation_interval)
  - [prometheus_extra_folders](#prometheus_extra_folders)
  - [prometheus_extra_labels](#prometheus_extra_labels)
  - [prometheus_extra_publish](#prometheus_extra_publish)
  - [prometheus_extra_rules](#prometheus_extra_rules)
  - [prometheus_extra_volumes](#prometheus_extra_volumes)
  - [prometheus_image](#prometheus_image)
  - [prometheus_installation](#prometheus_installation)
  - [prometheus_listen_address](#prometheus_listen_address)
  - [prometheus_memory_limit](#prometheus_memory_limit)
  - [prometheus_memory_soft_limit](#prometheus_memory_soft_limit)
  - [prometheus_memory_swap](#prometheus_memory_swap)
  - [prometheus_network](#prometheus_network)
  - [prometheus_number_of_cpus](#prometheus_number_of_cpus)
  - [prometheus_oauth2_access_logging](#prometheus_oauth2_access_logging)
  - [prometheus_oauth2_allowed_groups](#prometheus_oauth2_allowed_groups)
  - [prometheus_oauth2_arch](#prometheus_oauth2_arch)
  - [prometheus_oauth2_client_id](#prometheus_oauth2_client_id)
  - [prometheus_oauth2_client_secret](#prometheus_oauth2_client_secret)
  - [prometheus_oauth2_cookie_secret](#prometheus_oauth2_cookie_secret)
  - [prometheus_oauth2_cpu_shares](#prometheus_oauth2_cpu_shares)
  - [prometheus_oauth2_default_labels](#prometheus_oauth2_default_labels)
  - [prometheus_oauth2_default_publish](#prometheus_oauth2_default_publish)
  - [prometheus_oauth2_download](#prometheus_oauth2_download)
  - [prometheus_oauth2_enabled](#prometheus_oauth2_enabled)
  - [prometheus_oauth2_extra_labels](#prometheus_oauth2_extra_labels)
  - [prometheus_oauth2_extra_publish](#prometheus_oauth2_extra_publish)
  - [prometheus_oauth2_image](#prometheus_oauth2_image)
  - [prometheus_oauth2_keycloak_url](#prometheus_oauth2_keycloak_url)
  - [prometheus_oauth2_listen_address](#prometheus_oauth2_listen_address)
  - [prometheus_oauth2_memory_limit](#prometheus_oauth2_memory_limit)
  - [prometheus_oauth2_memory_soft_limit](#prometheus_oauth2_memory_soft_limit)
  - [prometheus_oauth2_memory_swap](#prometheus_oauth2_memory_swap)
  - [prometheus_oauth2_network](#prometheus_oauth2_network)
  - [prometheus_oauth2_number_of_cpus](#prometheus_oauth2_number_of_cpus)
  - [prometheus_oauth2_provider](#prometheus_oauth2_provider)
  - [prometheus_oauth2_pull_image](#prometheus_oauth2_pull_image)
  - [prometheus_oauth2_request_logging](#prometheus_oauth2_request_logging)
  - [prometheus_oauth2_static_groups](#prometheus_oauth2_static_groups)
  - [prometheus_oauth2_static_users](#prometheus_oauth2_static_users)
  - [prometheus_oauth2_upstream](#prometheus_oauth2_upstream)
  - [prometheus_oauth2_version](#prometheus_oauth2_version)
  - [prometheus_pull_image](#prometheus_pull_image)
  - [prometheus_rule_files](#prometheus_rule_files)
  - [prometheus_scrape_configs](#prometheus_scrape_configs)
  - [prometheus_scrape_interval](#prometheus_scrape_interval)
  - [prometheus_tsdb_retention_size](#prometheus_tsdb_retention_size)
  - [prometheus_tsdb_retention_time](#prometheus_tsdb_retention_time)
  - [prometheus_version](#prometheus_version)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### prometheus_alertmanagers

List of alertmanager configuration

#### Default value

```YAML
prometheus_alertmanagers: []
```

#### Example usage

```YAML
prometheus_alertmanagers:
  - scheme: http
    static_configs:
      - targets:
          - loclhost:9093
```

### prometheus_arch

Target system architecture of the binary

#### Default value

```YAML
prometheus_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' or ansible_architecture
  == 'arm64' else 'amd64' }}"
```

### prometheus_cpu_shares

CPU shares with Docker deployment

#### Default value

```YAML
prometheus_cpu_shares:
```

#### Example usage

```YAML
prometheus_cpu_shares: '512'
```

### prometheus_default_folders

List of default folders to create

#### Default value

```YAML
prometheus_default_folders:
  - /etc/prometheus
  - /etc/prometheus/rules
  - /var/lib/prometheus
```

### prometheus_default_labels

List of default labels to assign to docker

#### Default value

```YAML
prometheus_default_labels: []
```

### prometheus_default_publish

List of default port publishing for docker

#### Default value

```YAML
prometheus_default_publish: []
```

#### Example usage

```YAML
prometheus_default_publish:
  - 127.0.0.1:9090:9090
```

### prometheus_default_rules

List of default rule file definitions

#### Default value

```YAML
prometheus_default_rules: []
```

#### Example usage

```YAML
prometheus_default_rules:
  - name: example
    content:
      groups:
        - name: example
          rules:
            - alert: ...
              expr: ...
              for: 5m
  - name: example-from-url
    url: http://example.com/example.yml
  - name: example-from-template
    src: path/to/template.j2
  - name: example-to-remove
    state: absent
```

### prometheus_default_volumes

List of default volumes to mount for docker

#### Default value

```YAML
prometheus_default_volumes:
  - /var/lib/prometheus:/var/lib/prometheus
  - /etc/prometheus/rules:/etc/prometheus/rules
```

### prometheus_domain

Domain for external access

#### Default value

```YAML
prometheus_domain:
```

#### Example usage

```YAML
prometheus_domain: https://prometheus.example.com
```

### prometheus_download

URL to the archive of the release to install

#### Default value

```YAML
prometheus_download: 
  https://github.com/prometheus/prometheus/releases/download/v{{ 
  prometheus_version }}/prometheus-{{ prometheus_version }}.linux-{{ 
  prometheus_arch }}.tar.gz
```

### prometheus_enable_remote_write_receiver

Enable remote-write receiver in Prometheus

#### Default value

```YAML
prometheus_enable_remote_write_receiver: false
```

### prometheus_evaluation_interval

Global default evaluation interval

#### Default value

```YAML
prometheus_evaluation_interval: 15s
```

### prometheus_extra_folders

List of extra folders to create

#### Default value

```YAML
prometheus_extra_folders: []
```

#### Example usage

```YAML
prometheus_extra_folders:
  - /path/to/host/folder1
  - /path/to/host/folder2
  - /path/to/host/folder3
```

### prometheus_extra_labels

List of extra labels to assign to docker

#### Default value

```YAML
prometheus_extra_labels: []
```

### prometheus_extra_publish

List of extra port publishing for docker

#### Default value

```YAML
prometheus_extra_publish: []
```

#### Example usage

```YAML
prometheus_extra_publish:
  - 127.0.0.1:9000:9000
```

### prometheus_extra_rules

List of extra rule file definitions

#### Default value

```YAML
prometheus_extra_rules: []
```

#### Example usage

```YAML
prometheus_extra_rules:
  - name: example
    content:
      groups:
        - name: example
          rules:
            - alert: ...
              expr: ...
              for: 5m
  - name: example-from-url
    url: http://example.com/example.yml
  - name: example-from-template
    src: path/to/template.j2
  - name: example-to-remove
    state: absent
```

### prometheus_extra_volumes

List of extra volumes to mount for docker

#### Default value

```YAML
prometheus_extra_volumes: []
```

#### Example usage

```YAML
prometheus_extra_volumes:
  - /path/to/host/folder1:/path/within/container1
  - /path/to/host/folder2:/path/within/container2
  - /path/to/host/folder3:/path/within/container3
```

### prometheus_image

Docker image to use for deployment on OAuth2 Proxy

#### Default value

```YAML
prometheus_image: quay.io/prometheus/prometheus:v{{ prometheus_version }}
```

### prometheus_installation

Select installation method, could be native or docker

#### Default value

```YAML
prometheus_installation: native
```

### prometheus_listen_address

Listen address for the prometheus

#### Default value

```YAML
prometheus_listen_address: 0.0.0.0:9090
```

### prometheus_memory_limit

Memory limit with Docker deployment

#### Default value

```YAML
prometheus_memory_limit:
```

#### Example usage

```YAML
prometheus_memory_limit: 1024m
```

### prometheus_memory_soft_limit

Soft memory limit with Docker deployment

#### Default value

```YAML
prometheus_memory_soft_limit:
```

#### Example usage

```YAML
prometheus_memory_soft_limit: 512m
```

### prometheus_memory_swap

Swap usage with Docker deployment

#### Default value

```YAML
prometheus_memory_swap:
```

#### Example usage

```YAML
prometheus_memory_swap: 2048m
```

### prometheus_network

Optional docker network to attach on OAuth2 Proxy

#### Default value

```YAML
prometheus_network:
```

### prometheus_number_of_cpus

Number of CPUs with Docker deployment

#### Default value

```YAML
prometheus_number_of_cpus:
```

#### Example usage

```YAML
prometheus_number_of_cpus: '1.0'
```

### prometheus_oauth2_access_logging

Enable access logging for OAuth2 proxy

#### Default value

```YAML
prometheus_oauth2_access_logging: false
```

### prometheus_oauth2_allowed_groups

List of groups to allow access

#### Default value

```YAML
prometheus_oauth2_allowed_groups: []
```

#### Example usage

```YAML
prometheus_oauth2_allowed_groups:
  - /Group1
  - /Group2
  - /Group3
```

### prometheus_oauth2_arch

Target system architecture of the binary

#### Default value

```YAML
prometheus_oauth2_arch: '{{ prometheus_arch }}'
```

### prometheus_oauth2_client_id

Client ID for OAuth2 authentication

#### Default value

```YAML
prometheus_oauth2_client_id:
```

### prometheus_oauth2_client_secret

Client secret for OAuth2 authentication

#### Default value

```YAML
prometheus_oauth2_client_secret:
```

### prometheus_oauth2_cookie_secret

Cookie secret used by OAuth2 proxy

#### Default value

```YAML
prometheus_oauth2_cookie_secret:
```

### prometheus_oauth2_cpu_shares

CPU shares with Docker deployment

#### Default value

```YAML
prometheus_oauth2_cpu_shares:
```

#### Example usage

```YAML
prometheus_oauth2_cpu_shares: '512'
```

### prometheus_oauth2_default_labels

List of default labels to assign to docker on OAuth2 Proxy

#### Default value

```YAML
prometheus_oauth2_default_labels: []
```

### prometheus_oauth2_default_publish

List of default port publishing for docker on OAuth2 Proxy

#### Default value

```YAML
prometheus_oauth2_default_publish: []
```

#### Example usage

```YAML
prometheus_oauth2_default_publish:
  - 127.0.0.1:9089:9089
```

### prometheus_oauth2_download

#### Default value

```YAML
prometheus_oauth2_download: 
  https://github.com/oauth2-proxy/oauth2-proxy/releases/download/v{{ 
  prometheus_oauth2_version }}/oauth2-proxy-v{{ prometheus_oauth2_version 
  }}.linux-{{ prometheus_oauth2_arch }}.tar.gz
```

### prometheus_oauth2_enabled

URL of the OAuth2 Proxy to download

#### Default value

```YAML
prometheus_oauth2_enabled: false
```

### prometheus_oauth2_extra_labels

List of extra labels to assign to docker on OAuth2 Proxy

#### Default value

```YAML
prometheus_oauth2_extra_labels: []
```

### prometheus_oauth2_extra_publish

List of extra port publishing for docker on OAuth2 Proxy

#### Default value

```YAML
prometheus_oauth2_extra_publish: []
```

#### Example usage

```YAML
prometheus_oauth2_extra_publish:
  - 127.0.0.1:9089:9089
```

### prometheus_oauth2_image

#### Default value

```YAML
prometheus_oauth2_image: quay.io/oauth2-proxy/oauth2-proxy:v{{ 
  prometheus_oauth2_version }}
```

### prometheus_oauth2_keycloak_url

URL of the Keycloak realm

#### Default value

```YAML
prometheus_oauth2_keycloak_url:
```

### prometheus_oauth2_listen_address

Listem address for the OAuth2 proxy

#### Default value

```YAML
prometheus_oauth2_listen_address: 0.0.0.0:9089
```

### prometheus_oauth2_memory_limit

Memory limit with Docker deployment

#### Default value

```YAML
prometheus_oauth2_memory_limit:
```

#### Example usage

```YAML
prometheus_oauth2_memory_limit: 1024m
```

### prometheus_oauth2_memory_soft_limit

Soft memory limit with Docker deployment

#### Default value

```YAML
prometheus_oauth2_memory_soft_limit:
```

#### Example usage

```YAML
prometheus_oauth2_memory_soft_limit: 512m
```

### prometheus_oauth2_memory_swap

Swap usage with Docker deployment

#### Default value

```YAML
prometheus_oauth2_memory_swap:
```

#### Example usage

```YAML
prometheus_oauth2_memory_swap: 2048m
```

### prometheus_oauth2_network

#### Default value

```YAML
prometheus_oauth2_network: '{{ prometheus_network }}'
```

### prometheus_oauth2_number_of_cpus

Number of CPUs with Docker deployment

#### Default value

```YAML
prometheus_oauth2_number_of_cpus:
```

#### Example usage

```YAML
prometheus_oauth2_number_of_cpus: '1.5'
```

### prometheus_oauth2_provider

Provider for OAuth2 authentication

#### Default value

```YAML
prometheus_oauth2_provider: keycloak
```

### prometheus_oauth2_pull_image

#### Default value

```YAML
prometheus_oauth2_pull_image: true
```

### prometheus_oauth2_request_logging

Enable request logging for OAuth2 proxy

#### Default value

```YAML
prometheus_oauth2_request_logging: false
```

### prometheus_oauth2_static_groups

List of groups assigned to static users

#### Default value

```YAML
prometheus_oauth2_static_groups: []
```

### prometheus_oauth2_static_users

List of users to allow access

#### Default value

```YAML
prometheus_oauth2_static_users: []
```

#### Example usage

```YAML
prometheus_oauth2_static_users:
  - username: username1
    password: p455w0rd
  - username: username2
    password: p455w0rd
  - username: username3
    password: p455w0rd
```

### prometheus_oauth2_upstream

Upstream target for the OAuth2 proxy

#### Default value

```YAML
prometheus_oauth2_upstream: http://{{ prometheus_listen_address if 
  prometheus_installation == 'native' else 'prometheus:9090' }}
```

### prometheus_oauth2_version

Version of the OAuth2 Proxy to download

#### Default value

```YAML
prometheus_oauth2_version: 7.14.2
```

### prometheus_pull_image

Pull image as part of the tasks

#### Default value

```YAML
prometheus_pull_image: true
```

### prometheus_rule_files

List of paths to read rule files from

#### Default value

```YAML
prometheus_rule_files:
  - /etc/prometheus/rules/*.yml
```

### prometheus_scrape_configs

List of scrape configuration

#### Default value

```YAML
prometheus_scrape_configs: []
```

#### Example usage

```YAML
prometheus_scrape_configs:
  - job_name: prometheus
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets:
          - localhost:9090
```

### prometheus_scrape_interval

Global default scrape interval

#### Default value

```YAML
prometheus_scrape_interval: 15s
```

### prometheus_tsdb_retention_size

Retention size to define the maximum size of the data

#### Default value

```YAML
prometheus_tsdb_retention_size:
```

### prometheus_tsdb_retention_time

Retention time to define the maximum age of the data

#### Default value

```YAML
prometheus_tsdb_retention_time: 30d
```

### prometheus_version

Version of the release to install

#### Default value

```YAML
prometheus_version: 3.10.0
```

## Discovered Tags

**_oauth2_**

**_prometheus_**

## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)
- [ansible.posix](https://github.com/ansible-collections/ansible.posix)
- [community.docker](https://github.com/ansible-collections/community.docker)
- [community.general](https://github.com/ansible-collections/community.general)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
