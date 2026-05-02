# Audio/Video Synchronization Guide

Techniques for syncing audio and video in Remotion compositions.

## Basic Audio Embedding

### Audio Component

Simplest way to add audio to your composition:

```typescript
import { Audio } from 'remotion';

export const VideoWithAudio: React.FC = () => {
  return (
    <>
      <Audio src="/path/to/audio.mp3" volume={1} />
      {/* Video content here */}
    </>
  );
};
```

**Audio Props:**
- `src` (required) - Path to audio file
- `volume` - Volume level (0-1, default: 1)
- `muted` - Mute audio (default: false)
- `playbackRate` - Playback speed (default: 1)

### Audio File Formats

Supported formats:
- `.mp3` - Best compatibility
- `.wav` - Lossless quality
- `.aac` - Good compression
- `.m4a` - iTunes format
- `.ogg` - Open format
- `.flac` - High quality

**Recommendations:**
- **Recommended:** MP3 (320kbps)
- **High Quality:** FLAC or WAV
- **Streaming:** AAC (128-256kbps)

## Syncing Animation to Audio

### Getting Audio Frame

Use `useAudioFrame()` to get the current audio sample position:

```typescript
import { useAudioFrame } from 'remotion';

export const AudioSync: React.FC = () => {
  const audioFrame = useAudioFrame();

  // audioFrame = 0 at start of audio
  // audioFrame = duration * sampleRate at end

  return <div>Audio Frame: {audioFrame}</div>;
};
```

### Syncing to Beats

Sync animations to audio beats:

```typescript
import { useAudioFrame, useVideoConfig } from 'remotion';

export const BeatSync: React.FC = () => {
  const audioFrame = useAudioFrame();
  const { fps } = useVideoConfig();

  // Assuming audio is 120 BPM (2 beats per second)
  const beatsPerSecond = 120 / 60;
  const sampleRate = 48000; // Standard audio sample rate
  const audioSeconds = audioFrame / sampleRate;
  const beatCount = audioSeconds * beatsPerSecond;
  const currentBeat = Math.floor(beatCount) % 4; // 0-3 for 4/4 time

  // Animate based on beat
  const scale = currentBeat === 0 ? 1.2 : 1;

  return (
    <div style={{ transform: `scale(${scale})` }}>
      Beat: {currentBeat}
    </div>
  );
};
```

### Detecting Peaks

Detect when audio volume is high:

```typescript
export const PeakDetector: React.FC = () => {
  const audioFrame = useAudioFrame();

  // Simulate peak detection
  // In real scenario, you'd analyze audio data
  const isPeak = Math.sin(audioFrame / 1000) > 0.5;

  return (
    <div style={{
      backgroundColor: isPeak ? '#ff0000' : '#00ff00'
    }}>
      {isPeak ? 'PEAK' : 'Normal'}
    </div>
  );
};
```

## Timing Audio Tracks

### Multiple Audio Tracks

Layer multiple audio files:

```typescript
import { Audio, Sequence } from 'remotion';

export const MultiAudio: React.FC = () => {
  return (
    <>
      {/* Main audio throughout */}
      <Audio src="/audio/background.mp3" volume={0.5} />

      {/* Intro sound only first 5 seconds */}
      <Sequence from={0} durationInFrames={150}>
        <Audio src="/audio/intro.mp3" volume={1} />
      </Sequence>

      {/* Outro sound last 3 seconds */}
      <Sequence from={1620} durationInFrames={90}>
        <Audio src="/audio/outro.mp3" volume={1} />
      </Sequence>
    </>
  );
};
```

### Audio Volume Animation

Fade audio in and out:

```typescript
import { Audio, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

export const FadingAudio: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Fade in first 30 frames, fade out last 30 frames
  const volume = interpolate(
    frame,
    [0, 30, durationInFrames - 30, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return <Audio src="/audio/track.mp3" volume={volume} />;
};
```

## Text Subtitle Sync

### Static Subtitles

