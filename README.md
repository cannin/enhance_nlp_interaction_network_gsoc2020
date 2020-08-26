Github Action Workflows
---

This branch consists of workflows for Reactome Failed Query Analysis

| Workflow Name | README | Status | Purpose |
|-|-|-|-|
| [ConsistencyChecker](./.github/workflows/consistency_check.yml) | [View](./MTI/README.md) | ![ConsistencyChecker](https://github.com/pritishaw/enhance_nlp_interaction_network_gsoc2020/workflows/ConsistencyChecker/badge.svg?branch=cron-jobs) | Checks Interface changes in MTI Batch Processor, every Thursday at 01:00UTC, Failure indicates interface change|
| [Code Quality Check](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/blob/package/.github/workflows/test.yml) |  | ![CI](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/workflows/CI/badge.svg?branch=package) | This performs unit testing on the utils package and check code quality using Pylint, the workflow is also run as cron job, every Thursday at 00:00UTC to test the INDRA methods required for analysis |
