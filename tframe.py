#!/usr/bin/python3
#
# THIS IS NOT SUPPORTED BY TENABLE.
# THIS IS NOT SUPPORTED BY ANYONE.
#
# This is a skeleton script used as a starting point for building scripts that work with
# Tenable products.  THIS IS NOT SUPPORTED BY TENABLE.
#
# THIS IS NOT SUPPORTED BY TENABLE.
# THIS IS NOT SUPPORTED BY ANYONE.
#
# Rename the tframe.py to whatever you are calling your script, and then start coding!
# This uses pyTenable.  For more information see https://readthedocs.org/projects/pytenable/
#
# Requires the following:
#   pip install pytenable


from tenable.io import TenableIO
from tenable.sc import TenableSC
import argparse
import os
import csv
import sys
import time

#Right now, host and port are ignored
class TFrame(object):
    def __init__(self):
        self.debug = False
        self.tio_access_key = None
        self.tio_secret_key = None
        self.tsc_username = None
        self.tsc_password = None
        self.host = None
        self.port = None
        self.tenable_connection = None

    def enable_debug(self):
        self.debug = True
        print("Debugging is enabled.")

    def disable_debug(self):
        self.debug = False

    def set_tenable_io_access_key(self, value):
        try:
            self.tio_access_key = str(value)
            return True
        except:
            return False

    def set_tenable_io_secret_key(self, value):
        try:
            self.tio_secret_key = str(value)
            return True
        except:
            return False

    def set_tenable_sc_username(self, value):
        try:
            self.tsc_username = str(value)
            return True
        except:
            return False

    def set_tenable_sc_password(self, value):
        try:
            self.tsc_password = str(value)
            return True
        except:
            return False

    def set_host(self, value):
        try:
            self.host = str(value)
            return True
        except:
            return False

    def set_port(self, value):
        try:
            self.host = str(value)
            return True
        except:
            return False

    # If the connection succeeds, return True, otherwise False
    def connect(self):
        if self.host is not None and self.port is not None:
            if self.tio_access_key is not None and self.tio_secret_key is not None:
                self.tenable_connection = TenableIO(self.tio_access_key, self.tio_secret_key)
                return self.tenable_connection
            elif self.tsc_username is not None and self.tsc_password is not None:
                self.tenable_connection = TenableSC(self.host, port=self.port)
                self.tenable_connection.login(self.tsc_username, self.tsc_password)
                return self.tenable_connection
        return False



######################
###
### Program start
###
######################

if __name__ == '__main__':
    # Get the arguments from the command line
    parser = argparse.ArgumentParser(description="Put the description of your script here")
    parser.add_argument('--accesskey',help="The Tenable.io access key",nargs=1,action="store")
    parser.add_argument('--secretkey',help="The Tenable.io secret key",nargs=1,action="store")
    parser.add_argument('--username',help="The Tenable.sc username key",nargs=1,action="store")
    parser.add_argument('--password',help="The Tenable.sc password key",nargs=1,action="store")
    parser.add_argument('--host',help="The Tenable.io or Tenable.sc host. (Default is cloud.tenable.com)",nargs=1,action="store",default=["cloud.tenable.com"])
    parser.add_argument('--port',help="The Tenable.io port. (Default is 443)",nargs=1,action="store",default=["443"])
    parser.add_argument('--debug',help="Turn on debugging",action="store_true")
    args=parser.parse_args()

    tenable_connector = TFrame()

    if args.debug:
        tenable_connector.enable_debug()

    # Try pulling credentials from environment, but if there are command line variables they will override.
    if os.getenv('TIO_ACCESS_KEY') is not None:
        tenable_connector.set_tenable_io_access_key(os.getenv('TIO_ACCESS_KEY'))

    if os.getenv('TIO_SECRET_KEY') is not None:
        tenable_connector.set_tenable_io_secret_key(os.getenv('TIO_SECRET_KEY'))


    try:
        if args.accesskey[0] != "":
            tenable_connector.set_tenable_io_access_key(args.accesskey[0])
            tenable_connector.set_tenable_io_secret_key(args.secretkey[0])
    except:
        pass

    try:
        if args.username[0] != "":
            tenable_connector.set_tenable_sc_username(args.username[0])
            tenable_connector.set_tenable_sc_username(args.password[0])
    except:
        pass

    try:
        if args.host[0] != "":
            tenable_connector.set_host(args.host[0])
    except:
        pass

    try:
        if args.port[0] != "":
            tenable_connector.set_host(args.port[0])
    except:
        pass

    # Create the connection to whatever platform has been specified.
    conn = tenable_connector.connect()

    if conn is False:
        exit(-1)

    # The conn object can now be used to make calls