Simple subtitle display:

```typescript
interface SubtitleProps {
  startFrame: number;
  endFrame: number;
  text: string;
}

export const Subtitle: React.FC<SubtitleProps> = ({ startFrame, endFrame, text }) => {
  const frame = useCurrentFrame();

  if (frame < startFrame || frame > endFrame) {
    return null;
  }

  return (
    <div style={{
      position: 'absolute',
      bottom: 40,
      left: 0,
      right: 0,
      textAlign: 'center',
      color: '#fff',
      fontSize: 24,
      fontWeight: 'bold',
      textShadow: '2px 2px 4px rgba(0,0,0,0.7)',
    }}>
      {text}
    </div>
  );
};

// Usage
export const VideoWithSubtitles: React.FC = () => {
  return (
    <>
      <Audio src="/audio/narration.mp3" />

      {/* Intro */}
      <Subtitle startFrame={0} endFrame={150} text="Welcome to our video" />

      {/* Main content */}
      <Subtitle startFrame={150} endFrame={300} text="Here's the main point" />

      {/* Outro */}
      <Subtitle startFrame={300} endFrame={450} text="Thanks for watching" />
    </>
  );
};
```

### Timed Subtitle List

Load subtitles from data:

```typescript
interface SubtitleEntry {
  startTime: number; // seconds
  endTime: number;
  text: string;
}

interface SubtitlesProps {
  subtitles: SubtitleEntry[];
  fps: number;
}

export const Subtitles: React.FC<SubtitlesProps> = ({ subtitles, fps }) => {
  const frame = useCurrentFrame();
  const seconds = frame / fps;

  const currentSubtitle = subtitles.find(
    (sub) => seconds >= sub.startTime && seconds < sub.endTime
  );

  return (
    <div style={{
      position: 'absolute',
      bottom: 40,
      left: 0,
      right: 0,
      textAlign: 'center',
      color: '#fff',
      fontSize: 24,
      minHeight: 60,
    }}>
      {currentSubtitle?.text}
    </div>
  );
};
```

## Narration Sync

### Voice-Over Timing

Sync text appearance to narration:

```typescript
import { Audio, useAudioFrame, useVideoConfig } from 'remotion';

interface Narration {
  text: string;
  startTime: number; // seconds
  endTime: number;
}

export const NarrationVideo: React.FC = () => {
  const audioFrame = useAudioFrame();
  const { fps } = useVideoConfig();
  const sampleRate = 48000;
  const audioSeconds = audioFrame / sampleRate;

  const narrations: Narration[] = [
    { text: "First sentence", startTime: 0, endTime: 2 },
    { text: "Second sentence", startTime: 2, endTime: 4 },
    { text: "Third sentence", startTime: 4, endTime: 6 },
  ];

  const currentNarration = narrations.find(
    (n) => audioSeconds >= n.startTime && audioSeconds < n.endTime
  );

  return (
    <>
      <Audio src="/audio/narration.mp3" />

      <div style={{
        flex: 1,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 48,
        color: '#fff',
      }}>
        {currentNarration?.text}
      </div>
    </>
  );
};
```

## Music Beat Sync

### BPM-Based Timing

Calculate beat timing from audio:

