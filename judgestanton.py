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

def prediction_and_evaluation():
	judge_filtered = pd.read_csv('datasets/statcast/judge.csv', usecols=['release_speed', 'hit_distance_sc', 'launch_speed', 'launch_angle'])
	judge_filtered = judge_filtered.dropna(axis=0)
	y = judge_filtered.hit_distance_sc
	judge_features = ['release_speed', 'launch_speed', 'launch_angle']
	X = judge_filtered[judge_features]
	
	# Define model. Specify a number for random_state to ensure same results each run
	judge_model = DecisionTreeRegressor(random_state=1)

	# Fit model
	judge_model.fit(X, y)
	
	print("Making predictions for the following 5 hits:")
	print(X.head())
	print("The predictions are")
	print(judge_model.predict(X.head()))
	
	# split data into training and validation data, for both features and target
	# The split is based on a random number generator. Supplying a numeric value to
	# the random_state argument guarantees we get the same split every time we
	# run this script.
	train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
	# Define model
	judge_model = DecisionTreeRegressor()
	# Fit model
	judge_model.fit(train_X, train_y)

	# get predicted prices on validation data
	val_predictions = judge_model.predict(val_X)
	print(mean_absolute_error(val_y, val_predictions))
	

main()
