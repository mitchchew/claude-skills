#!/usr/bin/env python3
"""
Remotion composition template generator - Creates templates for common video patterns.
"""

import json
import sys
import argparse
from pathlib import Path


TEMPLATES = {
    'basic': {
        'description': 'Simple intro sequence',
        'duration': 150,
        'content': '''import { useVideoConfig } from 'remotion';

export const BasicIntro: React.FC = () => {
  const { durationInFrames } = useVideoConfig();

  return (
    <div style={{
      flex: 1,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontSize: 48,
      backgroundColor: '#000',
      color: '#fff',
      fontFamily: 'Arial, sans-serif',
    }}>
      <h1>Your Title Here</h1>
    </div>
  );
};
'''
    },
    'explainer': {
        'description': '2-3 minute explainer video template',
        'duration': 5400,
        'content': '''import { Sequence } from 'remotion';

export const Explainer: React.FC = () => {
  return (
    <>
      {/* Hook - 5 seconds */}
      <Sequence from={0} durationInFrames={150}>
        <div style={{
          flex: 1,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          fontSize: 64,
          backgroundColor: '#0066ff',
          color: '#fff',
        }}>
          The Problem
        </div>
      </Sequence>

      {/* Main Content - 90 seconds */}
      <Sequence from={150} durationInFrames={2700}>
        <div style={{
          flex: 1,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          fontSize: 48,
          backgroundColor: '#fff',
          color: '#000',
        }}>
          Solution Details
        </div>
      </Sequence>

      {/* Call to Action - 25 seconds */}
      <Sequence from={2850} durationInFrames={750}>
        <div style={{
          flex: 1,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          fontSize: 56,
          backgroundColor: '#00cc00',
          color: '#fff',
        }}>
          Get Started Now
        </div>
      </Sequence>
    </>
  );
};
'''
    },
    'product-demo': {
        'description': 'Product feature showcase',
        'duration': 3600,
        'content': '''import { Sequence, interpolate, useCurrentFrame } from 'remotion';

export const ProductDemo: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <>
      {/* Feature 1 - 20 seconds */}
      <Sequence from={0} durationInFrames={600}>
        <Feature
          title="Feature 1"
          description="Key benefit and explanation"
          frame={frame}
        />
      </Sequence>

      {/* Feature 2 - 20 seconds */}
      <Sequence from={600} durationInFrames={600}>
        <Feature
          title="Feature 2"
          description="Additional capability"
          frame={frame - 600}
        />
      </Sequence>

      {/* Feature 3 - 20 seconds */}
      <Sequence from={1200} durationInFrames={600}>
        <Feature
          title="Feature 3"
          description="Premium feature"
          frame={frame - 1200}
        />
      </Sequence>

      {/* CTA - 40 seconds */}
      <Sequence from={1800} durationInFrames={1200}>
        <CTAScreen />
      </Sequence>
    </>
  );
};

interface FeatureProps {
  title: string;
  description: string;
  frame: number;
}

const Feature: React.FC<FeatureProps> = ({ title, description, frame }) => {
  const opacity = interpolate(frame, [0, 15, 585, 600], [0, 1, 1, 0]);

  return (
    <div style={{
      flex: 1,
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#f5f5f5',
      opacity,
    }}>
      <h2 style={{ fontSize: 56, margin: '20px 0' }}>{title}</h2>
      <p style={{ fontSize: 28, maxWidth: 800, textAlign: 'center' }}>
        {description}
      </p>
    </div>
  );
};

const CTAScreen: React.FC = () => {
  return (
    <div style={{
      flex: 1,
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#003d99',
      color: '#fff',
    }}>
      <h1 style={{ fontSize: 72 }}>Ready?</h1>
      <p style={{ fontSize: 36, marginTop: 20 }}>Learn more at example.com</p>
    </div>
  );
};
'''
    },
    'animation': {
        'description': 'Custom animation template with keyframes',
        'duration': 300,
        'content': '''import { interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

export const AnimationTemplate: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Create smooth animations with interpolate
  const scale = interpolate(frame, [0, durationInFrames / 2, durationInFrames], [0.5, 1.2, 1]);
  const rotation = interpolate(frame, [0, durationInFrames], [0, 360]);
  const opacity = interpolate(frame, [0, 30, durationInFrames - 30, durationInFrames], [0, 1, 1, 0]);

  return (
    <div style={{
      flex: 1,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#000',
    }}>
      <div style={{
        width: 200,
        height: 200,
        backgroundColor: '#0066ff',
        borderRadius: '50%',
        transform: `scale(${scale}) rotate(${rotation}deg)`,
        opacity,
      }} />
    </div>
  );
};
'''
    },
    'slideshow': {
        'description': 'Image/content slideshow',
        'duration': 1800,
        'content': '''import { Sequence, interpolate, useCurrentFrame } from 'remotion';

export const Slideshow: React.FC = () => {
  const slides = [
    { title: 'Slide 1', color: '#ff6b6b', duration: 300 },
    { title: 'Slide 2', color: '#4ecdc4', duration: 300 },
    { title: 'Slide 3', color: '#45b7d1', duration: 300 },
    { title: 'Slide 4', color: '#f7dc6f', duration: 300 },
    { title: 'Slide 5', color: '#bb8fce', duration: 300 },
  ];

  let currentFrame = 0;

  return (
    <>
      {slides.map((slide, index) => (
        <Sequence key={index} from={currentFrame} durationInFrames={slide.duration}>
          <Slide {...slide} frame={useCurrentFrame()} maxFrame={slide.duration} />
          {(currentFrame += slide.duration), null}
        </Sequence>
      ))}
    </>
  );
};

interface SlideProps {
  title: string;
  color: string;
  frame: number;
  maxFrame: number;
}

const Slide: React.FC<SlideProps> = ({ title, color, frame, maxFrame }) => {
  const opacity = interpolate(frame, [0, 20, maxFrame - 20, maxFrame], [0, 1, 1, 0]);

  return (
    <div style={{
      flex: 1,
      backgroundColor: color,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      opacity,
    }}>
      <h1 style={{ fontSize: 72, color: '#fff', margin: 0 }}>{title}</h1>
    </div>
  );
};
'''
    },
    'data-viz': {
        'description': 'Data visualization animation',
        'duration': 600,
        'content': '''import { interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

export const DataViz: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const data = [
    { label: 'Q1', value: 30 },
    { label: 'Q2', value: 45 },
    { label: 'Q3', value: 38 },
    { label: 'Q4', value: 55 },
  ];

  return (
    <div style={{
      flex: 1,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'flex-end',
      gap: 40,
      padding: 60,
      backgroundColor: '#fff',
    }}>
      {data.map((item, index) => {
        const delay = index * 30;
        const height = interpolate(
          frame,
          [delay, delay + 60, durationInFrames],
          [0, item.value * 4, item.value * 4],
          { extrapolateRight: 'clamp' }
        );

        return (
          <div key={index} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div
              style={{
                width: 60,
                height,
                backgroundColor: '#0066ff',
                borderRadius: 4,
              }}
            />
            <p style={{ marginTop: 20, fontSize: 20, fontWeight: 'bold' }}>
              {item.label}
            </p>
          </div>
        );
      })}
    </div>
  );
};
'''
    },
}


