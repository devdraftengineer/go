# SDK Factory

A simple, repeatable setup for generating multi-language SDKs from OpenAPI specifications using OpenAPI Generator.

## Overview

This project provides a single command interface to generate SDKs for multiple popular programming languages from a single OpenAPI specification file.

## Supported Languages

- **TypeScript** (typescript-fetch generator)
- **Python** (python generator)
- **Java** (java generator)
- **Go** (go generator)
- **C#** (csharp generator)
- **PHP** (php generator)
- **Ruby** (ruby generator)

## Quick Start

### 1. Install Dependencies

```bash
# Using pnpm (recommended)
pnpm install

# Or using npm
npm install

# Or using yarn
yarn install
```

### 2. Place Your OpenAPI Specification

Place your OpenAPI specification file in the `./openapi/` directory. The generator supports:

- **Formats**: `.yml`, `.yaml`, or `.json`
- **Auto-detection**: The script will automatically find any spec file in the `./openapi/` directory
- **Priority order**: If multiple files exist, it will prefer files named:
  1. `api.yaml` / `api.yml`
  2. `openapi.yaml` / `openapi.yml` / `openapi.json`
  3. `spec.yaml` / `spec.yml` / `spec.json`
  4. Any other file with a supported extension

Example:
```
./openapi/api.yaml
./openapi/my-api.yml
./openapi/openapi.json
```

### 3. Generate SDKs

The generator will automatically detect your OpenAPI spec file in the `./openapi/` directory:

```bash
# Using pnpm (auto-detects spec file)
pnpm generate-sdks

# Or using npm
npm run generate-sdks

# Or using yarn
yarn generate-sdks
```

You can also explicitly specify a spec file path:

```bash
# Using pnpm
pnpm generate-sdks ./openapi/my-api.yaml

# Or using npm
npm run generate-sdks -- ./openapi/my-api.yaml

# Or using environment variable
OPENAPI_SPEC=./openapi/custom-api.yaml pnpm generate-sdks
```

**Note**: The script supports `.yml`, `.yaml`, and `.json` formats. If no path is provided, it will automatically search for and use the first valid spec file found in `./openapi/`.

### 4. Find Your Generated SDKs

All generated SDKs are placed in the `./sdks/` directory, organized by language:

```
./sdks/
  ├── typescript/
  ├── python/
  ├── java/
  ├── go/
  ├── csharp/
  ├── php/
  └── ruby/
```

## Configuration

### Package Names and Versions

You can customize package names, versions, and other generator-specific properties by editing `generator-config.json` in the project root.

Example:

```json
{
  "typescript": {
    "npmName": "@mycompany/api-client",
    "npmVersion": "1.0.0"
  },
  "python": {
    "packageName": "api_client",
    "packageVersion": "1.0.0",
    "projectName": "api-client"
  }
}
```

See `generator-config.json` for all available configuration options.

## Publishing Generated SDKs

After generation, each SDK can be published to its respective package manager. 

📖 **For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)**

The deployment guide includes:
- Step-by-step publishing instructions for each language
- Prerequisites and account setup
- Version management best practices
- CI/CD recommendations
- Troubleshooting tips

### Quick Reference

| Language | Package Manager | Quick Command |
|----------|----------------|---------------|
| TypeScript | npm | `cd ./sdks/typescript && npm publish` |
| Python | PyPI | `cd ./sdks/python && python -m build && twine upload dist/*` |
| Java | Maven Central | `cd ./sdks/java && mvn clean deploy` |
| Go | Go Modules | `cd ./sdks/go && git tag v1.0.0 && git push --tags` |
| C# | NuGet | `cd ./sdks/csharp && dotnet pack && dotnet nuget push *.nupkg` |
| PHP | Packagist | Submit repository URL via web UI |
| Ruby | RubyGems | `cd ./sdks/ruby && gem build *.gemspec && gem push *.gem` |

## Project Structure

```
.
├── openapi/              # Place your OpenAPI spec files here (.yml, .yaml, or .json)
│   └── api.yaml         # Example spec file (auto-detected)
├── sdks/                # Generated SDKs (one folder per language)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   ├── go/
│   ├── csharp/
│   ├── php/
│   └── ruby/
├── scripts/
│   └── generate-sdks.mjs  # Main generation script
├── generator-config.json  # Configuration for package names/versions
├── package.json
└── README.md
```

## How It Works

The `generate-sdks.mjs` script:

1. **Auto-detects** the OpenAPI specification file:
   - If a path is provided, it uses that path
   - If no path is provided, it searches `./openapi/` for files with `.yml`, `.yaml`, or `.json` extensions
   - Uses a priority order for common filenames (api.yaml, openapi.yaml, etc.)
2. Validates that the spec file exists
3. For each supported language:
   - Clears the existing output directory
   - Runs `openapi-generator-cli` with language-specific settings
   - Logs progress and results
4. Provides a summary of successful and failed generations
5. Exits with a non-zero status if any generation fails

## Requirements

- **Node.js** >= 18.0.0
- **Java** >= 11 (required by `@openapitools/openapi-generator-cli`)
- **npm**, **yarn**, or **pnpm**

### Java Requirement

The `@openapitools/openapi-generator-cli` package requires Java 11 or higher to be installed on your system. If you encounter Java-related errors:

**macOS (using Homebrew):**
```bash
brew install openjdk@11
# Or for the latest LTS version:
brew install openjdk@17
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

**Windows:**
Download and install from [Adoptium](https://adoptium.net/) or [Oracle](https://www.oracle.com/java/technologies/downloads/)

**Verify installation:**
```bash
java -version
# Should show version 11 or higher
```

**Note:** The `@openapitools/openapi-generator-cli` package will provide its own error messages if Java is missing or the wrong version.

## License

MIT

