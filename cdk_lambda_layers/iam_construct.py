"""Module to hold helper methods for CDK IAM creation"""
from typing import Dict, Any, List
from aws_cdk import aws_iam as iam
from aws_cdk.core import Stack

class IAMConstruct:
    """Class holds methods for IAM resource creation"""
    
    @staticmethod
    def create_role(
        stack: Stack,
        env: str,
        config: dict,
        role_name: str,
        assumed_by: List[str]) -> iam.Role:
        """Create role utilized by lambda, glue, step function, or the stack itself."""
        services = list(map(lambda x: iam.ServicePrincipal(
            f"{x}.amazonaws.com"), assumed_by))
        return iam.Role(
            scope=stack,
            id=f"{config['global']['app-name']}{role_name}-role-id",
            role_name=f"{config['global']['app-name']}{role_name}-role",
            assumed_by=iam.CompositePrincipal(*services)
        )
    
    @staticmethod
    def create_managed_policy(
        stack: Stack,
        env: str,
        config: dict,
        policy_name: str,
        statements: List[iam.PolicyStatement]) -> iam.ManagedPolicy:
        """Create managed policy for lambda roles with permissions for specific services."""
        return iam.ManagedPolicy(
            scope=stack,
            id=f"{config['global']['app-name']}-{policy_name}-policy-id",
            managed_policy_name=f"{config['global']['app-name']}-{policy_name}-policy",
            statements=statements    
        )