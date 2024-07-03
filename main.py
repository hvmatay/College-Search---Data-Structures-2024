from flask import Flask, redirect, render_template, request
from helpers import state_select, surrounding_select
import sqlite3

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def main():
	
	where_sql = ""
	name_sql = ""
	selected_state = ""
	surrounding_sql = ""
	selected_surrounding = ""
	slider_value = ""
	slider_sql = ""

	if request.method == "POST":
		selected_state = request.form.get('state')
		search = request.form.get('search')
		selected_surrounding = request.form.get('surrounding')
		slider_value = request.form.get('sat_slider')
		if selected_state != None and selected_state != "":
			where_sql = f" AND STABBR = '{selected_state}'"
		if search != None:
			name_sql = f" AND INSTNM LIKE '%{search}%'"
		if selected_surrounding != None and selected_surrounding != "":
			surrounding_sql = f" AND LOCALE = '{selected_surrounding}'"
		if slider_value != 400 and slider_value != None:
			slider_sql = f" AND CAST(SAT_AVG AS INT) > 0 AND SAT_AVG > {slider_value}"

	
	with sqlite3.connect('college.db') as conn:
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		# assemble the db query
		query = f"SELECT UNITID, INSTNM, CITY, STABBR, ZIP, INSTURL, ADM_RATE, SAT_AVG FROM colleges WHERE 1 = 1 {slider_sql} {where_sql} {name_sql} {surrounding_sql}"
		print(query)
		cursor.execute(query)
		rows = (cursor.fetchall())

		rows = [(dict(row)) for row in rows]

		for school in rows:
			for data in school:
				if school[data] == "NULL":
					school[data] = "No Data"
				else:
					if data == "ADM_RATE":
						school[data] = f"{round(school[data] * 100, 2)}%"
					if data == "SAT_AVG":
						school[data] = f"{round(school[data])}"
					if data == "INSTNM" and len(school[data]) > 70:
						school[data] = f"{school[data][0:70]}..."
			

	return render_template("index.html", colleges = rows, states = state_select(selected_state), surroundings = surrounding_select(selected_surrounding))

@app.route('/college/<college_id>')
def detail(college_id):
	with sqlite3.connect('college.db') as conn:
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute("SELECT UNITID, INSTNM, CITY, STABBR, ZIP, INSTURL, LATITUDE, LONGITUDE, ADM_RATE, SAT_AVG, COSTT4_A, TUITIONFEE_IN, TUITIONFEE_OUT, UGDS, UGDS_WHITE, UGDS_BLACK, UGDS_HISP, UGDS_ASIAN, UGDS_AIAN, UGDS_NHPI, UGDS_2MOR, UGDS_NRA, UGDS_UNKN FROM colleges WHERE UNITID=?", [college_id])
		row = (cursor.fetchone())
		row = dict(row)
		for data in row:
				if row[data] == "NULL":
					row[data] = "No Data"
				elif data == "ADM_RATE":
					row[data] = f"{round(row[data] * 100, 2)}%"
		
	return render_template("detail.html", college = row)



app.run(host='0.0.0.0', port=8080)
