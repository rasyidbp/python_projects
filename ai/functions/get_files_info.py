import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        valid_target_dir = os.path.commonpath(
                [working_dir_abs, target_dir]
            ) == working_dir_abs
        
        if directory == '.':
            result = 'Result for current directory:\n'
        else:
            result = f"Result for '{directory}' directory\n"

        if not valid_target_dir:
            return f'{result}    Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        if not os.path.isdir(target_dir):
            return f'{result}    Error: "{directory}" is not a directory\n'
        return f'{result}{list_files(target_dir)}'

    except Exception as e:
        return f"Error: {e}"

def list_files(target_dir):
    result=''
    dir_list=os.listdir(target_dir)
    for filename in dir_list:

        # Construct the full path for this entry
        full_path = os.path.join(target_dir, filename)

        # Get the size of this entry
        file_size = os.path.getsize(full_path)

        # Check whether this entry is a directory
        is_directory = os.path.isdir(full_path)

        # Append a formatted line to result
        result += f'  - {filename}: file_size={file_size} bytes, is_dir={is_directory}\n'

    return result
