# SDK Deployment Guide

This guide provides step-by-step instructions for publishing each generated SDK to its respective package manager.

## Table of Contents

- [TypeScript/JavaScript (npm)](#typescriptjavascript-npm)
- [Python (PyPI)](#python-pypi)
- [Java (Maven Central)](#java-maven-central)
- [Go (Go Modules)](#go-go-modules)
- [C# (NuGet)](#c-nuget)
- [PHP (Packagist)](#php-packagist)
- [Ruby (RubyGems)](#ruby-rubygems)

---

## TypeScript/JavaScript (npm)

### Prerequisites

- npm account (create at [npmjs.com](https://www.npmjs.com/signup))
- npm CLI installed (`npm install -g npm`)

### Steps

1. **Navigate to the TypeScript SDK directory:**
   ```bash
   cd ./sdks/typescript
   ```

2. **Review and update `package.json`:**
   - Verify `name`, `version`, `description`, `author`, `license`
   - Update `repository` URL if needed
   - Ensure `main`, `types`, and `files` fields are correct

3. **Login to npm:**
   ```bash
   npm login
   ```
   Enter your npm username, password, and email when prompted.

4. **Test the package locally (optional):**
   ```bash
   npm pack
   # This creates a .tgz file you can inspect
   ```

5. **Publish to npm:**
   ```bash
   npm publish
   ```
   
   For scoped packages (e.g., `@mycompany/api-client`), publish publicly:
   ```bash
   npm publish --access public
   ```

6. **Verify publication:**
   Visit `https://www.npmjs.com/package/YOUR_PACKAGE_NAME`

### Updating Versions

```bash
# Update version in package.json, then:
npm version patch  # 1.0.0 -> 1.0.1
npm version minor   # 1.0.0 -> 1.1.0
npm version major   # 1.0.0 -> 2.0.0

npm publish
```

### Configuration Tips

- Use `.npmignore` to exclude unnecessary files
- Set `"private": false` in `package.json` if publishing
- Consider using [semantic versioning](https://semver.org/)

---

## Python (PyPI)

### Prerequisites

- PyPI account (create at [pypi.org](https://pypi.org/account/register/))
- `build` and `twine` packages installed:
  ```bash
  pip install build twine
  ```

### Steps

1. **Navigate to the Python SDK directory:**
   ```bash
   cd ./sdks/python
   ```

2. **Review `setup.py` or `pyproject.toml`:**
   - Verify package name, version, author, description
   - Check `install_requires` dependencies
   - Update `url`, `author_email` if needed

3. **Build the package:**
   ```bash
   python -m build
   ```
   This creates `dist/` directory with `.whl` and `.tar.gz` files.

4. **Test the build locally (optional):**
   ```bash
   pip install dist/your_package-*.whl
   ```

5. **Upload to TestPyPI first (recommended):**
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```
   Create a TestPyPI account at [test.pypi.org](https://test.pypi.org/)

6. **Test installation from TestPyPI:**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ your-package-name
   ```

7. **Upload to PyPI:**
   ```bash
   python -m twine upload dist/*
   ```
   Enter your PyPI username and password when prompted.

8. **Verify publication:**
   Visit `https://pypi.org/project/YOUR_PACKAGE_NAME/`

### Updating Versions

1. Update version in `setup.py` or `pyproject.toml`
2. Rebuild and upload:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

### Configuration Tips

- Use `MANIFEST.in` to include additional files
- Consider using `pyproject.toml` for modern Python packaging
- Set up API tokens for automated publishing (avoid using passwords)

---

## Java (Maven Central)

### Prerequisites

- Sonatype account (create at [issues.sonatype.org](https://issues.sonatype.org/))
- GPG key for signing artifacts
- Maven installed (`brew install maven` or download from [maven.apache.org](https://maven.apache.org/))

### Steps

1. **Navigate to the Java SDK directory:**
   ```bash
   cd ./sdks/java
   ```

2. **Set up GPG signing:**
   ```bash
   # Generate GPG key (if you don't have one)
   gpg --gen-key
   
   # Export your public key
   gpg --keyserver keyserver.ubuntu.com --send-keys YOUR_KEY_ID
   ```

3. **Configure Maven `settings.xml`:**
   Create/edit `~/.m2/settings.xml`:
   ```xml
   <settings>
     <servers>
       <server>
         <id>ossrh</id>
         <username>YOUR_SONATYPE_USERNAME</username>
         <password>YOUR_SONATYPE_PASSWORD</password>
       </server>
     </servers>
   </settings>
   ```

4. **Review `pom.xml`:**
   - Verify `groupId`, `artifactId`, `version`
   - Check `name`, `description`, `url`, `licenses`
   - Ensure `scm` and `developers` sections are filled

5. **Build and verify:**
   ```bash
   mvn clean install
   mvn clean verify
   ```

6. **Deploy to Maven Central:**
   ```bash
   mvn clean deploy
   ```
   
   This uploads to Sonatype's staging repository.

7. **Release via Sonatype Nexus:**
   - Log in to [oss.sonatype.org](https://oss.sonatype.org/)
   - Go to "Staging Repositories"
   - Find your repository, select it, click "Close"
   - After validation, click "Release"
   - Your package will sync to Maven Central (takes ~10 minutes)

8. **Verify publication:**
   Visit `https://repo1.maven.org/maven2/com/yourcompany/your-artifact/`

### Updating Versions

Update version in `pom.xml`:
```xml
<version>1.0.1</version>
```

Then rebuild and deploy:
```bash
mvn clean deploy
```

### Configuration Tips

- First-time publishers need to create a JIRA ticket at [issues.sonatype.org](https://issues.sonatype.org/)
- Use `mvn versions:set -DnewVersion=1.0.1` to update version
- Consider using GitHub Actions for automated releases

---

## Go (Go Modules)

### Prerequisites

- Git repository (GitHub, GitLab, etc.)
- Go 1.11+ installed
- Git tags for versioning

### Steps

1. **Navigate to the Go SDK directory:**
   ```bash
   cd ./sdks/go
   ```

2. **Review `go.mod`:**
   - Verify module name (e.g., `github.com/yourcompany/api-client`)
   - Check Go version requirement

3. **Initialize Git repository (if not already):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Push to remote repository:**
   ```bash
   git remote add origin https://github.com/yourcompany/api-client.git
   git push -u origin main
   ```

5. **Create and push a version tag:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

6. **Verify publication:**
   Users can now install with:
   ```bash
   go get github.com/yourcompany/api-client@v1.0.0
   ```

### Updating Versions

1. Update code and commit:
   ```bash
   git add .
   git commit -m "Update to v1.0.1"
   ```

2. Create and push new tag:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

### Configuration Tips

- Use semantic versioning tags (`v1.0.0`, `v1.1.0`, `v2.0.0`)
- Add `go.sum` to version control
- Consider using [goreleaser](https://goreleaser.com/) for automated releases
- Document your module in a README.md

---

## C# (NuGet)

### Prerequisites

- NuGet account (create at [nuget.org](https://www.nuget.org/users/account/LogOn))
- .NET SDK installed (download from [dotnet.microsoft.com](https://dotnet.microsoft.com/download))

### Steps

1. **Navigate to the C# SDK directory:**
   ```bash
   cd ./sdks/csharp
   ```

2. **Review `.csproj` file:**
   - Verify `PackageId`, `Version`, `Authors`, `Description`
   - Check `PackageLicenseExpression` or `PackageLicenseUrl`
   - Update `RepositoryUrl` if needed

3. **Build the package:**
   ```bash
   dotnet build --configuration Release
   ```

4. **Pack the NuGet package:**
   ```bash
   dotnet pack --configuration Release
   ```
   This creates a `.nupkg` file in `bin/Release/`.

5. **Get your API key:**
   - Log in to [nuget.org](https://www.nuget.org/)
   - Go to Account Settings → API Keys
   - Create a new API key
   - Copy the key (you won't see it again)

6. **Publish to NuGet:**
   ```bash
   dotnet nuget push bin/Release/*.nupkg \
     --api-key YOUR_API_KEY \
     --source https://api.nuget.org/v3/index.json
   ```

   Or use interactive mode:
   ```bash
   dotnet nuget push bin/Release/*.nupkg \
     --source https://api.nuget.org/v3/index.json
   ```

7. **Verify publication:**
   Visit `https://www.nuget.org/packages/YOUR_PACKAGE_ID/`

### Updating Versions

Update version in `.csproj`:
```xml
<Version>1.0.1</Version>
```

Then rebuild, pack, and push:
```bash
dotnet pack --configuration Release
dotnet nuget push bin/Release/*.nupkg --api-key YOUR_API_KEY --source https://api.nuget.org/v3/index.json
```

### Configuration Tips

- Use `dotnet pack` with `--include-symbols` for symbol packages
- Consider using [GitHub Actions](https://github.com/marketplace/actions/publish-nuget) for CI/CD
- Set up API key as environment variable or use `nuget.config` for security

---

## PHP (Packagist)

### Prerequisites

- Packagist account (create at [packagist.org](https://packagist.org/register/))
- Git repository (GitHub, GitLab, Bitbucket)

### Steps

1. **Navigate to the PHP SDK directory:**
   ```bash
   cd ./sdks/php
   ```

2. **Review `composer.json`:**
   - Verify `name`, `description`, `type`, `license`
   - Check `autoload` configuration
   - Update `authors` section

3. **Initialize Git repository (if not already):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Push to remote repository:**
   ```bash
   git remote add origin https://github.com/yourcompany/api-client-php.git
   git push -u origin main
   ```

5. **Create a release tag:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

6. **Submit to Packagist:**
   - Log in to [packagist.org](https://packagist.org/)
   - Click "Submit" in the top menu
   - Enter your repository URL (e.g., `https://github.com/yourcompany/api-client-php`)
   - Click "Check" and then "Submit"

7. **Set up GitHub webhook (recommended):**
   - In your GitHub repository, go to Settings → Webhooks
   - Add webhook URL: `https://packagist.org/api/github?username=YOUR_PACKAGIST_USERNAME&apiToken=YOUR_API_TOKEN`
   - This auto-updates Packagist when you push tags

8. **Verify publication:**
   Visit `https://packagist.org/packages/yourcompany/api-client`

### Updating Versions

1. Update version in `composer.json`:
   ```json
   "version": "1.0.1"
   ```

2. Commit and tag:
   ```bash
   git add composer.json
   git commit -m "Release v1.0.1"
   git tag v1.0.1
   git push origin main --tags
   ```

3. Packagist will auto-update if webhook is configured, or manually click "Update" on Packagist

### Configuration Tips

- Use semantic versioning
- Ensure `composer.json` is valid (run `composer validate`)
- Add a `README.md` for better package visibility
- Consider using GitHub Actions to automate releases

---

## Ruby (RubyGems)

### Prerequisites

- RubyGems account (create at [rubygems.org](https://rubygems.org/sign_up))
- Ruby and RubyGems installed

### Steps

1. **Navigate to the Ruby SDK directory:**
   ```bash
   cd ./sdks/ruby
   ```

2. **Review `.gemspec` file:**
   - Verify `name`, `version`, `summary`, `description`
   - Check `authors`, `email`, `homepage`
   - Update `license` if needed

3. **Build the gem:**
   ```bash
   gem build *.gemspec
   ```
   This creates a `.gem` file.

4. **Test the gem locally (optional):**
   ```bash
   gem install ./your-gem-1.0.0.gem
   ```

5. **Login to RubyGems:**
   ```bash
   gem signin
   ```
   Enter your RubyGems email and password.

6. **Publish to RubyGems:**
   ```bash
   gem push your-gem-1.0.0.gem
   ```

   Or push all `.gem` files:
   ```bash
   gem push *.gem
   ```

7. **Verify publication:**
   Visit `https://rubygems.org/gems/YOUR_GEM_NAME`

### Updating Versions

1. Update version in `.gemspec`:
   ```ruby
   spec.version = "1.0.1"
   ```

2. Rebuild and push:
   ```bash
   gem build *.gemspec
   gem push your-gem-1.0.1.gem
   ```

### Configuration Tips

- Use semantic versioning
- Add a `README.md` for documentation
- Consider using [GitHub Actions](https://github.com/marketplace/actions/publish-rubygems) for CI/CD
- Use `gem yank` to remove a bad release (use carefully)

---

## General Best Practices

### Version Management

- Use [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH)
- Update version numbers before publishing
- Tag releases in Git for all SDKs

### Documentation

- Include a `README.md` with:
  - Installation instructions
  - Basic usage examples
  - API documentation links
  - Contributing guidelines

### CI/CD

Consider setting up automated publishing:
- **GitHub Actions** for npm, PyPI, NuGet, RubyGems
- **GitLab CI** for all platforms
- **CircleCI** or **Travis CI** alternatives

### Security

- Use API tokens/keys instead of passwords when possible
- Store secrets in environment variables or secret managers
- Enable 2FA on all package manager accounts
- Review dependencies for security vulnerabilities

### Testing

- Test packages locally before publishing
- Use test repositories (TestPyPI, npm test registry) when available
- Verify installation from the published package

---

## Quick Reference

| Language | Package Manager | Command |
|----------|----------------|---------|
| TypeScript | npm | `npm publish` |
| Python | PyPI | `twine upload dist/*` |
| Java | Maven Central | `mvn clean deploy` |
| Go | Go Modules | `git tag v1.0.0 && git push --tags` |
| C# | NuGet | `dotnet nuget push *.nupkg` |
| PHP | Packagist | Submit via web UI |
| Ruby | RubyGems | `gem push *.gem` |

---

## Troubleshooting

### Common Issues

1. **Authentication errors**: Verify credentials and API keys
2. **Version conflicts**: Ensure version numbers are incremented
3. **Build failures**: Check dependencies and build configuration
4. **Publishing delays**: Some registries take time to index (Maven Central: ~10 minutes)

### Getting Help

- Check package manager documentation
- Review generated SDK documentation
- Check GitHub issues for the OpenAPI Generator
- Consult package manager support forums

---

**Last Updated**: 2024

