# Performance Optimization Guide

Techniques and best practices for optimizing Remotion video composition performance.

## Rendering Performance Targets

**Target Frame Time @ 30fps:** 33ms
**Target Frame Time @ 60fps:** 16.7ms

If actual frame time > target, you'll miss frames and the video may not play smoothly.

## Profiling

### Chrome DevTools

1. Open `http://localhost:3000` in Chrome
2. Open DevTools (F12)
3. Go to Performance tab
4. Record timeline while video plays
5. Look for frames taking > 33ms

### Remotion Profiler

Built-in profiler to identify bottlenecks:

```typescript
import { useLayoutEffect } from 'react';

export const Component: React.FC = () => {
  useLayoutEffect(() => {
    console.time('Component Render');
    return () => console.timeEnd('Component Render');
  }, []);

  return <div>Content</div>;
};
```

## Optimization Techniques

### 1. Use Native Transforms

**Slow - avoid:**
```typescript
<div style={{ position: 'relative', left: `${x}px` }}>
```

**Fast - prefer:**
```typescript
<div style={{ transform: `translateX(${x}px)` }}>
```

Native transforms:
- `translate(x, y)` - Move element
- `scale(x)` - Resize element
- `rotate(angle)` - Rotate element
- `skew(x, y)` - Skew element

### 2. Memoize Components

Prevent unnecessary re-renders:

```typescript
import { memo } from 'react';

export const ExpensiveComponent = memo(() => {
  // This only re-renders if props change
  return <div>Expensive render</div>;
});
```

### 3. Pre-render Expensive Assets

Render once, reuse multiple times:

```typescript
// Render once to file, then use as image
<Img src="prerendered-animation.png" />

// Instead of:
<ComplexAnimation /> // Rendered every frame
```

### 4. Lazy Load Components

Only render visible content:

```typescript
export const LongVideo: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={150}>
        <Intro />
      </Sequence>

      {/* Only renders frames 150-450 */}
      <Sequence from={150} durationInFrames={300}>
        <MainContent />
      </Sequence>
    </>
  );
};
```

### 5. Optimize Images

**Image format recommendations:**
- **Stills:** WebP (best compression), PNG (transparency), JPG (photos)
- **Animated:** MP4 > GIF > PNG sequence
- **Max resolution:** Match video resolution (1920x1080 for Full HD)
- **File size:** <5MB per image, ideally <2MB

**Optimization tools:**
```bash
# Convert to WebP
ffmpeg -i image.jpg -c:v libwebp -q:v 80 image.webp

# Compress PNG
pngquant image.png --ext .png --force

# Reduce resolution
ffmpeg -i image.jpg -vf scale=1920:1080 image_scaled.jpg
```

### 6. Reduce Animation Complexity

**Slow - many moving parts:**
```typescript
// 100 animated elements
{Array.from({ length: 100 }).map((_, i) => (
  <AnimatedBox key={i} index={i} />
))}
```

**Fast - simpler animation:**
```typescript
// Animate container, not children
<div style={{ transform: `translateX(${x}px)` }}>
  {/* Static children */}
</div>
```

### 7. Use Canvas for Complex Graphics

For very complex graphics, use canvas instead of DOM:

```typescript
import { useRef, useEffect } from 'react';

export const CanvasAnimation: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d')!;
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }, []);

  return <canvas ref={canvasRef} style={{ width: '100%', height: '100%' }} />;
};
```

### 8. Limit Concurrent Animations

Only animate what's visible:

```typescript
export const Component: React.FC = () => {
  const frame = useCurrentFrame();

  // Only animate if in view
  if (frame < START_FRAME || frame > END_FRAME) {
    return null; // Don't render
  }

  return <AnimatedElement frame={frame} />;
};
```

### 9. Disable Shadow/Blur Effects

Heavy effects impact performance:

**Slow:**
```typescript
style={{
  boxShadow: '0 10px 30px rgba(0,0,0,0.3)',
  filter: 'blur(10px)',
}}
```

