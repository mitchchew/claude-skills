---
name: "remotion-dev"
description: Remotion development toolkit for creating videos programmatically with React. Includes project scaffolding, composition templates, video export automation, performance optimization, and best practices. Use for video generation pipelines, dynamic content creation, animated explainers, and automated video rendering.
---

# Remotion Development Toolkit

Production-ready tools for building, optimizing, and rendering videos programmatically using React and Remotion.

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Tools](#tools)
  - [Project Scaffolder](#project-scaffolder)
  - [Composition Template Generator](#composition-template-generator)
  - [Video Render Pipeline](#video-render-pipeline)
  - [Performance Analyzer](#performance-analyzer)
  - [Asset Manager](#asset-manager)
- [Workflow Recipes](#workflow-recipes)
- [Best Practices](#best-practices)
- [Reference Guides](#reference-guides)

---

## Overview

Remotion is a library for creating videos programmatically with React. This skill provides production-ready automation, project templates, and optimization tools for building scalable video generation pipelines.

**Key Capabilities:**
- Project scaffolding with TypeScript + Remotion setup
- Composition templates for common video patterns
- Batch rendering and video export automation
- Performance monitoring and optimization
- Asset management and optimization
- Dynamic content rendering from data sources

---

## Quick Start

### 1. Scaffold a New Project

```bash
python scripts/project_scaffolder.py my-video-app --template basic
cd my-video-app
npm install
npm start
```

### 2. Generate Your First Composition

```bash
python scripts/template_generator.py --type explainer --output src/Explainer.tsx
```

### 3. Render to Video

```bash
python scripts/render_pipeline.py --composition Explainer --output output.mp4 --codec h264
```

---

## Tools

### Project Scaffolder

Creates production-ready Remotion projects with TypeScript, ESLint, Prettier, and testing infrastructure.

**Usage:**
```bash
python scripts/project_scaffolder.py <project-name> [options]

# Options:
#   --template [basic|advanced|full]  Project template (default: basic)
#   --typescript                      Include TypeScript (default: true)
#   --testing                         Include testing setup (default: true)
#   --docker                          Include Docker configuration (default: false)
```

**Creates:**
```
my-video-app/
├── src/
│   ├── Composition.tsx          # Main video composition
│   ├── index.tsx                # Entry point
│   └── styles.css
├── public/
├── package.json
├── tsconfig.json
├── .eslintrc.json
├── .prettierrc
├── Dockerfile                   # Optional
└── README.md
```

**Features:**
- TypeScript strict mode
- ESLint + Prettier configuration
- Vitest + React Testing Library setup
- GitHub Actions CI/CD for renders
- Hot module reloading
- Production-optimized build

---

### Composition Template Generator

Generates ready-to-use React composition templates for common video patterns.

**Usage:**
```bash
python scripts/template_generator.py --type <type> [options]

# Template Types:
#   - basic           Simple intro sequence
#   - explainer       2-3 minute explainer video
#   - product-demo    Product feature showcase
#   - testimonial     User testimonial format
#   - animation       Custom animation template
#   - slideshow       Image/content slideshow
#   - title-sequence  Movie-style opening
#   - data-viz        Data visualization animation
```

**Example: Generate Explainer Template**
```bash
python scripts/template_generator.py --type explainer \
  --output src/Explainer.tsx \
  --duration 180 \
  --fps 30
```

**Output Includes:**
- Scene transitions
- Text animations
- Music/audio sync points
- Placeholder assets
- Keyframe timing structure

---

### Video Render Pipeline

Batch rendering and optimization for video export.

**Usage:**
```bash
python scripts/render_pipeline.py [options]

# Options:
#   --composition NAME              Composition to render
#   --output FILE                   Output file path
#   --codec [h264|h265|png]         Video codec (default: h264)
#   --quality [low|medium|high]     Export quality (default: high)
#   --fps NUMBER                    Frames per second (default: 30)
#   --width NUMBER                  Video width (default: 1920)
#   --height NUMBER                 Video height (default: 1080)
#   --concurrency NUMBER            Parallel workers (default: 4)
#   --batch FILE                    JSON file with batch config
```

**Batch Rendering Example (batch.json):**
```json
{
  "renders": [
    {
      "composition": "Intro",
      "variables": {"title": "Video 1"},
      "output": "output1.mp4"
    },
    {
      "composition": "Intro",
      "variables": {"title": "Video 2"},
      "output": "output2.mp4"
    }
  ],
  "codec": "h264",
  "quality": "high",
  "concurrency": 2
}
```

**Run Batch:**
```bash
python scripts/render_pipeline.py --batch batch.json
```

**Output:**
```
Render Progress:
✓ Intro [1/2] → output1.mp4 (45s)
✓ Intro [2/2] → output2.mp4 (42s)

Summary:
- Total Duration: 87s
- Average Per Video: 43.5s
- Output Size: 245 MB
- Success Rate: 100%
```

---

### Performance Analyzer

Monitors and optimizes video composition performance.

**Usage:**
```bash
python scripts/performance_analyzer.py <project-path> [options]

# Options:
#   --composition NAME              Analyze specific composition
#   --fps NUMBER                    Target FPS (default: 30)
#   --duration SECONDS              Video duration (default: 60)
#   --report [json|html|text]       Report format (default: text)
```

**Analysis Includes:**
- Frame rendering time per component
- Memory usage throughout video
- GPU utilization
- Animation smoothness
- Asset loading performance
- Optimization recommendations

**Sample Output:**
```
Performance Report: src/Composition.tsx

Frame Render Time: 42ms avg (target: 33ms @ 30fps)
Peak Memory: 512MB
GPU Utilization: 65% avg

Bottlenecks Detected:
1. Image transforms in overlay (12ms)
   → Suggestion: Use native video transforms
2. Complex SVG animations (8ms)
   → Suggestion: Pre-render or use canvas

Recommendations:
- Reduce animation complexity by 20% for 60fps
- Pre-render 3D assets before composition
- Use Remotion's <Sequence /> for lazy loading
```

---

### Asset Manager

Optimizes, validates, and catalogs video assets.

**Usage:**
```bash
python scripts/asset_manager.py <assets-directory> [options]

# Options:
#   --validate                      Check file integrity
#   --optimize                      Auto-compress images
#   --catalog                       Generate asset manifest
#   --output FILE                   Save manifest JSON
#   --formats [jpg,png,mp4,webm]   Supported formats
```

**Asset Validation:**
```bash
python scripts/asset_manager.py ./assets --validate
```

**Output:**
```
Asset Validation Report:
✓ images/logo.png (2048x2048, 145KB) - Optimal
✓ videos/bg.mp4 (1920x1080, 12MB) - Good
⚠ images/banner.jpg (4096x4096, 8MB) - Large, suggest 2048x2048
✗ videos/intro.mov - Unsupported codec, convert to h264

Optimization Suggestions:
1. Optimize 3 PNG files (save ~240KB)
2. Convert MOV to MP4 for better compatibility
3. Resize 2 oversized images (save ~6MB)

Run: python scripts/asset_manager.py ./assets --optimize
```

**Generate Manifest:**
```bash
python scripts/asset_manager.py ./assets --catalog --output manifest.json
```

---

## Workflow Recipes

### Recipe 1: Generate Explainer Videos from Script

Create multiple videos from a data file with different variables:

```bash
# 1. Create base template
python scripts/template_generator.py --type explainer --output src/Explainer.tsx

# 2. Create batch config from script data
cat > batch.json << 'EOF'
{
  "renders": [
    {"composition": "Explainer", "variables": {"title": "Feature A"}, "output": "feature-a.mp4"},
    {"composition": "Explainer", "variables": {"title": "Feature B"}, "output": "feature-b.mp4"},
    {"composition": "Explainer", "variables": {"title": "Feature C"}, "output": "feature-c.mp4"}
  ],
  "codec": "h264",
  "quality": "high"
}
EOF

# 3. Render batch
python scripts/render_pipeline.py --batch batch.json

# 4. Validate output
python scripts/asset_manager.py ./output --validate
```

### Recipe 2: Optimize Render Performance

```bash
# 1. Analyze current performance
python scripts/performance_analyzer.py ./ --duration 60

# 2. Identify bottlenecks
# Review recommendations

# 3. Implement fixes in composition

# 4. Re-analyze to confirm improvement
python scripts/performance_analyzer.py ./ --duration 60 --report html
```

### Recipe 3: Automated Asset Management

```bash
# 1. Validate all assets
python scripts/asset_manager.py ./public/assets --validate

# 2. Optimize assets
python scripts/asset_manager.py ./public/assets --optimize

# 3. Generate manifest for composition
python scripts/asset_manager.py ./public/assets --catalog --output src/assets.json

# 4. Use in composition:
# import assets from './assets.json'
```

---

## Best Practices

### 1. Composition Structure

**Organize compositions hierarchically:**
```typescript
// src/compositions/
├── index.ts                    // Export all compositions
├── Intro.tsx                   // 5-10 second intro
├── MainContent.tsx             // Core animation/content
└── Outro.tsx                   // 3-5 second close

// Use <Sequence /> for timing
<Sequence from={0} durationInFrames={150}>
  <Intro />
</Sequence>

<Sequence from={150} durationInFrames={300}>
  <MainContent />
</Sequence>

<Sequence from={450} durationInFrames={120}>
  <Outro />
</Sequence>
```

### 2. Performance Optimization

**Key techniques:**
- Use native transforms (rotate, scale) instead of CSS
- Pre-render expensive animations
- Lazy-load assets with `<Sequence />`
- Use `memo()` for complex components
- Limit concurrent animations
- Optimize image formats (WebP > PNG for stills)

### 3. Audio Synchronization

**Sync audio to animations:**
```typescript
// Use Remotion's audio-frame utilities
import { useAudioFrame } from 'remotion'

const audioFrame = useAudioFrame() // 0-fps relative
const beat = audioFrame > 480 ? 'drop' : 'build'
```

### 4. Testing Compositions

**Test keyframes and timing:**
```typescript
// vitest example
describe('Intro', () => {
  it('should show title at frame 30', () => {
    const frame = 30
    expect(calculateOpacity(frame)).toBe(1)
  })
})
```

### 5. Rendering Pipeline

**Best practices:**
- Use concurrency sparingly (default: 4 workers)
- Monitor system resources during batch renders
- Implement checkpointing for long renders
- Log all render metadata for analytics
- Use production codec (h264) for final output
- Test render settings on small frames first

---

## Reference Guides

See `references/` directory for:

- **remotion-fundamentals.md** — Core concepts, APIs, composition lifecycle
- **performance-optimization.md** — Profiling, optimization techniques, benchmarks
- **audio-video-sync.md** — Audio/video synchronization patterns and tools
- **advanced-animations.md** — Complex animation techniques, bezier curves, physics
- **deployment.md** — Serverless rendering, CI/CD integration, scaling considerations
- **react-best-practices.md** — React patterns within Remotion, hooks, state management
- **troubleshooting.md** — Common issues, error messages, and solutions

---

## Version Info

- **Remotion Version:** 4.0+
- **Node Version:** 16+
- **React Version:** 18+
- **Supported OS:** macOS, Linux, Windows

---

## Resources

- [Remotion Docs](https://www.remotion.dev)
- [API Reference](https://www.remotion.dev/api)
- [Examples Gallery](https://www.remotion.dev/examples)
- [Community Discord](https://discord.gg/remotion)

---

**Last Updated:** May 2, 2026
**Skill Status:** Production-Ready
**Dependencies:** Node.js 16+, FFmpeg (for rendering)
