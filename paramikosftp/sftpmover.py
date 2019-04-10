#!usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connecto to
t = paramiko.Transport("10.10.2.3", 22) ## IP and Port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filetocopy/"): # iterate on directory contents
    if not os.path.isdir("/home/student/filetocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filetocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close()  # close the connection
