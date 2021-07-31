from aws_cdk import core as cdk
from aws_cdk import aws_ecs
from aws_cdk import aws_certificatemanager as aws_acm
import cdk_fargate_patterns as patterns


class CdkConstructsChallengesStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        ecs_task = aws_ecs.FargateTaskDefinition(
            self, 
            "myTask",
            cpu = 256,
            memory_limit_mib = 512,
        )
        
        port_mapping = aws_ecs.PortMapping(
            container_port = 80,
            host_port = 80,
            protocol = aws_ecs.Protocol.TCP
        )

        ecs_task.add_container(
            "myImage",
            image = aws_ecs.ContainerImage.from_registry("nginx:latest"),
            port_mappings=[port_mapping]
        )
        
        cert = aws_acm.Certificate.from_certificate_arn(
            self,
            "myCert",
            "type_your_aws_certificate_arn_here",
        )
        
        patterns.DualAlbFargateService(
            self,
            "myService",
            spot = True,
            tasks = [
                {
                    "task": ecs_task,
                    "external": {"port": 443, "certificate": [cert]},
                    "internal": {"port": 80},
                },
            ],
        )