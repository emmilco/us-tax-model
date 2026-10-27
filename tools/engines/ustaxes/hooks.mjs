// Module hooks that let Node run UsTaxes' TypeScript sources as shipped, without its build.
//
// UsTaxes is a React application; its tax logic lives in src/ as TypeScript that imports types
// without `import type`, so Node's own type stripping cannot load it. These hooks:
//   resolve  'ustaxes/*' -> <USTAXES_SRC>/src/*; extensionless relative imports -> .ts, .tsx, .js or
//            index.ts; the bare runtime packages (lodash, loglevel) -> <USTAXES_DEPS>/node_modules
//   load     .ts/.tsx files under <USTAXES_SRC> -> ES modules transpiled by the TypeScript compiler
//            pinned in UsTaxes' package-lock (transpileModule elides type-only imports and compiles
//            enums); nothing is type-checked and no file is written
// Used only by run.mjs beside this file, under `node --no-experimental-strip-types --import`.
import { registerHooks, createRequire } from 'node:module'
import { existsSync, statSync, readFileSync } from 'node:fs'
import { pathToFileURL, fileURLToPath } from 'node:url'
import path from 'node:path'

const ROOT = process.env.USTAXES_SRC
const DEPS = process.env.USTAXES_DEPS
if (!ROOT || !DEPS) throw new Error('USTAXES_SRC and USTAXES_DEPS must be set')
const SRC = path.join(ROOT, 'src') + path.sep

const tryFile = (p) => {
  for (const c of [p, p + '.ts', p + '.tsx', p + '.js', path.join(p, 'index.ts'), path.join(p, 'index.js')])
    if (existsSync(c) && statSync(c).isFile()) return c
  return null
}

registerHooks({
  resolve(spec, ctx, next) {
    let target = null
    if (spec.startsWith('ustaxes/')) target = tryFile(path.join(SRC, spec.slice('ustaxes/'.length)))
    else if ((spec === '.' || spec === '..' || spec.startsWith('./') || spec.startsWith('../')) && ctx.parentURL?.startsWith('file:')
             && fileURLToPath(ctx.parentURL).startsWith(SRC))
      target = tryFile(path.resolve(path.dirname(fileURLToPath(ctx.parentURL)), spec))
    if (target) return { url: pathToFileURL(target).href, shortCircuit: true }
    if (spec === 'lodash' || spec === 'loglevel')
      return next(spec, { ...ctx, parentURL: pathToFileURL(path.join(DEPS, 'x.js')).href })
    return next(spec, ctx)
  }
})

const ts = createRequire(path.join(DEPS, 'x.js'))('typescript')
registerHooks({
  load(url, ctx, next) {
    if (url.startsWith('file:') && /\.tsx?$/.test(url) && fileURLToPath(url).startsWith(SRC)) {
      const file = fileURLToPath(url)
      const out = ts.transpileModule(readFileSync(file, 'utf8'), {
        fileName: file,
        compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2020, esModuleInterop: true, jsx: ts.JsxEmit.ReactJSX }
      })
      return { format: 'module', source: out.outputText, shortCircuit: true }
    }
    return next(url, ctx)
  }
})