**Better:**
```typescript
// Pre-render shadow as image
<Img src="element-with-shadow.png" />
```

### 10. Optimize Fonts

Large font files impact performance:

```typescript
// Load only necessary weights/sizes
import '@fontsource/inter/400.css'; // 400 weight only

// Use system fonts when possible
fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
```

## Batch Rendering Optimization

### Use Concurrency

Parallel rendering speeds up batch operations:

```bash
# Render 4 videos in parallel
remotion render src/index.tsx MyComposition \
  --concurrency 4 \
  --outName="output-{composition-{}.mp4"
```

**Recommended values:**
- Single video: 4-8 workers
- Batch rendering: 2-4 workers (prevent system overload)
- GPU available: increase to 8-12 workers

### Use Checkpointing

For long renders, enable frame checkpointing:

```bash
remotion render src/index.tsx MyComposition \
  --outName="output.mp4" \
  --concurrency 4 \
  --dump-to "/tmp/remotion-cache"
```

## Memory Management

### Monitor Memory Usage

Check peak memory during rendering:

```bash
# Linux/Mac
watch -n 1 'ps aux | grep remotion'

# Windows
tasklist | find "node"
```

### Reduce Memory Footprint

```typescript
// Bad - keeps all 1000 items in memory
const items = Array.from({ length: 1000 }).map((_, i) => (
  <Item key={i} />
));

// Good - only render visible items
const visibleItems = items.slice(startIndex, endIndex);
```

### Use Streaming for Large Datasets

For large data sets, process in chunks:

```typescript
export const DataVisualization: React.FC = () => {
  const frame = useCurrentFrame();

  // Process data in chunks
  const chunkIndex = Math.floor(frame / 30);
  const dataChunk = getAllData().slice(chunkIndex * 100, (chunkIndex + 1) * 100);

  return <Chart data={dataChunk} />;
};
```

## GPU Acceleration

### Enable Hardware Acceleration

**macOS:**
```bash
remotion render src/index.tsx MyComposition \
  --outName="output.mp4" \
  --video-bitrate 10m
```

**Linux (with NVIDIA GPU):**
```bash
# Use NVIDIA encoding
remotion render src/index.tsx MyComposition \
  --outName="output.mp4" \
  --codec h264_nvenc
```

### Monitor GPU Usage

```bash
# NVIDIA GPU
nvidia-smi

# AMD GPU
rocm-smi
```

## Benchmark Results

Typical performance on modern hardware (2023 MacBook Pro M2):

**Simple composition (static text):**
- Frame time: 2-5ms
- Memory: 200MB
- 30fps achievable: ✓

**Complex composition (50 animated elements):**
- Frame time: 18-25ms
- Memory: 400MB
- 30fps achievable: ✓

**Very complex (200+ elements, 3D transforms):**
- Frame time: 40-60ms
- Memory: 800MB+
- 30fps achievable: ✗ (consider optimization)

## Optimization Checklist

- [ ] Profile with Chrome DevTools
- [ ] Replace CSS animations with transforms
- [ ] Memoize expensive components
- [ ] Use lazy loading with Sequence
- [ ] Optimize image formats and sizes
- [ ] Limit concurrent animations
- [ ] Pre-render expensive assets
- [ ] Use canvas for complex graphics
- [ ] Monitor memory usage
- [ ] Test on target hardware
- [ ] Use appropriate concurrency for batch renders
- [ ] Consider GPU acceleration

## Tools

- **Chrome DevTools** - Performance profiling
- **Remotion CLI** - Built-in performance metrics
- **Activity Monitor** (Mac) / Task Manager (Windows) - System monitoring
- **GPU monitoring** - nvidia-smi, rocm-smi, Activity Monitor

## Resources

- [Remotion Performance Guide](https://www.remotion.dev/docs/performance)
- [Chrome DevTools Performance](https://developer.chrome.com/docs/devtools/performance/)
- [Web Performance APIs](https://developer.mozilla.org/en-US/docs/Web/API/Performance)
