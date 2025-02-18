
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
python downgrade_onnx.py <input_model_path> <output_model_path>
```

- `<input_model_path>`: The path to the original ONNX model you want to downgrade.
- `<output_model_path>`: The path where the downgraded model will be saved.

### Example:

```bash
python downgrade_onnx.py model_v12.onnx model_v8.onnx
```

This will load `model_v12.onnx`, downgrade it to IR version 8, set opset version 17, validate, and save the new model as `model_v8.onnx`.

## How it Works:
1. The script loads the ONNX model using the `onnx.load()` method.
2. It downgrades the **IR version** to v8.
3. It updates all **opset imports** to version 17.
4. It validates the model with `onnx.checker.check_model()`.
5. The script saves the modified model to the specified output path.

## Error Handling
If the model fails validation, the script will display a **validation error** and not save the modified model.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or fixes.

## License
This project is licensed under the MIT License.
