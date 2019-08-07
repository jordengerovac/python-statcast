import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

def main():
	# Load Aaron Judge's Statcast data
	judge = pd.read_csv('datasets/statcast/judge.csv')

	# Load Giancarlo Stanton's Statcast data
	stanton = pd.read_csv('datasets/statcast/stanton.csv')

	# Filter to include home runs only
	judge_hr = judge[judge['events'] == 'home_run']
	stanton_hr = stanton.loc[stanton['events'] == 'home_run']
	
	# Zones 11, 12, 13, and 14 are to be ignored for plotting simplicity
	judge_strike_hr = judge_hr.copy().loc[judge_hr.zone <= 9]

	# Assign Cartesian coordinates to pitches in the strike zone for Judge home runs
	judge_strike_hr['zone_x'] = judge_strike_hr.apply(assign_x_coord,axis=1)
	judge_strike_hr['zone_y'] = judge_strike_hr.apply(assign_y_coord,axis=1)

	# Plot Judge's home run zone as a 2D histogram with a colorbar
	plt.hist2d(judge_strike_hr['zone_x'], judge_strike_hr['zone_y'], bins = 3, cmap='Blues')
	plt.title('Aaron Judge Home Runs on\n Pitches in the Strike Zone, 2015-2017')
	plt.gca().get_xaxis().set_visible(False)
	plt.gca().get_yaxis().set_visible(False)
	cb = plt.colorbar()
	cb.set_label('Counts in Bin')


def assign_x_coord(row):
    """
    Assigns an x-coordinate to Statcast's strike zone numbers. Zones 11, 12, 13,
    and 14 are ignored for plotting simplicity.
    """
    # Left third of strike zone
    if row.zone in [1, 4, 7]:
        # ... YOUR CODE FOR TASK 6 ...
        return 1
    # Middle third of strike zone
    if row.zone in [2, 5, 8]:
        # ... YOUR CODE FOR TASK 6 ...
        return 2
    # Right third of strike zone
    if row.zone in [3, 6, 9]:
        # ... YOUR CODE FOR TASK 6 ...
        return 3

def assign_y_coord(row):
    """
    Assigns a y-coordinate to Statcast's strike zone numbers. Zones 11, 12, 13,
    and 14 are ignored for plotting simplicity.
    """
    # Upper third of strike zone
    # ... YOUR CODE FOR TASK 7 ...
    if row.zone in [1,2,3]:
        return 3
    # Middle third of strike zone
    # ... YOUR CODE FOR TASK 7 ...
    if row.zone in [4,5,6]:
        return 2
    # Lower third of strike zone
    # ... YOUR CODE FOR TASK 7 ...
    if row.zone in [7,8,9]:
        return 1


main()
