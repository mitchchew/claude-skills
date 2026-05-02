# Remotion Fundamentals

Core concepts, APIs, and composition lifecycle for building videos programmatically.

## What is Remotion?

Remotion is a JavaScript/TypeScript library that allows you to create videos using React. Instead of using traditional video editors, you write code that renders to video files.

**Key Benefits:**
- Write videos with JavaScript/React
- Version control videos like code
- Generate videos dynamically from data
- Automate video production
- Test video compositions
- Integrate with CI/CD pipelines

## Core Concepts

### Composition

A composition is a React component that represents your video. It defines the visual content and duration.

```typescript
import { Composition } from 'remotion';

export const MyVideo: React.FC = () => {
  return (
    <div style={{ flex: 1, background: '#000', display: 'flex' }}>
      <h1 style={{ color: '#fff' }}>Hello Remotion</h1>
    </div>
  );
};

// Register composition
export const compositions: Composition[] = [
  {
    id: 'MyVideo',
    component: MyVideo,
    durationInFrames: 150,
    fps: 30,
    width: 1920,
    height: 1080,
  },
];
```

### Frames

Remotion works with frames. Duration is specified in frames, not seconds.

```
Frames = Duration (seconds) × FPS

Examples:
- 5 seconds @ 30fps = 5 × 30 = 150 frames
- 10 seconds @ 60fps = 10 × 60 = 600 frames
```

### Current Frame

The `useCurrentFrame()` hook gives you the current frame number (0-indexed) during rendering.

```typescript
import { useCurrentFrame } from 'remotion';

export const Animation: React.FC = () => {
  const frame = useCurrentFrame();
  
  return (
    <div>
      Current Frame: {frame} / 150
    </div>
  );
};
```

### Video Config

The `useVideoConfig()` hook provides metadata about the composition.

```typescript
import { useVideoConfig } from 'remotion';

export const Component: React.FC = () => {
  const { durationInFrames, fps, width, height } = useVideoConfig();
  
  return (
    <div style={{ width, height }}>
      {/* Component content */}
    </div>
  );
};
```

## Essential APIs

### Sequence

Groups components with timing control. Only content within the duration is rendered.

```typescript
import { Sequence } from 'remotion';

export const Timeline: React.FC = () => {
  return (
    <>
      {/* Render Intro from frame 0-150 */}
      <Sequence from={0} durationInFrames={150}>
        <Intro />
      </Sequence>

      {/* Render Main from frame 150-450 */}
      <Sequence from={150} durationInFrames={300}>
        <MainContent />
      </Sequence>

      {/* Render Outro from frame 450-600 */}
      <Sequence from={450} durationInFrames={150}>
        <Outro />
      </Sequence>
    </>
  );
};
```

### Interpolate

Smoothly animate values between frames.

```typescript
import { interpolate, useCurrentFrame } from 'remotion';

export const ScaleAnimation: React.FC = () => {
  const frame = useCurrentFrame();
  
  // Scale from 0.5 to 1.5 over 150 frames
  const scale = interpolate(frame, [0, 150], [0.5, 1.5]);
  
  return (
    <div style={{ transform: `scale(${scale})` }}>
      Content
    </div>
  );
};
```

**interpolate() Syntax:**
```typescript
interpolate(
  input,              // Current frame
  [inputMin, inputMax], // Input range
  [outputMin, outputMax], // Output range
  { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
)
```

### Spring Animation

Create physics-based animations that feel natural.

```typescript
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const SpringAnimation: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  // Spring animation over 40 frames
  const scale = spring({
    fps,
    frame,
    config: {
      damping: 10,
      mass: 1,
      overshootClamping: false,
      restDisplacementThreshold: 0.001,
      restSpeedThreshold: 0.001,
      stiffness: 100,
      tension: 100,
    },
    durationInFrames: 40,
    delay: 0,
  });
  
  return (
    <div style={{ transform: `scale(${scale})` }}>
      Content
    </div>
  );
};
```

### Img Component

Optimized image rendering with lazy loading support.

```typescript
import { Img } from 'remotion';

export const ImageComponent: React.FC = () => {
  return (
    <Img
      src="/path/to/image.png"
      style={{ width: '100%', height: '100%' }}
    />
  );
};
```

