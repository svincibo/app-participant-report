#!/usr/bin/env python3

import os
import sys
import numpy as np
import nibabel

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

bold = nibabel.load(sys.argv[1])
bold_data = bold.get_fdata()

html_filename = sys.argv[2]

print("creating mean across all volume")
bold_mean = np.mean(bold_data, axis=3)
print(bold_mean.shape)

#just show seg/cor/axi side by side
def show_slices(slices, means):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    #cmap = matplotlib.colors.LinearSegmentedColormap.from_list('my_cmap',['green','blue'],256)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('my_cmap',['none','red'])
    for i,slice in enumerate(slices):
        axes[i].imshow(means[i].T, cmap="gray", origin="lower")
        axes[i].imshow(slices[i].T, cmap=cmap, origin="lower")
    return fig 

#create thumbnail for bold_mean as base image
sag_i = bold_mean.shape[0]//2
cor_i = bold_mean.shape[1]//2
axi_i = bold_mean.shape[2]//2
means = [
    bold_mean[sag_i, :, :],
    bold_mean[:, cor_i, :],
    bold_mean[:, :, axi_i]
]

with open(html_filename, "w") as html:

    html.write(f'<div class="thumbnails">\n')

    #create overlay for each volumes
    for vidx in range(0, bold_data.shape[3]):
        print("creating thumbnail for", vidx)
        volume = bold_data[:,:,:,vidx]

        #compute the difference between the volume and std across each direction
        diff = (bold_mean - volume)
        sag = np.std(diff, axis=0)
        cor = np.std(diff, axis=1)
        axi = np.std(diff, axis=2)

        fig = show_slices([sag, cor, axi], means)
        fig.savefig(f'output/html/bold/thumb{vidx}.png',  bbox_inches='tight')
        plt.close(fig)

        html.write(f'<div class="thumbnail"><b>Volume {vidx}</b><br><img src="bold/thumb{vidx}.png"></div></li>\n')

    html.write("</div>\n")
