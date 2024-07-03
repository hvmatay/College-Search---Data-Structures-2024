def state_select(selected_state=None):
	states = [
		("", "[None Selected]"), ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
		("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"),
		("DC", "District of Columbia"), ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"),
		("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
		("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"),
		("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"),
		("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"),
		("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"), ("NM", "New Mexico"),
		("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"),
		("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"),
		("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"),
		("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"),
		("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming")
	]
	options = ""
	for abbreviation, state in states:
		selected = "selected" if abbreviation == selected_state else ""
		options += f'<option value="{abbreviation}" {selected}>{state}</option>'
	return options

def surrounding_select(selected_surrounding = None):

	surroundings = [("", "[None Selected]"), ("11", "City: Large"), ("12", "City: Medium"), ("13", "City: Small"), 
	("21", "Suburb: Large"), ("22", "Suburb: Medium"), ("23", "Suburb: Small"),("31", "Town"), ("41", "Rural")]

	options = ""
	for value, surrounding in surroundings:
		selected = "selected" if value == selected_surrounding else ""
		options += f'<option value="{value}" {selected}>{surrounding}</option>'
	return options

# Function to generate HTML
def main_campus(checked=False):
	checkbox_html = 'Main Campus: <input type="checkbox" id="main" name="main"'
	if checked:
		checkbox_html += ' checked'
	checkbox_html += '>'
	return checkbox_html