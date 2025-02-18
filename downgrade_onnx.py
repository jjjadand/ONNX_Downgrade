import onnx
import argparse

def downgrade_onnx_versions(input_path, output_path, target_ir_version=8, target_opset_version=17):
    # Load the original model
    model = onnx.load(input_path)
    
    # Downgrade IR version to the target version
    model.ir_version = target_ir_version
    
    # Update all opset imports to the target opset version
    for opset in model.opset_import:
        # For default ONNX domain (empty string or ai.onnx)
        if opset.domain in ['', 'ai.onnx']:
            opset.version = target_opset_version
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
    
    # Optional arguments for IR version and Opset version
    parser.add_argument('--target_ir_version', type=int, default=8, help="Target IR version (default: 8)")
    parser.add_argument('--target_opset_version', type=int, default=17, help="Target Opset version (default: 17)")
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Execute version downgrade
    downgrade_onnx_versions(args.input_model, args.output_model, args.target_ir_version, args.target_opset_version)

if __name__ == "__main__":
    main()

