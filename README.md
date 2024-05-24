
![image](static/banner_tradinglab.png)
## Cookiecutter for Strategy Containerization

[![image](https://github.com/TradingLab-app/cookiecutter-tradinglab-container/workflows/build/badge.svg)](https://github.com/TradingLab-app/cookiecutter-tradinglab-container/actions?query=workflow%3Abuild)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a containerized Python strategy.

-   GitHub repo: <https://github.com/TradingLab-app/cookiecutter-tradinglab-container>
-   Free software: BSD license

## Features

-   Testing setup with `unittest` or `pytest`
-   GitHub actions: Ready for GitHub Continuous Integration testing
-   [bump-my-version](https://github.com/callowayproject/bump-my-version): Pre-configured version bumping with a single command

## Usage

This guide provides detailed steps on how to create a Python package where you can write your own trading strategy, configure it for docker containerization, and manage its versioning and releases. First, install `cookiecutter`, `bump-my-version` and `poetry` and then follow the steps below.

```bash
pip install cookiecutter bump-my-version poetry
```

### _- dependency management_

We'll use poetry as the main dependency management and packaging tool. To add an open-source library, instead of using `pip install`, it can be easily done by:

```shell
poetry add requests
```

For more information about how to use poetry, please visit [Python-Poetry.org](https://python-poetry.org/docs/).

### 1. Create the Package Structure

Use `cookiecutter` to create a package structure. `cookiecutter` is a command-line utility that creates projects from templates.

```bash
cookiecutter gh:TradingLab-app/cookiecutter-tradinglab-container
```

### 2. Initialize and Commit to Git

Navigate to your project directory and initialize a Git repository:

```bash
cd your-package-name
git init
git add .
git commit -m "Initial commit"
```

### 3. Create a Repository on GitHub

-   Go to [GitHub](https://github.com/) and create a new empty repository.
-   Do NOT initialize it with a README, license, or .gitignore file.

### 4. Add Git Remote

Link your local repository to the GitHub repository. If your git branch is named `main`, use the following commands:

```bash
git remote add origin [your-repository-url]
git branch -M main
git push -u origin main
```

If your git branch is named `master`, use the following commands:

```bash
git remote add origin [your-repository-url]
git branch -M master
git push -u origin master
```

### 5. Configure GitHub Actions

Change the GitHub Actions settings in your repository to allow read and write operations:

-   Go to your repository on GitHub.
-   Click on `Settings` > `Actions` > `General` > `Workflow permissions`.
-   Change the settings to allow **read and write operations**.

### 6. Push to GitHub

Push your local changes to GitHub:

```bash
git push
```

### 7. Version Management with bump-my-version

Use `bump-my-version` for managing the version of your package:

-   First, do a dry run to see what changes will be made:

```bash
bump-my-version bump [patch/minor/major] --dry-run --verbose
```

-   If satisfied, apply the version bump:

```bash
bump-my-version bump [patch/minor/major]
```

### 8. Push Tags and Changes to GitHub

After bumping the version, push the tags and changes:

```bash
git push --tags
git push origin [main/master]
```

### 9. Add GitHub Repository Secrets

Add your GCP credentials as secrets in your GitHub repository in order to push your docker container to the Artifact Registry:

- **`GCP_CREDENTIALS`**: the service account key in json <sup>[1]</sup>
- **`GCP_REGION`**: the GCP region to host the repository <sup>[2]</sup>
- **`GAR_REPO_NAME`**: the repository name in which to store the docker image <sup>[3]</sup>

<span style="font-size:0.7em;">[1] Make sure that you grant artifact registry permission to this service account.</span>\
<span style="font-size:0.7em;">[2] You may refer to the [Regions](https://cloud.google.com/compute/docs/regions-zones#available) listed in the GCP documentation; you may disregard the zone suffix but only the zonal information (e.g. `asia-east1`).</span>\
<span style="font-size:0.7em;">[3] It is strongly suggested to follow the naming convention of `[username]-[project_slug]-strategy-repo`</span>

### 10. Make a New Release on GitHub

Finally, make a new release on GitHub with the updated version.

---

Remember to replace placeholders (like `your-package-name` and `[your-repository-url]`) with actual values relevant to your package. This guide assumes basic familiarity with Git, GitHub, and Python packaging conventions.
