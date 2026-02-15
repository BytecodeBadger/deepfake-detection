"""
Sample N images from every subdirectory and copy to output directory.
Usage:
    python sample_images.py /path/to/source_dir /path/to/output_dir -n 10
"""

import argparse
import shutil
import random
from pathlib import Path
from typing import Optional


def sample_images_from_dirs(
    source_dir: Path,
    output_dir: Path,
    sample_size: int,
    recursive: bool = True
) -> None:
    """
    Sample N images from every directory and copy to output directory.
    
    Args:
        source_dir: Root directory containing image subdirectories or images
        output_dir: Directory where sampled images will be copied
        sample_size: Number of images to sample from each directory
        recursive: If True, recursively sample from nested directories (default: True)
    """
    source_dir = Path(source_dir).resolve()
    output_dir = Path(output_dir).resolve()
    
    if not source_dir.exists():
        raise ValueError(f"Source directory does not exist: {source_dir}")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Image extensions to consider
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    
    # Check if source_dir contains images directly
    direct_images = [
        f for f in source_dir.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]
    
    total_copied = 0
    
    # If there are images directly in source_dir, process them
    if direct_images:
        sample = random.sample(direct_images, min(sample_size, len(direct_images)))
        
        # Copy sampled images
        for img_file in sample:
            try:
                output_path = output_dir / img_file.name
                shutil.copy2(img_file, output_path)
                total_copied += 1
            except Exception as e:
                print(f"Error copying {img_file.name}: {e}")
        
        print(f"Sampled {len(sample)} images from {source_dir.name}")
    
    # Otherwise, find all leaf directories that contain images and process them
    else:
        # Get all directories recursively and filter to only those with images
        all_dirs = [d for d in source_dir.rglob('*') if d.is_dir()]
        
        dirs_with_images = []
        for dir_path in all_dirs:
            image_files = [
                f for f in dir_path.iterdir()
                if f.is_file() and f.suffix.lower() in image_extensions
            ]
            if image_files:
                dirs_with_images.append((dir_path, image_files))
        
        if not dirs_with_images:
            print(f"No images found in: {source_dir}")
        else:
            for dir_path, image_files in dirs_with_images:
                # Sample up to sample_size images
                sample = random.sample(image_files, min(sample_size, len(image_files)))
                
                # Create subdirectory in output preserving relative path
                relative_path = dir_path.relative_to(source_dir)
                output_subdir = output_dir / relative_path
                output_subdir.mkdir(parents=True, exist_ok=True)
                
                # Copy sampled images
                for img_file in sample:
                    try:
                        output_path = output_subdir / img_file.name
                        shutil.copy2(img_file, output_path)
                        total_copied += 1
                    except Exception as e:
                        print(f"Error copying {img_file.name}: {e}")
                
                print(f"Sampled {len(sample)} images from {dir_path.relative_to(source_dir)}")
    
    print(f"\nTotal images copied: {total_copied}")
    print(f"Output directory: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Sample N images from every subdirectory"
    )
    parser.add_argument(
        "source_dir",
        type=str,
        help="Source directory containing image subdirectories"
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Output directory where sampled images will be copied"
    )
    parser.add_argument(
        "-n", "--sample-size",
        type=int,
        default=10,
        help="Number of images to sample from each directory (default: 10)"
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recursively process nested directories (default: True)"
    )
    
    args = parser.parse_args()
    
    try:
        sample_images_from_dirs(
            source_dir=args.source_dir,
            output_dir=args.output_dir,
            sample_size=args.sample_size,
            recursive=args.recursive
        )
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