### Audio Component

Embed and sync audio with video.

```typescript
import { Audio, useCurrentFrame, useVideoConfig } from 'remotion';

export const AudioComponent: React.FC = () => {
  return (
    <Audio src="/path/to/audio.mp3" volume={0.5} />
  );
};
```

### Video Component

Embed video files within compositions.

```typescript
import { Video } from 'remotion';

export const VideoComponent: React.FC = () => {
  return (
    <Video src="/path/to/video.mp4" />
  );
};
```

## Composition Lifecycle

1. **Mount** → Component mounts
2. **Render** → Each frame renders (0 to durationInFrames)
3. **Unmount** → Component unmounts after duration

Key behaviors:
- Each frame re-renders the component
- State resets each frame (use `useCurrentFrame()` for animation)
- DOM is never displayed (renders to canvas)
- Side effects should be avoided (no external API calls)

## Best Practices

### 1. Use Functional Components

```typescript
// Good
export const MyComponent: React.FC = () => {
  const frame = useCurrentFrame();
  return <div>{frame}</div>;
};

// Avoid
export class MyComponent extends React.Component {
  render() { /* ... */ }
}
```

### 2. Optimize with useMemo

Memoize expensive calculations.

```typescript
import { useMemo, useCurrentFrame } from 'remotion';

export const Component: React.FC = () => {
  const frame = useCurrentFrame();
  
  const complexValue = useMemo(() => {
    return expensiveCalculation(frame);
  }, [frame]);
  
  return <div>{complexValue}</div>;
};
```

### 3. Use CSS for Simple Styles

```typescript
const styles = {
  container: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
    height: '100%',
  }
};

export const Component: React.FC = () => (
  <div style={styles.container}>
    Content
  </div>
);
```

### 4. Lazy Load with Sequences

Only render what's visible.

```typescript
export const LongVideo: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={150}>
        <Intro />
      </Sequence>
      
      {/* Only renders between frame 150-450 */}
      <Sequence from={150} durationInFrames={300}>
        <HeavyComponent />
      </Sequence>
    </>
  );
};
```

### 5. Avoid Dependencies in Hooks

Hooks run every frame, so avoid creating objects.

```typescript
// Bad - creates new array every frame
const opacity = interpolate(frame, [0, 150], [0, 1]);

// Good - use constants
const START_FRAME = 0;
const END_FRAME = 150;
const opacity = interpolate(frame, [START_FRAME, END_FRAME], [0, 1]);
```

## TypeScript

Add type safety to compositions.

```typescript
interface ComponentProps {
  title: string;
  duration: number;
}

export const TypedComponent: React.FC<ComponentProps> = ({ title, duration }) => {
  const frame = useCurrentFrame();
  
  return <div>{title}</div>;
};
```

## Composition Variables

Pass dynamic data to compositions.

```typescript
export const compositions: Composition[] = [
  {
    id: 'WithVariables',
    component: ComponentWithVariables,
    durationInFrames: 150,
    fps: 30,
    width: 1920,
    height: 1080,
    props: {
      title: 'Dynamic Title',
      subtitle: 'Dynamic Subtitle',
    },
  },
];

interface Props {
  title: string;
  subtitle: string;
}

export const ComponentWithVariables: React.FC<Props> = ({ title, subtitle }) => (
  <div>
    <h1>{title}</h1>
    <h2>{subtitle}</h2>
  </div>
);
```

## Rendering

### Preview Mode

Run locally with hot reload:
```bash
npm start
```

### Render to File

Create a video file:
```bash
remotion render src/index.tsx MyComposition --outName="output.mp4"
```

### Render with Options

```bash
remotion render src/index.tsx MyComposition \
  --outName="output.mp4" \
  --codec h264 \
  --quality high \
  --width 1920 \
  --height 1080 \
  --fps 30 \
  --concurrency 4
```

## Resources

- [Remotion Documentation](https://www.remotion.dev/docs)
- [API Reference](https://www.remotion.dev/api)
- [Examples](https://www.remotion.dev/examples)
- [Community Discord](https://discord.gg/remotion)