```typescript
export const BeatTiming = {
  /**
   * Get beat number at current audio frame
   * @param audioFrame - Current audio sample position
   * @param bpm - Beats per minute of the track
   * @param sampleRate - Audio sample rate (default: 48000)
   */
  getBeatNumber(audioFrame: number, bpm: number, sampleRate = 48000): number {
    const audioSeconds = audioFrame / sampleRate;
    const beatsPerSecond = bpm / 60;
    return audioSeconds * beatsPerSecond;
  },

  /**
   * Check if on a beat
   * @param audioFrame - Current audio sample position
   * @param bpm - Beats per minute
   * @param tolerance - How close to beat (0-1, default: 0.1)
   */
  isBeat(
    audioFrame: number,
    bpm: number,
    tolerance = 0.1,
    sampleRate = 48000
  ): boolean {
    const beatNumber = this.getBeatNumber(audioFrame, bpm, sampleRate);
    const beatFraction = beatNumber - Math.floor(beatNumber);
    return beatFraction < tolerance || beatFraction > 1 - tolerance;
  },

  /**
   * Get beat progress (0-1)
   * @param audioFrame - Current audio sample position
   * @param bpm - Beats per minute
   */
  getBeatProgress(audioFrame: number, bpm: number, sampleRate = 48000): number {
    const beatNumber = this.getBeatNumber(audioFrame, bpm, sampleRate);
    return beatNumber - Math.floor(beatNumber);
  },
};

// Usage
export const MusicSync: React.FC = () => {
  const audioFrame = useAudioFrame();
  const bpm = 120; // Track BPM

  const beatNumber = BeatTiming.getBeatNumber(audioFrame, bpm);
  const beatProgress = BeatTiming.getBeatProgress(audioFrame, bpm);
  const isBeat = BeatTiming.isBeat(audioFrame, bpm);

  // Pulse on beat
  const scale = isBeat ? 1.1 : 1;

  return (
    <div style={{
      transform: `scale(${scale})`,
      transition: 'transform 0.05s',
    }}>
      Beat {Math.floor(beatNumber)}
    </div>
  );
};
```

## Audio Analysis

### Getting Audio Duration

```typescript
async function getAudioDuration(audioPath: string): Promise<number> {
  const audio = new Audio();
  return new Promise((resolve) => {
    audio.src = audioPath;
    audio.onloadedmetadata = () => {
      resolve(audio.duration);
    };
  });
}

// Usage
const duration = await getAudioDuration('/audio/track.mp3');
const durationFrames = Math.ceil(duration * 30); // @ 30fps
```

### Visual Audio Analysis

Create a waveform visualization:

```typescript
export const Waveform: React.FC<{ audioPath: string }> = ({ audioPath }) => {
  // In real implementation, would analyze audio data
  const audioFrame = useAudioFrame();
  const sampleRate = 48000;

  // Simulate waveform
  const value = Math.sin((audioFrame / sampleRate) * Math.PI * 4) * 50 + 50;

  return (
    <div style={{
      width: '100%',
      height: `${value}%`,
      backgroundColor: '#0066ff',
    }} />
  );
};
```

## Best Practices

### 1. Always Test Sync

- Test audio/video sync during development
- Use a reference monitor to verify timing
- Check on different playback speeds
- Verify on final export quality

### 2. Account for Processing Delay

Audio may have slight delays. Add offset if needed:

```typescript
const AUDIO_DELAY_MS = 50; // 50ms delay
const audioFrame = useAudioFrame() + (AUDIO_DELAY_MS / 1000) * 48000;
```

### 3. Use High-Quality Audio

- Record narration in quiet environment
- Use consistent audio level
- Export as high quality (320kbps MP3 or lossless)

### 4. Compress Audio Before Export

Smaller audio files render faster:

```bash
ffmpeg -i audio.wav -c:a libmp3lame -b:a 192k audio.mp3
```

### 5. Test with Target System

Sync can vary based on system load. Test on:
- Development machine
- CI/CD pipeline
- Target playback device

## Troubleshooting

**Audio not playing:**
- Check file path and format
- Verify audio codec is supported
- Check browser console for errors

**Audio/video out of sync:**
- Verify frame rate matches audio sample rate
- Check for processing delays
- Use `useAudioFrame()` for precise sync

**Audio cuts off:**
- Check composition duration matches audio length
- Ensure `<Audio>` component is within composition bounds

**Memory issues:**
- Large audio files load into memory
- Consider splitting long audio
- Use streaming for live audio

## Resources

- [Remotion Audio API](https://www.remotion.dev/docs/audio)
- [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- [FFmpeg Audio Guide](https://ffmpeg.org/ffmpeg-codecs.html#Audio-Codecs)
