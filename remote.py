#!/usr/bin/env python

import paramiko

def init(host): 

    user = "ec2-user"
    idyFile = "/home/mark/aws/gcbitestKeypair.pem"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, username=user, key_filename=idyFile)
    return ssh


def createNewEc2():
    newEc2Cli = ['aws', 'ec2', 'run-instances', '--image-id'
            , 'ami-bcc45885', '--count', '1', '--instance-type'
            , 't2.micro', '--key-name', 'gcbitestKeypair'
            , '--security-groups', 'launch-wizard-1']

    call(newEc2Cli)

def runRemote(host, cmd)
    #host = "ec2-54-223-46-183.cn-north-1.compute.amazonaws.com.cn"
    ssh = init(host)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdout.readlines()
    ssh.close()


