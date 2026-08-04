
mkdir templates 
python3 scaffold.py user username email phone country_id:references password
python3 scaffold.py country name
python3 scaffold.py room name
python3 scaffold.py User_Items_Table user_id:references room_id:references  name
python3 scaffold.py User_Job user_id:references job_id:references
python3 scaffold.py User_Ai_Job user_id:references job_id:references
python3 scaffold.py Bullet_Point_Workflows User_Job_id:references content
python3 scaffold.py AI_Job_Link_Table  User_Ai_Job:references content
