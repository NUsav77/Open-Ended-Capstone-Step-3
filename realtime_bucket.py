# Access S3 NEXRAD Bucket real-time

import boto3
from datetime import datetime
from botocore import UNSIGNED
from botocore.client import Config
import matplotlib.pyplot as plt
from metpy.io import Level2File
from metpy.plots import add_timestamp, ctables
import cartopy
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np


s3 = boto3.resource("s3", config=Config(signature_version=UNSIGNED, user_agent_extra='Resource'))
bucket = s3.Bucket("unidata-nexrad-level2-chunks")


# Create a date/time object for whatever date/time I am interested in
d = datetime(2021, 5, 9, 10)
station = 'KTLX'

# Creates the filename
prefix = f'{d:%Y}/{d:%m}/{d:%d}/{station}/{station}{d:%Y%m%d_%H}'

objects = []
for obj in bucket.objects.filter(Bucket='unidata-nexrad-level2-chunks', limit=10):
    print(obj.key)
    objects.append(obj)

f = Level2File(objects[4].get()['Body'])
ref_norm, ref_cmap = ctables.registry.get_with_steps('NWSReflectivity', 5, 5)

fig, ax = plt.subplots(figsize=(15, 15))

sweep = 0

az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = np.arange(ref_hdr.num_gates) * ref_hdr.gate_width + ref_hdr.first_gate

ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

data = np.ma.array(ref)
data[np.isnan(data)] = np.ma.masked

xlocs = ref_range * np.sin(np.deg2rad(az[:, np.newaxis]))
ylocs = ref_range * np.cos(np.deg2rad(az[:, np.newaxis]))

ax.pcolormesh(xlocs, ylocs, data, cmap=ref_cmap, norm=ref_norm, shading='auto')

ax.set_aspect('equal', 'datalim')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

# # Print first 10 objects in S3 bucket
# for obj in bucket.objects.limit(10):
#     print(obj)

# # Prints all objects in the bucket
# for obj in bucket.objects.filter(Bucket='unidata-nexrad-level2-chunks', limit=1):
#     print(obj.key)
#
#     f = Level2File(obj.get()['Body'])
#
#
#     # Accessing Subset Data
#     sweep = 0
#     az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])
#
#     ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
#     ref_range = np.arange(ref_hdr.num_gates) * ref_hdr.gate_width + ref_hdr.first_gate
#     ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])
#
#     rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
#     rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
#     rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])
#
#     phi_hdr = f.sweeps[sweep][0][4][b'PHI'][0]
#     phi_range = (np.arange(phi_hdr.num_gates + 1) - 0.5) * phi_hdr.gate_width + phi_hdr.first_gate
#     phi = np.array([ray[4][b'PHI'][1] for ray in f.sweeps[sweep]])
#
#     zdr_hdr = f.sweeps[sweep][0][4][b'ZDR'][0]
#     zdr_range = (np.arange(zdr_hdr.num_gates + 1) - 0.5) * zdr_hdr.gate_width + zdr_hdr.first_gate
#     zdr = np.array([ray[4][b'ZDR'][1] for ray in f.sweeps[sweep]])
#
#
#
#
#     # Get the NWS reflectivity colortable from MetPy
#     ref_norm, ref_cmap = ctables.registry.get_with_steps('NWSReflectivity', 5, 5)
#
#     # Plot the data!
#     fig, axes = plt.subplots(2, 2, figsize=(15, 15))
#     for var_data, var_range, colors, lbl, ax in zip((ref, rho, zdr, phi),
#                                                     (ref_range, rho_range, zdr_range, phi_range),
#                                                     (ref_cmap, 'plasma', 'viridis', 'viridis'),
#                                                     ('REF (dBZ)', 'RHO', 'ZDR (dBZ)', 'PHI'),
#                                                     axes.flatten()):
#         # Turn into an array, then mask
#         data = np.ma.array(var_data)
#         data[np.isnan(data)] = np.ma.masked
#
#         # Convert az,range to x,y
#         xlocs = var_range * np.sin(np.deg2rad(az[:, np.newaxis]))
#         ylocs = var_range * np.cos(np.deg2rad(az[:, np.newaxis]))
#
#         # Define norm for reflectivity
#         norm = ref_norm if colors == ref_cmap else None
#
#         # Plot the data
#         a = ax.pcolormesh(xlocs, ylocs, data, cmap=colors, norm=norm)
#
#         divider = make_axes_locatable(ax)
#         cax = divider.append_axes('right', size='5%', pad=0.05)
#         fig.colorbar(a, cax=cax, orientation='vertical', label=lbl)
#
#         ax.set_aspect('equal', 'datalim')
#         ax.set_xlim(-100, 100)
#         ax.set_ylim(-100, 100)
#         add_timestamp(ax, f.dt, y=0.02, high_contrast=False)
#     plt.suptitle('KVWX Level 2 Data', fontsize=20)
#     plt.tight_layout()
#     plt.show()