import os
import importlib.util

# Get the directory path
directory = os.path.join(os.path.dirname(__file__), 'utils')

# List all files in the directory
files = os.listdir(directory)

# Filter Python files
python_files = [file for file in files if file.endswith('.py')]

# Import each Python file dynamically
for file in python_files:
    # Construct the full path to the file
    file_path = os.path.join(directory, file)

    # Define the module name
    module_name = file.replace('.py', '')

    # Define the module spec
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    # Load the module
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def test():
    from utils import nginx_utils
    nginx_utils.output_config(
        os.path.join(os.path.dirname(__file__), 'trash',nginx_utils.get_standard_config_filename("testsite")), nginx_utils.get_common_domain_variations("testsite1.com"), 3000)
