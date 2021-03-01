# prometheus

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/prometheus) [![Build Status](https://img.shields.io/drone/build/rolehippie/prometheus/master?logo=drone)](https://cloud.drone.io/rolehippie/prometheus) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/prometheus)](https://github.com/rolehippie/prometheus/blob/master/LICENSE) 

Ansible role to install and configure Prometheus. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [prometheus_alertmanagers](#prometheus_alertmanagers)
  * [prometheus_default_rules](#prometheus_default_rules)
  * [prometheus_domain](#prometheus_domain)
  * [prometheus_download](#prometheus_download)
  * [prometheus_evaluation_interval](#prometheus_evaluation_interval)
  * [prometheus_extra_rules](#prometheus_extra_rules)
  * [prometheus_rule_files](#prometheus_rule_files)
  * [prometheus_scrape_configs](#prometheus_scrape_configs)
  * [prometheus_scrape_interval](#prometheus_scrape_interval)
  * [prometheus_tsdb_retention_time](#prometheus_tsdb_retention_time)
  * [prometheus_version](#prometheus_version)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

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
prometheus_version: 2.19.1
```

## Dependencies

* [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
