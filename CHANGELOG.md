# Changelog

## [1.8.2](https://github.com/rolehippie/prometheus/compare/v1.8.1...v1.8.2) (2023-10-09)


### Bugfixes

* **deps:** update dependency prometheus/prometheus to v2.47.1 ([d2b751a](https://github.com/rolehippie/prometheus/commit/d2b751a6db0e119f9152a63ef2866a6781883ed1))

## [1.8.1](https://github.com/rolehippie/prometheus/compare/v1.8.0...v1.8.1) (2023-09-25)


### Bugfixes

* **deps:** update dependency oauth2-proxy/oauth2-proxy to v7.5.1 ([0f7d548](https://github.com/rolehippie/prometheus/commit/0f7d548e04ef90c462524891e4e0668511e22ad6))

## [1.8.0](https://github.com/rolehippie/prometheus/compare/v1.7.0...v1.8.0) (2023-09-11)


### Features

* **deps:** update dependency oauth2-proxy/oauth2-proxy to v7.5.0 ([cf5ee78](https://github.com/rolehippie/prometheus/commit/cf5ee78eca6b502b241b5690e0f1b5ac1555e84b))
* **deps:** update dependency prometheus/prometheus to v2.47.0 ([6fb108c](https://github.com/rolehippie/prometheus/commit/6fb108c3ce43bf272cb7d966558536ece2fcc7cc))

## [1.7.0](https://github.com/rolehippie/prometheus/compare/v1.6.0...v1.7.0) (2023-08-24)


### Features

* add optional defaults for cpu and memory limit ([4e92a98](https://github.com/rolehippie/prometheus/commit/4e92a9865c07539ffcd8434a88d9a67653a5268c))

## [1.6.0](https://github.com/rolehippie/prometheus/compare/v1.5.0...v1.6.0) (2023-07-31)


### Features

* **deps:** update dependency prometheus/prometheus to v2.46.0 ([5dad620](https://github.com/rolehippie/prometheus/commit/5dad62033cc0f90ea924530b7b2fcfedab7fa608))

## [1.5.0](https://github.com/rolehippie/prometheus/compare/v1.4.1...v1.5.0) (2023-07-06)


### Features

* add options to disable access and auth logging for oauth2 proxy ([4330c25](https://github.com/rolehippie/prometheus/commit/4330c253dfdb572faff28189716a7faaa1fe4304))
* move image pull to tasks from service and create network ([4f85436](https://github.com/rolehippie/prometheus/commit/4f85436fc1912fbaf2ebf2115ecdf8c7c07f9840))

## [1.4.1](https://github.com/rolehippie/prometheus/compare/v1.4.0...v1.4.1) (2023-07-05)


### Bugfixes

* no prometheus user for docker install ([c9473d2](https://github.com/rolehippie/prometheus/commit/c9473d2cf213d74ef60f9cd6f437a91150dfbfc8))

## [1.4.0](https://github.com/rolehippie/prometheus/compare/v1.3.0...v1.4.0) (2023-06-26)


### Features

* **deps:** update dependency prometheus/prometheus to v2.45.0 ([607d4b2](https://github.com/rolehippie/prometheus/commit/607d4b2dc89035bd15a72efeefb3adcc43546438))

## [1.3.0](https://github.com/rolehippie/prometheus/compare/v1.2.1...v1.3.0) (2023-05-15)


### Features

* **deps:** update dependency prometheus/prometheus to v2.44.0 ([7385bf3](https://github.com/rolehippie/prometheus/commit/7385bf336023de302a571bbc76bdf65befcc02d6))

## [1.2.1](https://github.com/rolehippie/prometheus/compare/v1.2.0...v1.2.1) (2023-05-08)


### Bugfixes

* **deps:** update dependency prometheus/prometheus to v2.43.1+stringlabels ([e953e11](https://github.com/rolehippie/prometheus/commit/e953e1178788d45e61da9f88f97ddccf9fdc20fe))

## [1.2.0](https://github.com/rolehippie/prometheus/compare/v1.1.0...v1.2.0) (2023-03-27)


### Features

* **deps:** update dependency prometheus/prometheus to v2.43.0+stringlabels ([5bce7ca](https://github.com/rolehippie/prometheus/commit/5bce7caf7e1761dbd0fdb04b281b2af7fbba229a))

## [1.1.0](https://github.com/rolehippie/prometheus/compare/v1.0.0...v1.1.0) (2023-02-06)


### Features

* **deps:** update dependency prometheus/prometheus to v2.42.0 ([3839fcd](https://github.com/rolehippie/prometheus/commit/3839fcd926a3afe4adcde31303df011cc0586be4))

## 1.0.0 (2023-01-05)


### Features

* add default for retention size ([a4b1eed](https://github.com/rolehippie/prometheus/commit/a4b1eedd860a33abe8845706535b5ca9d996dc3a))
* integrate docker install method ([1053bec](https://github.com/rolehippie/prometheus/commit/1053becf9113f1b813b5e3fc12e461d4ec8a0d2f))
* restructure workflows and enable automated releases ([044558e](https://github.com/rolehippie/prometheus/commit/044558e2fffeaf30556febb13c28792e3a7fbdd5))


### Bugfixes

* move argument to a position here it always can end with slash ([8db6ca5](https://github.com/rolehippie/prometheus/commit/8db6ca56a45c6b675f679c9210668eec667069b5))
* move default more to the top ([2ac9374](https://github.com/rolehippie/prometheus/commit/2ac937495a3725fdc5d0d86dd0e4e375188ecf54))
* stdout and stderr for oauth2 version check ([6912b2c](https://github.com/rolehippie/prometheus/commit/6912b2c9a62602e232a6463738b0d74a70e1b258))
* tsdb is not part of archive anymore, drop it from fs as well ([9f23383](https://github.com/rolehippie/prometheus/commit/9f23383bc01645b408e00843a7e2f9215923c7fb))
* use include_tasks instead of include ([2a1dd6b](https://github.com/rolehippie/prometheus/commit/2a1dd6b1d6e1e70452c465a2c1bdcd2a92362c1c))
* use keycloak-oidc provider for oauth2 proxy ([86f88f7](https://github.com/rolehippie/prometheus/commit/86f88f7143e07e215bf118ffa15b64f3bcab6fba))
