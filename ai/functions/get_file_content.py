import os

MAX_CHARS = 10_000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Get the absolute path of the permitted working directory
        working_dir_abs = os.path.realpath(working_directory)

        # Build the target file path
        target_file = os.path.realpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Check whether the target is inside the working directory
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs
        )

        if not valid_target_file:
            return (
                f'Error: Cannot read "{file_path}" '
                'as it is outside the permitted working directory'
            )

        # Check whether the target exists and is a regular file
        if not os.path.isfile(target_file):
            return (
                f'Error: File not found or is not a regular file: '
                f'"{file_path}"'
            )

        # Read up to MAX_CHARS characters
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            # Check whether there is more content
            if f.read(1):
                content += (
                    f'\n[...File "{file_path}" truncated '
                    f'at {MAX_CHARS} characters]'
                )

        return content

    except Exception as e:
        return f"Error: {e}"

