# ci-cd-final-project — IBM DevOps & Software Engineering Certificate

[![CI Pipeline](https://github.com/dishathakur1625-cpu/cicd-final-project/actions/workflows/workflow.yml/badge.svg)](https://github.com/dishathakur1625-cpu/cicd-final-project/actions/workflows/workflow.yml)

## Project Overview

This repository contains the **CI/CD Final Project** for the IBM DevOps and Software Engineering Professional Certificate on Coursera. It demonstrates a complete end-to-end CI/CD pipeline using:

- **GitHub Actions** — automated linting (flake8) and unit testing (nose/pytest) on every push/pull request
- **Tekton** — Kubernetes-native pipelines with cleanup and test tasks
- **OpenShift** — cloud-native container platform for deploying the pipeline

## Repository Structure

```
cicd-final-project/
├── .github/
│   └── workflows/
│       └── workflow.yml        # GitHub Actions CI workflow
├── .tekton/
│   └── tasks.yml               # Tekton Task definitions
├── src/
│   └── app.py                  # Sample application code
├── tests/
│   └── test_app.py             # Unit tests (nosetests/pytest)
├── requirements.txt            # Python dependencies
├── setup.cfg                   # nosetests & flake8 config
└── README.md                   # This file
```

## CI/CD Pipeline Details

### GitHub Actions Workflow (`.github/workflows/workflow.yml`)

Triggered on every `push` and `pull_request` to the `main` branch:

| Step | Tool | Purpose |
|------|------|---------|
| Lint | `flake8` | Enforce PEP-8 code style |
| Test | `nosetests` | Run unit tests with coverage |

### Tekton Tasks (`.tekton/tasks.yml`)

| Task Name | Description |
|-----------|-------------|
| `cleanup` | Cleans the workspace before the pipeline run |
| `nose`    | Runs unit tests using `nosetests` |

### OpenShift Pipeline

The pipeline (`oc-pipelines-oc-final`) is configured to:
1. Clone the repository
2. Run the `cleanup` task
3. Execute unit tests via the `nose` task

## Getting Started

### Prerequisites

- Python 3.9+
- `pip` package manager
- (Optional) OpenShift CLI (`oc`) for cloud deployment

### Local Setup

```bash
# Clone the repository
git clone https://github.com/dishathakur1625-cpu/cicd-final-project.git
cd cicd-final-project

# Install dependencies
pip install -r requirements.txt

# Run linting
flake8 src/ tests/ --max-line-length=100

# Run unit tests
nosetests tests/ -v
```

## OpenShift Pipeline Setup

To run the Tekton pipeline on OpenShift:

```bash
# 1. Login to your OpenShift cluster
oc login --token=<your-token> --server=<your-server-url>

# 2. Create a new project
oc new-project cicd-final-project

# 3. Apply Tekton tasks
oc apply -f .tekton/tasks.yml

# 4. Create the pipeline run
oc create -f .tekton/pipeline-run.yml

# 5. Watch the pipeline run
tkn pipelinerun list
tkn pipelinerun logs --last -f
```

## Author

**Disha Thakur** — Coursera IBM DevOps & Software Engineering Professional Certificate
