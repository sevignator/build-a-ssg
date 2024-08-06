import os
import shutil


def main() -> None:
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(current_dir)
    source_dir = os.path.join(root_dir, "static")
    dest_dir = os.path.join(root_dir, "public")

    copy_source_to_dest(source_dir, dest_dir)


def copy_source_to_dest(src_dir: str, dest_dir: str):
    if not os.path.exists(src_dir):
        raise ValueError(f"Source directory doesn't exist: {src_dir}.")

    if not os.path.exists(dest_dir):
        raise ValueError(f"Destination directory doesn't exist: {dest_dir}.")

    # Get the list of all entries in both directories
    src_content = os.listdir(src_dir)
    dest_content = os.listdir(dest_dir)

    # Exit early if the source directory has no entry
    if len(src_content) == 0:
        return

    # Clear destination directory if non-empty
    if len(dest_content) != 0:
        for entry in dest_content:
            dest_entry_path = os.path.join(dest_dir, entry)

            # Delete files
            if os.path.isfile(dest_entry_path):
                os.remove(dest_entry_path)
                continue

            # Delete directory trees
            shutil.rmtree(dest_entry_path)

    # For each entry, determine whether it's a file or a sub-directory
    for entry in src_content:
        src_entry_path = os.path.join(src_dir, entry)
        dest_entry_path = os.path.join(dest_dir, entry)

        # Copy the file over to the destination and move to the next iteration
        if os.path.isfile(src_entry_path):
            print(f"New file: {dest_entry_path}")
            shutil.copy(src_entry_path, dest_entry_path)
            continue

        # Create same directory in the destination and recursively
        # call this function.
        print(f"New directory: {dest_entry_path}")
        os.mkdir(dest_entry_path)
        copy_source_to_dest(src_entry_path, dest_entry_path)


main()
