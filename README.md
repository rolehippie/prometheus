# prometheus

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/prometheus) [![Build Status](https://img.shields.io/drone/build/rolehippie/prometheus/master?logo=drone)](https://cloud.drone.io/rolehippie/prometheus) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/prometheus)](https://github.com/rolehippie/prometheus/blob/master/LICENSE) 

Ansible role to install and configure Prometheus. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [prometheus_alertmanagers](#prometheus_alertmanagers)
  * [prometheus_default_folders](#prometheus_default_folders)
  * [prometheus_default_labels](#prometheus_default_labels)
  * [prometheus_default_publish](#prometheus_default_publish)
  * [prometheus_default_rules](#prometheus_default_rules)
  * [prometheus_default_volumes](#prometheus_default_volumes)
  * [prometheus_domain](#prometheus_domain)
  * [prometheus_evaluation_interval](#prometheus_evaluation_interval)
  * [prometheus_extra_folders](#prometheus_extra_folders)
  * [prometheus_extra_labels](#prometheus_extra_labels)
  * [prometheus_extra_publish](#prometheus_extra_publish)
  * [prometheus_extra_rules](#prometheus_extra_rules)
  * [prometheus_extra_volumes](#prometheus_extra_volumes)
  * [prometheus_image](#prometheus_image)
  * [prometheus_network](#prometheus_network)
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

### prometheus_default_folders

List of default folders to create

#### Default value

```YAML
prometheus_default_folders:
  - /etc/prometheus/rules
  - /var/lib/prometheus
```

### prometheus_default_labels

List of default labels to assign to docker command

#### Default value

```YAML
prometheus_default_labels: []
```

### prometheus_default_publish

List of default port publishing

#### Default value

```YAML
prometheus_default_publish:
  - 9090:9090
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

List of default volumes to mount

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

List of extra labels to assign to docker command

#### Default value

```YAML
prometheus_extra_labels: []
```

### prometheus_extra_publish

List of extra port publishing

#### Default value

```YAML
prometheus_extra_publish: []
```

#### Example usage

```YAML
prometheus_extra_publish:
  - 8080:8080
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

List of extra volumes to mount

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

Docker image to use for deployment

#### Default value

```YAML
prometheus_image: quay.io/prometheus/prometheus:v{{ prometheus_version }}
```

### prometheus_network

Optionally assign this Docker network to container

#### Default value

```YAML
prometheus_network:
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

Version of Prometheus to use

#### Default value

```YAML
prometheus_version: 2.23.0
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
