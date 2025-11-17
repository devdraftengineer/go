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

Place your OpenAPI specification file in the `./openapi/` directory. By default, the generator expects:

```
./openapi/api.yaml
```

You can use any filename, but you'll need to specify it when running the generator (see below).

### 3. Generate SDKs

Run the generator with the default spec file:

```bash
# Using pnpm
pnpm generate-sdks

# Or using npm
npm run generate-sdks

# Or using yarn
yarn generate-sdks
```

Or specify a custom OpenAPI spec path:

```bash
# Using pnpm
pnpm generate-sdks ./openapi/my-api.yaml

# Or using npm
npm run generate-sdks -- ./openapi/my-api.yaml

# Or using environment variable
OPENAPI_SPEC=./openapi/custom-api.yaml pnpm generate-sdks
```

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

After generation, each SDK can be published to its respective package manager. Here's a high-level overview:

### TypeScript/JavaScript (npm)

```bash
cd ./sdks/typescript
npm publish
```

### Python (PyPI)

```bash
cd ./sdks/python
python -m pip install build twine
python -m build
twine upload dist/*
```

### Java (Maven Central)

```bash
cd ./sdks/java
mvn clean deploy
```

### Go (Go Modules)

```bash
cd ./sdks/go
# Tag and push to your Git repository
git tag v1.0.0
git push origin v1.0.0
```

### C# (NuGet)

```bash
cd ./sdks/csharp
dotnet pack
dotnet nuget push bin/Debug/*.nupkg --source https://api.nuget.org/v3/index.json
```

### PHP (Packagist)

```bash
cd ./sdks/php
# Push to your Git repository and configure Packagist to auto-update
```

### Ruby (RubyGems)

```bash
cd ./sdks/ruby
gem build *.gemspec
gem push *.gem
```

## Project Structure

```
.
├── openapi/              # Place your OpenAPI spec files here
│   └── api.yaml         # Default spec file
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

1. Validates that the OpenAPI specification file exists
2. For each supported language:
   - Clears the existing output directory
   - Runs `openapi-generator-cli` with language-specific settings
   - Logs progress and results
3. Provides a summary of successful and failed generations
4. Exits with a non-zero status if any generation fails

## Requirements

- Node.js >= 18.0.0
- npm, yarn, or pnpm

## License

MIT

