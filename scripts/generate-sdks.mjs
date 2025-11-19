#!/usr/bin/env node

/**
 * SDK Generator Script
 * 
 * Generates SDKs for multiple languages from an OpenAPI specification.
 * 
 * Auto-detection:
 *   - If no path is provided, automatically searches ./openapi/ for spec files
 *   - Supports .yml, .yaml, and .json formats
 *   - Priority: api.yaml > openapi.yaml > spec.yaml > any other .yml/.yaml/.json file
 * 
 * Usage:
 *   node ./scripts/generate-sdks.mjs [path-to-openapi-spec]
 * 
 * Examples:
 *   # Auto-detect spec file in ./openapi/
 *   node ./scripts/generate-sdks.mjs
 *   pnpm generate-sdks
 * 
 *   # Explicitly specify a spec file
 *   node ./scripts/generate-sdks.mjs ./openapi/api.yaml
 *   node ./scripts/generate-sdks.mjs ./openapi/my-api.yml
 *   node ./scripts/generate-sdks.mjs ./openapi/openapi.json
 * 
 *   # Via npm/yarn
 *   npm run generate-sdks -- ./openapi/custom-api.yaml
 * 
 *   # Via environment variable
 *   OPENAPI_SPEC=./openapi/custom-api.yaml pnpm generate-sdks
 */

