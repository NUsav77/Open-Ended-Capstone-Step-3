import nexradaws
from datetime import datetime
import pytz
# import pyart
# import matplotlib.pyplot as plt

conn = nexradaws.NexradAwsInterface()

# Print available years
print(conn.get_avail_years())

# Get available radars on a given day
print(conn.get_avail_radars('2021', '05', '09'))

# San Diego radar station is KNKX
# Check how many San Diego scans are available between 8am May 9, 2021 and 12pm May 9, 2021
pacific_timezone = pytz.timezone('US/Pacific')
radar_id = 'KNKX'
start = pacific_timezone.localize(datetime(2021, 5, 9, 8, 0))
end = pacific_timezone.localize(datetime(2021, 5, 9, 12, 0))
scans = conn.get_avail_scans_in_range(start, end, radar_id)
print(f'There are {len(scans)} between {start} and {end}')

# Download the first 4 results
results = conn.download(scans[0:4], 'c:')




# The following requires pyart. However, I am unable to install it on Pycharm
# I could only get it working on Jupyter

# fig = plt.figure(figsize=(16, 12))
# for i, scan in enumerate(results.iter_success(), start=1):
#     ax = fig.add_subplot(2, 2, i)
#     radar = scan.open_pyart()
#     display = pyart.graph.RadarDisplay(radar)
#     display.plot('reflectivity', 0, ax=ax, title="{} {}".format(scan.radar_id, scan.scan_time))
#     display.set_limits((-150, 150), (-150, 150), ax=ax)
