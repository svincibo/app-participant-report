#!/usr/bin/env python3

import os
import sys
import json

tracts_dir = sys.argv[1]
surfaces_dir = sys.argv[2]
output_filename = sys.argv[3]

with open(tracts_dir+"/tracts.json") as f:
    tracts = json.load(f)
    for tract in tracts:
        tract["url"] = "../tracts/"+tract["filename"]

surfaces = []
if os.path.exists(surfaces_dir):
    with open(surfaces_dir+"/index.json") as f:
        surfaces = json.load(f)
        for surface in surfaces:
            surface["url"] = "../surfaces/"+surface["filename"]

config = {"tracts": tracts, "surfaces": surfaces}
configJSON = json.dumps(config, indent=4)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="icon" href="/ui/tractview/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TractView</title>
  <script>
   window.config = {configJSON}
  </script>
  <script type="module" crossorigin src="./assets/index.a795d4d3.js"></script>
  <link rel="modulepreload" href="./assets/vendor.3bdcd755.js">
  <link rel="stylesheet" href="./assets/index.3c6d3a59.css">
</head>
<body>
  <div id="app"/>
</body>
</html>
"""

with open(output_filename, "w") as f:
    f.write(html)