def get_template(template_type: str) -> dict | None:
    """Retrieve template by type."""
    return TEMPLATES.get(template_type)


def list_templates() -> dict:
    """List all available templates."""
    return {
        'templates': [
            {
                'type': key,
                'description': value['description'],
                'default_duration': value['duration']
            }
            for key, value in TEMPLATES.items()
        ]
    }


def generate_template(
    template_type: str,
    output: str | None = None,
    duration: int | None = None,
    fps: int = 30
) -> dict:
    """Generate a composition template."""
    template = get_template(template_type)

    if not template:
        return {
            'success': False,
            'error': f'Template "{template_type}" not found',
            'available': list(TEMPLATES.keys())
        }

    result_duration = duration or template['duration']

    output_data = {
        'success': True,
        'template': template_type,
        'description': template['description'],
        'duration': result_duration,
        'fps': fps,
        'durationInSeconds': result_duration / fps,
    }

    if output:
        try:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(template['content'])
            result_duration_data = {
                'outputPath': str(output_path.absolute()),
                'fileSize': len(template['content']),
            }
            output_data.update(result_duration_data)
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'template': template_type
            }

    return output_data


def main():
    parser = argparse.ArgumentParser(
        description='Generate Remotion composition templates'
    )
    parser.add_argument(
        '--type',
        choices=list(TEMPLATES.keys()),
        help='Template type'
    )
    parser.add_argument(
        '--output',
        help='Output file path'
    )
    parser.add_argument(
        '--duration',
        type=int,
        help='Custom duration in frames'
    )
    parser.add_argument(
        '--fps',
        type=int,
        default=30,
        help='Frames per second (default: 30)'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all available templates'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    if args.list:
        result = list_templates()
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print("Available Templates:")
            for tpl in result['templates']:
                print(f"  - {tpl['type']}: {tpl['description']} ({tpl['default_duration']} frames)")
        return

    if not args.type:
        print("Error: --type is required (use --list to see available templates)")
        sys.exit(1)

    result = generate_template(
        args.type,
        output=args.output,
        duration=args.duration,
        fps=args.fps
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result['success']:
            print(f"✓ Generated template: {result['template']}")
            print(f"  Description: {result['description']}")
            print(f"  Duration: {result['duration']} frames ({result['durationInSeconds']:.2f}s @ {result['fps']}fps)")
            if 'outputPath' in result:
                print(f"  Saved to: {result['outputPath']}")
        else:
            print(f"✗ Error: {result['error']}")
            sys.exit(1)


if __name__ == '__main__':
    main()
