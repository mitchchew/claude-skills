#!/usr/bin/env python3
"""
Remotion project scaffolder - Creates production-ready Remotion projects with TypeScript setup.
"""

import json
import os
import sys
import argparse
from pathlib import Path


def create_package_json(project_name: str, template: str) -> dict:
    """Generate package.json for Remotion project."""
    return {
        "name": project_name,
        "version": "1.0.0",
        "description": "Remotion video project",
        "scripts": {
            "start": "remotion preview src/index.tsx",
            "build": "remotion render src/index.tsx --outName=\"./out.mp4\"",
            "test": "vitest",
            "lint": "eslint src --ext .ts,.tsx",
            "format": "prettier --write src"
        },
        "dependencies": {
            "remotion": "^4.0.0",
            "react": "^18.0.0",
            "react-dom": "^18.0.0"
        },
        "devDependencies": {
            "@types/node": "^20.0.0",
            "@types/react": "^18.0.0",
            "@types/react-dom": "^18.0.0",
            "@typescript-eslint/eslint-plugin": "^6.0.0",
            "@typescript-eslint/parser": "^6.0.0",
            "eslint": "^8.0.0",
            "prettier": "^3.0.0",
            "typescript": "^5.0.0",
            "vitest": "^0.34.0"
        }
    }


def create_tsconfig() -> dict:
    """Generate tsconfig.json."""
    return {
        "compilerOptions": {
            "target": "ES2020",
            "lib": ["ES2020", "DOM"],
            "jsx": "react-jsx",
            "module": "ESNext",
            "moduleResolution": "node",
            "strict": True,
            "esModuleInterop": True,
            "skipLibCheck": True,
            "forceConsistentCasingInFileNames": True,
            "resolveJsonModule": True,
            "declaration": True,
            "declarationMap": True,
            "sourceMap": True
        },
        "include": ["src"],
        "exclude": ["node_modules", "dist"]
    }


def create_eslintrc() -> dict:
    """Generate .eslintrc.json."""
    return {
        "parser": "@typescript-eslint/parser",
        "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
        "env": {
            "browser": True,
            "es2021": True,
            "node": True
        },
        "parserOptions": {
            "ecmaVersion": "latest",
            "sourceType": "module"
        },
        "rules": {
            "no-unused-vars": "off",
            "@typescript-eslint/no-unused-vars": ["error", {"argsIgnorePattern": "^_"}]
        }
    }


def create_prettierrc() -> dict:
    """Generate .prettierrc."""
    return {
        "semi": True,
        "trailingComma": "es5",
        "singleQuote": True,
        "printWidth": 80,
        "tabWidth": 2,
        "useTabs": False
    }


def create_gitignore() -> str:
    """Generate .gitignore content."""
    return """node_modules/
dist/
out/
*.log
.DS_Store
.env
.env.local
.vscode/
.idea/
*.swp
*.swo
*~
build/
coverage/
"""


def create_dockerfile() -> str:
    """Generate Dockerfile."""
    return """FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run build

CMD ["npm", "start"]
"""


def create_github_workflow() -> str:
    """Generate GitHub Actions workflow for rendering."""
    return """name: Render Video

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  render:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v3
        with:
          name: video
          path: out.mp4
"""


def create_basic_composition() -> str:
    """Generate basic composition component."""
    return '''import { Composition } from 'remotion';

export const BasicComposition: React.FC = () => {
  return (
    <div style={{
      flex: 1,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontSize: 100,
      backgroundColor: '#1f1f1f',
      color: 'white',
    }}>
      Hello, Remotion!
    </div>
  );
};

export const compositions: Composition[] = [
  {
    id: 'basic',
    component: BasicComposition,
    durationInFrames: 150,
    fps: 30,
    width: 1920,
    height: 1080,
  },
];
'''


def create_index_tsx() -> str:
    """Generate src/index.tsx entry point."""
    return '''import { Composition } from 'remotion';
import { BasicComposition } from './Composition';

export const MyComposition = () => {
  return (
    <>
      <Composition
        id="BasicComposition"
        component={BasicComposition}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
'''


