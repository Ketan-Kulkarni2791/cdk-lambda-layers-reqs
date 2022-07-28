"""Code for generating lambda layers."""
from typing import List
from aws_cdk import (
    core,
    aws_lambda as _lambda
)


class LambdaLayerConstruct:
    """Construct for creating lambdas layers."""
    
    @staticmethod
    def create_lambda_layer(
        stack: core.Stack,
        env: str,
        config: dict,
        layer_name: str,
        compatible_runtimes: List[_lambda.Runtime]
    ) -> _lambda.LayerVersion:
        """Method to create Lambda Layers."""
        
        code_location = _lambda.AssetCode(config['global'][f"{layer_name}_location"])
        return _lambda.LayerVersion(
            scope=stack,
            id=f"{config['global']['app-name']}-{layer_name}-Id",
            code=code_location,
            compatible_runtimes=compatible_runtimes
        )