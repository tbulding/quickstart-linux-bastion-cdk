#!/usr/bin/env python3

from aws_cdk import core

from quickstart_linux_bastion_cdk.quickstart_linux_bastion_cdk_stack import QuickstartLinuxBastionCdkStack


app = core.App()
QuickstartLinuxBastionCdkStack(app, "quickstart-linux-bastion-cdk")

app.synth()
