
# ONNX Version Downgrader

This script allows you to **downgrade the ONNX model version** to **IR version 8** and update the **opset version** to **17**. It is useful when you need to ensure compatibility with systems or frameworks that require older ONNX versions.

## Requirements
- Python 3.x
- **onnx** library

### Installation:
To install the `onnx` library, use the following command:

```bash
pip install onnx
```

## Usage

### Command-line Usage:

Run the script by providing the input and output model file paths as command-line arguments:

```bash
python downgrade_onnx.py <input_model_path> <output_model_path>
```

- `<input_model_path>`: The path to the original ONNX model you want to downgrade.
- `<output_model_path>`: The path where the downgraded model will be saved.

### Example:

```bash
python downgrade_onnx.py model_v12.onnx model_v8.onnx
```

This will load `model_v12.onnx`, downgrade it to IR version 8, set opset version 17, validate, and save the new model as `model_v8.onnx`.

