#!/usr/bin/env node
import { chmod, mkdir, writeFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const projectRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const binDir = join(projectRoot, ".hugo-bin");
const tailwindCli = join(
  projectRoot,
  "node_modules",
  "@tailwindcss",
  "cli",
  "dist",
  "index.mjs",
);
const tailwindWrapper = join(binDir, "tailwindcss");

await mkdir(binDir, { recursive: true });
await writeFile(
  tailwindWrapper,
  `#!/usr/bin/env node\nimport ${JSON.stringify(pathToFileURL(tailwindCli).href)};\n`,
);
await chmod(tailwindWrapper, 0o755);

const args = process.argv.slice(2);
const hugoArgs = args.length > 0 ? args : ["server", "--disableFastRender"];
const child = spawn("hugo", hugoArgs, {
  cwd: projectRoot,
  env: {
    ...process.env,
    PATH: `${binDir}:${process.env.PATH ?? ""}`,
  },
  stdio: "inherit",
});

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
    return;
  }
  process.exit(code ?? 0);
});
