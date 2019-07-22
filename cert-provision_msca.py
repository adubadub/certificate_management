#! /usr/bin/env python3
if True: # imports
    import os
    import datetime
    import pypsrp
    from pypsrp.client import Client
if True: # set global variables
    now = datetime.datetime.now()
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    device_hostname = '''+DEVICE HOSTNAME HERE+'''
    user = r'''+MS CA USERNAME WITH DOMAIN HERE+'''
    pwd = '''+MS CA PASSWORD HERE+'''
    ca = '''+MS CA IP OR RESOLVABLE HOSTNAME HERE+'''
    date_format = f'{now.year}{month}{day}'
    csrname = f'{device_hostname}_{now.year}{month}{day}.txt'
    ca_drive = r'''+PATH TO DRIVE WHERE CERTIFICATES ARE MANAGED ON MS CA HERE+'''
    submit_command = 'certreq.exe -submit -config -'
    certname = f'{now.year}{month}{day}.cer'
if True: # set pypsrp client connection settings to CA
    ca_client = Client(f"{ca}", username=f"{user}",
                password=pwd,
                cert_validation=False,
                ssl=False
                )
if True: # copy csr to CA with pypsrp client
    # !!!applicable csr must be present in directory where this is run!!!
    ca_client.copy(csrname, f"{ca_drive}\\{csrname}")
if True: # 'submit'/sign csr on CA with pypsrp client      
    ca_client.execute_cmd(f'{submit_command} {ca_drive}\\{csrname} {ca_drive}\\{certname}')
if True: # fetch cert from CA
    # !!!will put certificate in directory where this is run!!!
    ca_client.fetch(f"{ca_drive}\\{certname}", certname)
