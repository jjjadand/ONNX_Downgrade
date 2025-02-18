
# ONNX Version Downgrader

This script allows you to **downgrade the ONNX model version** to **IR version 8** and update the **opset version** to **17**. It is useful when you need to ensure compatibility with systems or frameworks that require older ONNX versions.

## Features
- Downgrades the **IR version** of the ONNX model to **v8**.
- Updates all **opset imports** to version **17** for the default ONNX domain (`''` or `ai.onnx`).
- Validates the modified model using ONNX's checker.
- Saves the modified model to a specified output path.

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
python downgrade_onnx.py <input_model_path> <output_model_path> --target_ir_version <IR_version> --target_opset_version <Opset_version>
```

- `<input_model_path>`: The path to the original ONNX model you want to downgrade.
- `<output_model_path>`: The path where the downgraded model will be saved.
- --target_ir_version `<IR_version>`: Optional. The target IR version to downgrade to. Default is 8.
- --target_opset_version `<Opset_version>`: Optional. The target Opset version to downgrade to. Default is 17.
### Example:
1. Using Default Versions (IR v8, Opset v17):
```bash
python downgrade_onnx.py model_v12.onnx model_v8.onnx
```
This will load `model_v12.onnx`, downgrade it to IR version 8, set opset version 17, validate, and save the new model as `model_v8.onnx`.

2. Using Custom Versions (IR v9, Opset v11):
```bash
python downgrade_onnx.py model_v12.onnx model_v9.onnx --target_ir_version 9 --target_opset_version 11
```
This will load `model_v12.onnx`, downgrade it to IR version 9, set opset version 11, validate, and save the new model as model_v9.onnx.


