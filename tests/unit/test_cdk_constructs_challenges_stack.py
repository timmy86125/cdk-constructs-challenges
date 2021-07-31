import json
import pytest

from aws_cdk import core
from cdk-constructs-challenges.cdk_constructs_challenges_stack import CdkConstructsChallengesStack


def get_template():
    app = core.App()
    CdkConstructsChallengesStack(app, "cdk-constructs-challenges")
    return json.dumps(app.synth().get_stack("cdk-constructs-challenges").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
