#!/usr/bin/env python3

import os
import sys
import json

output_filename = sys.argv[1]

with open("config.json") as f:
    config = json.load(f)

#grab the first input and use that meta
input = config["_inputs"][0]
meta = input["meta"]

subject = ""
if "subject" in meta:
    subject = "sub-"+meta["subject"]

session = ""
if "session" in meta:
    session = "/ ses-"+meta["subject"]

html = """
<!doctype html>
<html>
<head>
    <title>Participant Report</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        .thumbnails {
            display: flex;
            flex-wrap: wrap;
        }
    </style>
</head>
<body>

<div class="container">
    <br>
    <h1 class="title">Participant Report - %s %s</h1>

    <p>TODO describe for the whole report</p>
    <br>

    <div class="columns is-multiline">
""" % (subject, session)

with open(output_filename, "w") as f:
    f.write(html)
