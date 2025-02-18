import onnx
import argparse

def downgrade_onnx_versions(input_path, output_path):
    # Load the original model
    model = onnx.load(input_path)
    
    # Downgrade IR version to 8
    model.ir_version = 8
    
    # Update all opset imports to version 17
    for opset in model.opset_import:
        # For default ONNX domain (empty string or ai.onnx)
        if opset.domain in ['', 'ai.onnx']:
            opset.version = 17
        # Add logic here if other domains need handling
    
    # Validate and save the modified model
    try:
        onnx.checker.check_model(model)
        onnx.save(model, output_path)
        print(f"Model successfully saved to {output_path}")
    except onnx.checker.ValidationError as e:
        print(f"Validation failed: {e}")

def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Downgrade ONNX model versions.")
    
    # Add arguments for input and output model paths
    parser.add_argument('input_model', type=str, help="Path to the input ONNX model")
    parser.add_argument('output_model', type=str, help="Path to save the downgraded ONNX model")
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Execute version downgrade
    downgrade_onnx_versions(args.input_model, args.output_model)

if __name__ == "__main__":
    main()