def create_readme(project_name: str) -> str:
    """Generate README.md."""
    return f"""# {project_name}

A Remotion video project.

## Getting Started

### Installation

```bash
npm install
```

### Development

Start the preview server:

```bash
npm start
```

### Build

Render the video:

```bash
npm run build
```

The video will be output to `out.mp4`.

### Testing

Run tests:

```bash
npm test
```

### Linting

Check code style:

```bash
npm run lint
```

Format code:

```bash
npm run format
```

## Project Structure

```
src/
├── index.tsx           # Entry point
├── Composition.tsx     # Main video composition
└── styles.css         # Global styles
```

## Resources

- [Remotion Docs](https://www.remotion.dev)
- [API Reference](https://www.remotion.dev/api)

## License

MIT
"""


def scaffold_project(project_name: str, template: str = 'basic', typescript: bool = True, testing: bool = True, docker: bool = False) -> dict:
    """Create a new Remotion project."""
    project_path = Path(project_name)

    if project_path.exists():
        return {
            'success': False,
            'error': f'Directory "{project_name}" already exists',
            'path': str(project_path)
        }

    try:
        # Create directory structure
        project_path.mkdir(parents=True)
        (project_path / 'src').mkdir()
        (project_path / 'public').mkdir()

        # Create configuration files
        (project_path / 'package.json').write_text(
            json.dumps(create_package_json(project_name, template), indent=2)
        )
        (project_path / 'tsconfig.json').write_text(
            json.dumps(create_tsconfig(), indent=2)
        )
        (project_path / '.eslintrc.json').write_text(
            json.dumps(create_eslintrc(), indent=2)
        )
        (project_path / '.prettierrc').write_text(
            json.dumps(create_prettierrc(), indent=2)
        )
        (project_path / '.gitignore').write_text(create_gitignore())
        (project_path / 'README.md').write_text(create_readme(project_name))

        # Create source files
        (project_path / 'src' / 'index.tsx').write_text(create_index_tsx())
        (project_path / 'src' / 'Composition.tsx').write_text(create_basic_composition())

        # Optional: Docker
        if docker:
            (project_path / 'Dockerfile').write_text(create_dockerfile())

        # Optional: GitHub Actions
        github_path = project_path / '.github' / 'workflows'
        github_path.mkdir(parents=True, exist_ok=True)
        (github_path / 'render.yml').write_text(create_github_workflow())

        return {
            'success': True,
            'project': project_name,
            'path': str(project_path.absolute()),
            'template': template,
            'typescript': typescript,
            'testing': testing,
            'docker': docker,
            'next_steps': [
                f'cd {project_name}',
                'npm install',
                'npm start',
            ]
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'project': project_name
        }


def main():
    parser = argparse.ArgumentParser(
        description='Create a production-ready Remotion project'
    )
    parser.add_argument('project_name', help='Name of the project')
    parser.add_argument(
        '--template',
        choices=['basic', 'advanced', 'full'],
        default='basic',
        help='Project template (default: basic)'
    )
    parser.add_argument(
        '--typescript',
        action='store_true',
        default=True,
        help='Include TypeScript (default: true)'
    )
    parser.add_argument(
        '--testing',
        action='store_true',
        default=True,
        help='Include testing setup (default: true)'
    )
    parser.add_argument(
        '--docker',
        action='store_true',
        help='Include Docker configuration'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    result = scaffold_project(
        args.project_name,
        template=args.template,
        typescript=args.typescript,
        testing=args.testing,
        docker=args.docker
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result['success']:
            print(f"✓ Created project: {result['project']}")
            print(f"  Path: {result['path']}")
            print("\n  Next steps:")
            for step in result['next_steps']:
                print(f"    {step}")
        else:
            print(f"✗ Error: {result['error']}")
            sys.exit(1)


if __name__ == '__main__':
    main()
