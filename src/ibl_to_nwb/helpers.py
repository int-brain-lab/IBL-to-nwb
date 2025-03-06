import os
from pathlib import Path
from one.alf.path import remove_uuid_string


def create_symlinks(source_dir, target_dir, remove_uuid=True, filter=None):
    """replicates the tree under source_dir at target dir in the form of symlinks"""

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = Path(root) / file
            if filter is not None:
                if filter not in str(source_file_path):
                    continue

            target_file_path = target_dir / source_file_path.relative_to(source_dir)
            target_file_path.parent.mkdir(parents=True, exist_ok=True)

            if remove_uuid:
                target_file_path = remove_uuid_string(target_file_path)
            if not target_file_path.exists():
                target_file_path.symlink_to(source_file_path)
