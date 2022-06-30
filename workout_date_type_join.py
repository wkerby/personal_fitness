import pandas as pd
#load in each separate body part table as a df 
arms_w = pd.read_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\Arm-Workouts.xlsx')
back_w = pd.read_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\Back-Workouts.xlsx')
chest_w = pd.read_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\\Chest-Workouts.xlsx')
shoulder_w = pd.read_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\\Shoulder-Workouts.xlsx')
leg_w = pd.read_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\\Leg-Workouts.xlsx')

#create the dict that will become the workout_date_type_join table that we write to excel
workout_date_type_dict = {'Workout Type Join ID' : [], 'Workout ID': [], 'Type ID': []}

#create a list of all body part workout dataframes 
workouts = [arms_w, back_w, chest_w, shoulder_w, leg_w]

#transform all dfs in the workouts dictionary into own dictionaries by creating a list of dictionaries
body_workouts = [w.to_dict() for w in workouts]

#retrieve a list of only the first instance of every workout ID that appears in every body part table
#and add it to the Workout ID key in workout_date_type_dict and then create a list of the corresponding type value
#for that workout id and add it to the Type ID key in workout_date_type_dict
for workout in body_workouts:
	workout_ids = []
	indices = []
	for index, workout_id in list(workout['Workout ID'].items()):
		if workout_id not in workout_ids:
			workout_ids.append(workout_id)
			indices.append(index)

	if body_workouts.index(workout) == 0:
		workout_date_type_dict['Workout ID'] = workout_ids
		workout_date_type_dict['Type ID'] = [list(workout['Type ID'].values())[index] for index in indices]
	else:
		for workout_id in workout_ids:
			workout_date_type_dict['Workout ID'].append(workout_id)
		for type_id in [list(workout['Type ID'].values())[index] for index in indices]:
			workout_date_type_dict['Type ID'].append(type_id)

#create the join ID attribute so it is just an integer index from 0 to len of either Workout ID or Type ID attribute
workout_date_type_dict['Workout Type Join ID'] = list(range(1,len(workout_date_type_dict['Workout ID'])+1))

#pass the workout_date_type_dict into a df so we can write to excel
workout_date_type_join_ = pd.DataFrame(workout_date_type_dict)

#write the workout_date_type_join table to excel with index = False
workout_date_type_join_.to_excel(r'C:\Users\wkerb\Dropbox\PC\Desktop\Exercise\\workout-date-type-join.xlsx', index = False)