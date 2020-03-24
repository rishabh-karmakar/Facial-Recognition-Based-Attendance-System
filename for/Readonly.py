import os
from stat import S_IREAD, S_IRGRP, S_IROTH
src = r'Attendance.xlsx'
os.chmod(src, S_IREAD|S_IRGRP|S_IROTH)
