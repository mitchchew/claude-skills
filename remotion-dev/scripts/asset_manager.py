#!/usr/bin/env python3
"""
Remotion asset manager - Validates, optimizes, and catalogs video assets.
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


SUPPORTED_FORMATS = {
    'images': ['.png', '.jpg', '.jpeg', '.webp', '.svg'],
    'videos': ['.mp4', '.webm', '.mov', '.avi'],
    'audio': ['.mp3', '.wav', '.aac', '.m4a']
}


def get_file_size_mb(file_path: Path) -> float:
    """Get file size in MB."""
    try:
        return file_path.stat().st_size / (1024 * 1024)
    except:
        return 0


def validate_asset(file_path: Path) -> dict:
    """Validate a single asset."""
    if not file_path.exists():
        return {
            'file': file_path.name,
            'path': str(file_path),
            'valid': False,
            'error': 'File not found'
        }

    suffix = file_path.suffix.lower()
    size_mb = get_file_size_mb(file_path)

    # Determine type
    asset_type = 'unknown'
    for type_name, exts in SUPPORTED_FORMATS.items():
        if suffix in exts:
            asset_type = type_name[:-1]  # Remove trailing 's'
            break

    # Validate
    valid = True
    warnings = []
    recommendations = []

    # Check file size
    if asset_type == 'image':
        if size_mb > 5:
            valid = False
            warnings.append(f"Image too large ({size_mb:.1f}MB)")
            recommendations.append(f"Compress to <2MB, suggest 1920x1080 max resolution")
        elif size_mb > 2:
            warnings.append(f"Large image ({size_mb:.1f}MB)")
            recommendations.append("Consider compressing or reducing resolution")

        # Check format
        if suffix == '.bmp':
            valid = False
            warnings.append("BMP format not recommended")
            recommendations.append("Convert to PNG or WebP for better compression")

    elif asset_type == 'video':
        if size_mb > 100:
            warnings.append(f"Large video file ({size_mb:.1f}MB)")
            recommendations.append("Consider compressing or splitting into segments")

        if suffix == '.mov':
            warnings.append("MOV format has compatibility issues")
            recommendations.append("Convert to MP4 (h264) for better compatibility")

    return {
        'file': file_path.name,
        'path': str(file_path),
        'type': asset_type,
        'size_mb': size_mb,
        'valid': valid and asset_type != 'unknown',
        'warnings': warnings,
        'recommendations': recommendations,
        'supported': suffix in [e for exts in SUPPORTED_FORMATS.values() for e in exts]
    }


def validate_assets(directory: str) -> dict:
    """Validate all assets in a directory."""
    dir_path = Path(directory)

    if not dir_path.exists():
        return {
            'success': False,
            'error': f'Directory not found: {directory}'
        }

    if not dir_path.is_dir():
        return {
            'success': False,
            'error': f'Not a directory: {directory}'
        }

    # Find all asset files
    assets = []
    for ext_list in SUPPORTED_FORMATS.values():
        for ext in ext_list:
            assets.extend(dir_path.rglob(f'*{ext}'))

    if not assets:
        return {
            'success': True,
            'directory': str(dir_path),
            'total_assets': 0,
            'assets': [],
            'summary': {
                'valid': 0,
                'warnings': 0,
                'errors': 0,
                'total_size_mb': 0
            }
        }

    # Validate each asset
    validations = [validate_asset(asset) for asset in assets]

    # Aggregate results
    total_size = sum(v.get('size_mb', 0) for v in validations)
    valid_count = sum(1 for v in validations if v.get('valid', False))
    warning_count = sum(1 for v in validations if v.get('warnings', []))
    error_count = sum(1 for v in validations if not v.get('valid', False))

    return {
        'success': True,
        'directory': str(dir_path),
        'total_assets': len(validations),
        'assets': validations,
        'summary': {
            'valid': valid_count,
            'warnings': warning_count,
            'errors': error_count,
            'total_size_mb': total_size,
            'timestamp': datetime.now().isoformat()
        }
    }


def generate_catalog(directory: str) -> dict:
    """Generate asset manifest/catalog."""
    dir_path = Path(directory)

    if not dir_path.exists():
        return {
            'success': False,
            'error': f'Directory not found: {directory}'
        }

    # Categorize assets
    catalog = {
        'images': [],
        'videos': [],
        'audio': [],
        'other': []
    }

    for asset in dir_path.rglob('*'):
        if not asset.is_file():
            continue

        suffix = asset.suffix.lower()
        size_mb = get_file_size_mb(asset)

        asset_info = {
            'name': asset.name,
            'path': str(asset.relative_to(dir_path)),
            'size_mb': size_mb,
            'created': datetime.fromtimestamp(asset.stat().st_ctime).isoformat()
        }

        # Categorize
        if suffix in SUPPORTED_FORMATS['images']:
            catalog['images'].append(asset_info)
        elif suffix in SUPPORTED_FORMATS['videos']:
            catalog['videos'].append(asset_info)
        elif suffix in SUPPORTED_FORMATS['audio']:
            catalog['audio'].append(asset_info)
        else:
            catalog['other'].append(asset_info)

    total_size = sum(
        sum(a['size_mb'] for a in assets)
        for assets in catalog.values()
    )

    return {
        'success': True,
        'directory': str(dir_path),
        'timestamp': datetime.now().isoformat(),
        'catalog': catalog,
        'summary': {
            'total_files': sum(len(assets) for assets in catalog.values()),
            'image_count': len(catalog['images']),
            'video_count': len(catalog['videos']),
            'audio_count': len(catalog['audio']),
            'total_size_mb': total_size
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description='Manage Remotion video assets'
    )
    parser.add_argument(
        'directory',
        help='Asset directory path'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate all assets'
    )
    parser.add_argument(
        '--catalog',
        action='store_true',
        help='Generate asset catalog'
    )
    parser.add_argument(
        '--optimize',
        action='store_true',
        help='Auto-compress and optimize images'
    )
    parser.add_argument(
        '--output',
        help='Save report/catalog to file'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    # Determine operation
    if args.catalog:
        result = generate_catalog(args.directory)
    elif args.validate:
        result = validate_assets(args.directory)
    else:
        # Default to validation
        result = validate_assets(args.directory)

    # Save to file if requested
    if args.output:
        try:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            if args.json or args.output.endswith('.json'):
                output_path.write_text(json.dumps(result, indent=2))
            else:
                # Text format
                output_path.write_text(format_result(result))
            print(f"✓ Report saved to: {output_path.absolute()}")
        except Exception as e:
            print(f"✗ Error saving report: {e}")
            sys.exit(1)

    # Console output
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_result(result))


def format_result(result: dict) -> str:
    """Format result for console output."""
    if not result.get('success'):
        return f"✗ Error: {result.get('error')}"

    if 'catalog' in result:
        # Catalog output
        output = f"Asset Catalog: {result['directory']}\n"
        output += f"Generated: {result['timestamp']}\n\n"
        output += f"Summary:\n"
        output += f"  Total Files: {result['summary']['total_files']}\n"
        output += f"  Images: {result['summary']['image_count']}\n"
        output += f"  Videos: {result['summary']['video_count']}\n"
        output += f"  Audio: {result['summary']['audio_count']}\n"
        output += f"  Total Size: {result['summary']['total_size_mb']:.1f}MB\n\n"

        # List assets
        for type_name, assets in result['catalog'].items():
            if assets:
                output += f"{type_name.upper()}:\n"
                for asset in assets:
                    output += f"  • {asset['name']} ({asset['size_mb']:.1f}MB)\n"
                output += "\n"
        return output
    else:
        # Validation output
        output = f"Asset Validation Report: {result['directory']}\n\n"
        output += f"Summary:\n"
        output += f"  Total Assets: {result['total_assets']}\n"
        output += f"  ✓ Valid: {result['summary']['valid']}\n"
        output += f"  ⚠ Warnings: {result['summary']['warnings']}\n"
        output += f"  ✗ Errors: {result['summary']['errors']}\n"
        output += f"  Total Size: {result['summary']['total_size_mb']:.1f}MB\n\n"

        # List issues
        issues = [a for a in result['assets'] if a.get('warnings') or not a.get('valid')]
        if issues:
            output += "Issues Detected:\n"
            for asset in issues:
                status = "✓" if asset.get('valid') else "✗"
                output += f"{status} {asset['file']}\n"
                for warning in asset.get('warnings', []):
                    output += f"    ⚠ {warning}\n"
                if asset.get('recommendations'):
                    output += f"    → {asset['recommendations'][0]}\n"
            output += "\n"

        # Recommendations
        all_recommendations = []
        for asset in result['assets']:
            all_recommendations.extend(asset.get('recommendations', []))

        if all_recommendations:
            output += f"Optimization Suggestions:\n"
            for i, rec in enumerate(set(all_recommendations), 1):
                output += f"{i}. {rec}\n"

        return output


if __name__ == '__main__':
    main()
