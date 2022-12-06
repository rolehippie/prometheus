# prometheus

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/prometheus) [![Testing Build](https://github.com/rolehippie/prometheus/workflows/testing/badge.svg)](https://github.com/rolehippie/prometheus/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/prometheus/workflows/readme/badge.svg)](https://github.com/rolehippie/prometheus/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/prometheus/workflows/galaxy/badge.svg)](https://github.com/rolehippie/prometheus/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/prometheus)](https://github.com/rolehippie/prometheus/blob/master/LICENSE)

Ansible role to install and configure Prometheus.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [prometheus_alertmanagers](#prometheus_alertmanagers)
  - [prometheus_default_rules](#prometheus_default_rules)
  - [prometheus_domain](#prometheus_domain)
  - [prometheus_download](#prometheus_download)
  - [prometheus_evaluation_interval](#prometheus_evaluation_interval)
  - [prometheus_extra_rules](#prometheus_extra_rules)
  - [prometheus_listen_address](#prometheus_listen_address)
  - [prometheus_oauth2_allowed_groups](#prometheus_oauth2_allowed_groups)
  - [prometheus_oauth2_client_id](#prometheus_oauth2_client_id)
  - [prometheus_oauth2_client_secret](#prometheus_oauth2_client_secret)
  - [prometheus_oauth2_cookie_secret](#prometheus_oauth2_cookie_secret)
  - [prometheus_oauth2_download](#prometheus_oauth2_download)
  - [prometheus_oauth2_enabled](#prometheus_oauth2_enabled)
  - [prometheus_oauth2_keycloak_url](#prometheus_oauth2_keycloak_url)
  - [prometheus_oauth2_listen_address](#prometheus_oauth2_listen_address)
  - [prometheus_oauth2_provider](#prometheus_oauth2_provider)
  - [prometheus_oauth2_static_groups](#prometheus_oauth2_static_groups)
  - [prometheus_oauth2_static_users](#prometheus_oauth2_static_users)
  - [prometheus_oauth2_upstream](#prometheus_oauth2_upstream)
  - [prometheus_oauth2_version](#prometheus_oauth2_version)
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
prometheus_download: https://github.com/prometheus/prometheus/releases/download/v{{
  prometheus_version }}/prometheus-{{ prometheus_version }}.linux-amd64.tar.gz
```

### prometheus_evaluation_interval

Global default evaluation interval

#### Default value

```YAML
prometheus_evaluation_interval: 15s
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

### prometheus_listen_address

Listen address for the prometheus

#### Default value

```YAML
prometheus_listen_address: 0.0.0.0:9090
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

### prometheus_oauth2_download

#### Default value

```YAML
prometheus_oauth2_download: https://github.com/oauth2-proxy/oauth2-proxy/releases/download/v{{
  prometheus_oauth2_version }}/oauth2-proxy-v{{ prometheus_oauth2_version }}.linux-amd64.tar.gz
```

### prometheus_oauth2_enabled

URL of the OAuth2 Proxy to download

#### Default value

```YAML
prometheus_oauth2_enabled: false
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

### prometheus_oauth2_provider

Provider for OAuth2 authentication

#### Default value

```YAML
prometheus_oauth2_provider: keycloak
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
prometheus_oauth2_upstream: http://{{ prometheus_listen_address }}
```

### prometheus_oauth2_version

Version of the OAuth2 Proxy to download

#### Default value

```YAML
prometheus_oauth2_version: 7.4.0
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
prometheus_version: 2.40.5
```

## Discovered Tags

**_oauth2_**

**_prometheus_**


## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
