from aws_cdk import core
from cdk_constructs_challenges.cdk_constructs_challenges_stack import CdkConstructsChallengesStack

app = core.App()
CdkConstructsChallengesStack(app, "CdkConstructsChallengesStack")
app.synth()