import { execSync } from 'child_process';
import { existsSync, rmSync, mkdirSync, readdirSync } from 'fs';
import { resolve, dirname, extname, join, relative } from 'path';
import { fileURLToPath } from 'url';
import { readFileSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = resolve(__dirname, '..');

// Load generator configuration
const configPath = resolve(projectRoot, 'generator-config.json');
let generatorConfig = {};
if (existsSync(configPath)) {
  try {
    generatorConfig = JSON.parse(readFileSync(configPath, 'utf-8'));
  } catch (error) {
    console.warn(`Warning: Could not parse generator-config.json: ${error.message}`);
  }
}

// Default generator configurations
const generators = [
  {
    name: 'TypeScript',
    generator: 'typescript-fetch',
    outputDir: 'typescript',
    additionalProperties: {
      npmName: generatorConfig.typescript?.npmName || '@mycompany/api-client',
      npmVersion: generatorConfig.typescript?.npmVersion || '1.0.0',
      supportsES6: 'true',
      typescriptThreePlus: 'true'
    }
  },
  {
    name: 'Python',
    generator: 'python',
    outputDir: 'python',
    additionalProperties: {
      packageName: generatorConfig.python?.packageName || 'api_client',
      packageVersion: generatorConfig.python?.packageVersion || '1.0.0',
      projectName: generatorConfig.python?.projectName || 'api-client'
    }
  },
  {
    name: 'Java',
    generator: 'java',
    outputDir: 'java',
    additionalProperties: {
      groupId: generatorConfig.java?.groupId || 'com.mycompany',
      artifactId: generatorConfig.java?.artifactId || 'api-client',
      artifactVersion: generatorConfig.java?.artifactVersion || '1.0.0',
      library: 'native',
      java8: 'true'
    }
  },
  {
    name: 'Go',
    generator: 'go',
    outputDir: 'go',
    additionalProperties: {
      packageName: generatorConfig.go?.packageName || 'api',
      packageVersion: generatorConfig.go?.packageVersion || '1.0.0',
      moduleName: generatorConfig.go?.moduleName || 'github.com/mycompany/api-client'
    }
  },
  {
    name: 'C#',
    generator: 'csharp',
    outputDir: 'csharp',
    additionalProperties: {
      packageName: generatorConfig.csharp?.packageName || 'ApiClient',
      packageVersion: generatorConfig.csharp?.packageVersion || '1.0.0',
      targetFramework: 'netstandard2.0'
    }
  },
  {
    name: 'PHP',
    generator: 'php',
    outputDir: 'php',
    additionalProperties: {
      packageName: generatorConfig.php?.packageName || 'api-client',
      packageVersion: generatorConfig.php?.packageVersion || '1.0.0',
      invokerPackage: generatorConfig.php?.invokerPackage || 'ApiClient'
    }
  },
  {
    name: 'Ruby',
    generator: 'ruby',
    outputDir: 'ruby',
    additionalProperties: {
      gemName: generatorConfig.ruby?.gemName || 'api_client',
      gemVersion: generatorConfig.ruby?.gemVersion || '1.0.0',
      moduleName: generatorConfig.ruby?.moduleName || 'ApiClient'
    }
  }
];

/**
 * Auto-detect OpenAPI spec file in the openapi directory
 * Supports .yml, .yaml, and .json extensions
 */
function detectSpecFile(openapiDir) {
  const supportedExtensions = ['.yml', '.yaml', '.json'];
  const priorityOrder = ['api.yaml', 'api.yml', 'openapi.yaml', 'openapi.yml', 'openapi.json', 'spec.yaml', 'spec.yml', 'spec.json'];
  
  if (!existsSync(openapiDir)) {
    return null;
  }
  
  try {
    const files = readdirSync(openapiDir);
    
    // First, check for priority filenames
    for (const priorityFile of priorityOrder) {
      if (files.includes(priorityFile)) {
        const filePath = join(openapiDir, priorityFile);
        if (existsSync(filePath)) {
          return filePath;
        }
      }
    }
    
    // If no priority file found, find any file with supported extension
    for (const file of files) {
      const ext = extname(file).toLowerCase();
      if (supportedExtensions.includes(ext)) {
        const filePath = join(openapiDir, file);
        if (existsSync(filePath)) {
          return filePath;
        }
      }
    }
  } catch (error) {
    console.warn(`Warning: Could not read openapi directory: ${error.message}`);
  }
  
  return null;
}

/**
 * Convert additional properties object to CLI string format
 */
function formatAdditionalProperties(props) {
  return Object.entries(props)
    .map(([key, value]) => `${key}=${value}`)
    .join(',');
}

/**
 * Clear output directory if it exists
 */
function clearOutputDir(outputPath) {
  if (existsSync(outputPath)) {
    console.log(`  Clearing existing output directory: ${outputPath}`);
    rmSync(outputPath, { recursive: true, force: true });
  }
  mkdirSync(outputPath, { recursive: true });
}

/**
 * Generate SDK for a specific language
 */
function generateSDK(specPath, generator) {
  const outputPath = resolve(projectRoot, 'sdks', generator.outputDir);
  
  console.log(`\n📦 Generating ${generator.name} SDK...`);
  console.log(`   Generator: ${generator.generator}`);
  console.log(`   Output: ${outputPath}`);
  
  // Clear output directory
  clearOutputDir(outputPath);
  
  // Build the command
  const additionalProps = formatAdditionalProperties(generator.additionalProperties);
  const command = [
    'npx',
    '@openapitools/openapi-generator-cli',
    'generate',
    `-i "${specPath}"`,
    `-g ${generator.generator}`,
    `-o "${outputPath}"`,
    `--additional-properties="${additionalProps}"`,
    '--skip-validate-spec'
  ].join(' ');
  
  try {
    execSync(command, {
      stdio: 'inherit',
      cwd: projectRoot,
      env: { ...process.env }
    });
    console.log(`✅ ${generator.name} SDK generated successfully`);
    return true;
  } catch (error) {
    console.error(`❌ Failed to generate ${generator.name} SDK`);
    console.error(`   Error: ${error.message}`);
    return false;
  }
}

/**
 * Main execution
 */
function main() {
  console.log('🚀 SDK Factory - Multi-language SDK Generator\n');
  
  // Get spec path from CLI argument or environment variable
  const cliArg = process.argv[2];
  const envSpec = process.env.OPENAPI_SPEC;
  
  let specPath = cliArg || envSpec;
  let resolvedSpecPath = null;
  
  // If a path was provided, use it
  if (specPath) {
    resolvedSpecPath = resolve(projectRoot, specPath);
    console.log(`📄 OpenAPI Spec: ${specPath}`);
    console.log(`   Resolved: ${resolvedSpecPath}\n`);
    
    // Check if the provided path exists
    if (!existsSync(resolvedSpecPath)) {
      console.warn(`⚠️  Warning: Provided spec file not found: ${resolvedSpecPath}`);
      console.log(`   Attempting to auto-detect spec file in ./openapi/ directory...\n`);
      resolvedSpecPath = null; // Will trigger auto-detection below
    }
  }
  
  // Auto-detect spec file if not provided or not found
  if (!resolvedSpecPath) {
    const openapiDir = resolve(projectRoot, 'openapi');
    const detectedPath = detectSpecFile(openapiDir);
    
    if (detectedPath) {
      resolvedSpecPath = detectedPath;
      specPath = './' + relative(projectRoot, detectedPath).replace(/\\/g, '/');
      console.log(`📄 Auto-detected OpenAPI Spec: ${specPath}`);
      console.log(`   Resolved: ${resolvedSpecPath}\n`);
    } else {
      console.error(`❌ Error: Could not find OpenAPI spec file.`);
      console.error(`   Searched in: ${openapiDir}`);
      console.error(`   Supported formats: .yml, .yaml, .json`);
      console.error(`   Please place your OpenAPI spec file in the ./openapi/ directory,`);
      console.error(`   or specify the path explicitly:`);
      console.error(`     pnpm generate-sdks ./openapi/your-spec.yaml`);
      process.exit(1);
    }
  }
  
  console.log(`✅ Spec file found\n`);
  console.log(`📋 Generating SDKs for ${generators.length} languages...\n`);
  
  // Generate SDKs for all languages
  const results = generators.map(gen => ({
    generator: gen,
    success: generateSDK(resolvedSpecPath, gen)
  }));
  
  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 Generation Summary');
  console.log('='.repeat(60));
  
  const successful = results.filter(r => r.success).length;
  const failed = results.filter(r => !r.success).length;
  
  results.forEach(({ generator, success }) => {
    const status = success ? '✅' : '❌';
    console.log(`${status} ${generator.name.padEnd(12)} → ./sdks/${generator.outputDir}`);
  });
  
  console.log('='.repeat(60));
  console.log(`Total: ${results.length} | Successful: ${successful} | Failed: ${failed}`);
  console.log('='.repeat(60) + '\n');
  
  // Exit with error if any generation failed
  if (failed > 0) {
    console.error('❌ Some SDKs failed to generate. Please check the errors above.');
    process.exit(1);
  }
  
  console.log('🎉 All SDKs generated successfully!');
}

// Run main function
main();

