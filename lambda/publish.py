# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT


# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
def publish_function(connection, alarm, imok):
    ENDPOINT = "a1s2o6e2f4mlx6-ats.iot.us-east-1.amazonaws.com"
    CLIENT_ID = "NodeMCU"
    PATH_TO_CERT = "certificate.pem.crt"
    PATH_TO_KEY = "private.pem.key"
    PATH_TO_ROOT = "CA.pem"
    
    myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    
    myAWSIoTMQTTClient.connect()

    myAWSIoTMQTTClient.publish("INTERVAL_CONNECTION", connection, 1) 
    myAWSIoTMQTTClient.publish("INTERVAL_ALARM", alarm, 1)
    myAWSIoTMQTTClient.publish("INTERVAL_IMOK", imok, 1)
    t.sleep(0.1)
    
    myAWSIoTMQTTClient.disconnect()