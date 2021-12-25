from django.db import models

class UserDataPatientRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_name = models.CharField(db_column='Patient_Name', max_length=150)  # Field name made lowercase.
    patient_mobile = models.CharField(db_column='Patient_Mobile', max_length=12)  # Field name made lowercase.
    patient_email = models.CharField(db_column='Patient_Email', max_length=150)  # Field name made lowercase.
    patient_address = models.TextField(db_column='Patient_Address')  # Field name made lowercase.
    patient_aadharnumber = models.CharField(db_column='Patient_Aadharnumber', max_length=13)  # Field name made lowercase.
    patient_ref_id = models.CharField(db_column='Patient_Ref_id', unique=True, max_length=12)  # Field name made lowercase.
    x_rayimage = models.CharField(max_length=100)
    patient_status = models.CharField(db_column='Patient_Status', max_length=10)  # Field name made lowercase.
    patient_severity = models.CharField(db_column='Patient_Severity', max_length=20)  # Field name made lowercase.
    patient_result = models.CharField(db_column='Patient_Result', max_length=25)  # Field name made lowercase.
    patient_age = models.CharField(db_column='Patient_Age', max_length=3)  # Field name made lowercase.
    patient_gender = models.CharField(db_column='Patient_Gender', max_length=7)  # Field name made lowercase.
    scan_time = models.DateTimeField(db_column='Scan_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_data_patient_record'