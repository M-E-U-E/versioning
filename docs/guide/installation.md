# Installation Guide

## Prerequisites

1. Python 3.7 or later
2. pip package manager
3. Git

## Basic Installation

```bash
pip install mkdocs
pip install mkdocs-material
pip install mike
```

## Configuration

1. Create mkdocs.yml:
```yaml
site_name: My Dummy Project
repo_url: https://github.com/M-E-U-E/versioning
site_dir: site

theme:
  name: material

plugins:
  - search
  - mike

extra:
  version:
    provider: mike
    default: latest
    name: 1.1
    alias: latest
```