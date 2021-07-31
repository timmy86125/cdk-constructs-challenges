# cdk-constructs-challenges

Using AWS CDK Constructs DualAlbFargateService to build a serverless container service.

### Prerequisites

- Set AWS Credentials ```aws configure```

- Install Python packages ```pip & virtualenv```

- Install AWS CDK ```npm install -g aws-cdk```

### CDK Init

- ```cdk init -l python```

- ```source .venv/bin/activate```

- ```pip install -r requirements.txt```

- ```cdk bootstrap --profile aws_profile_name```

### Modify 

- Type your AWS ACM ARN in aws_acm.Certificate.from_certificate_arn at [cdk_constructs_challenges_stack.py](./cdk_constructs_challenges/cdk_constructs_challenges_stack.py)

### CDK Deploy

- ```cdk diff --profile aws_profile_name```

- ```cdk deploy --profile aws_profile_name```


### Complete

- Get Output CdkConstructsChallengesStack.myServiceExternalEndpoint, and add the CNAME at your domain name service to point to ALB.

- Now, you can access the serverless container service by using your own domain. (ex: https://your.domain.com)

### CDK Destroy

- ```cdk destroy cdk_stack_name --profile aws_profile_name```

### Reference
- https://constructs.dev/
- https://pypi.org/project/cdk-fargate-patterns/
- https://docs.aws.amazon.com/cdk/api/latest/python/
