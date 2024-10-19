A very simple and basic Python script with minimal dependencies to help make AWS Lambda layers.
Uses uv instead of pip as the package manager. Cleans up after itself and zips the environment.

Assuming one is on a Unix system with their base environment setup, one can simply execute './lambda_packager.py {layer_name} {package_1} ... {package_n}' to build the Python packages and zip them into layer_name.zip, ready to be uploaded.
