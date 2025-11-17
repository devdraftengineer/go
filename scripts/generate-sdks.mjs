#!/usr/bin/env node

/**
 * SDK Generator Script
 * 
 * Generates SDKs for multiple languages from an OpenAPI specification.
 * 
 * Usage:
 *   node ./scripts/generate-sdks.mjs <path-to-openapi-spec>
 * 
 * Examples:
 *   node ./scripts/generate-sdks.mjs ./openapi/api.yaml
 *   node ./scripts/generate-sdks.mjs ./openapi/my-api.yaml
 * 
 * You can also override the default spec path via CLI argument:
 *   pnpm generate-sdks ./openapi/custom-api.yaml
 *   npm run generate-sdks -- ./openapi/custom-api.yaml
 * 
 * Or set OPENAPI_SPEC environment variable:
 *   OPENAPI_SPEC=./openapi/custom-api.yaml pnpm generate-sdks
 */

import { execSync } from 'child_process';
import { existsSync, rmSync, mkdirSync } from 'fs';
import { resolve, dirname } from 'path';
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
  // Get spec path from CLI argument or environment variable or default
  const cliArg = process.argv[2];
  const envSpec = process.env.OPENAPI_SPEC;
  const defaultSpec = './openapi/api.yaml';
  
  const specPath = cliArg || envSpec || defaultSpec;
  const resolvedSpecPath = resolve(projectRoot, specPath);
  
  console.log('🚀 SDK Factory - Multi-language SDK Generator\n');
  console.log(`📄 OpenAPI Spec: ${specPath}`);
  console.log(`   Resolved: ${resolvedSpecPath}\n`);
  
  // Validate spec file exists
  if (!existsSync(resolvedSpecPath)) {
    console.error(`❌ Error: OpenAPI spec file not found: ${resolvedSpecPath}`);
    console.error(`   Please ensure the file exists and the path is correct.`);
    process.exit(1);
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

