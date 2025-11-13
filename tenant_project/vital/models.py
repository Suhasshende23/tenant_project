from django.db import models


class VitalFrequencyChoices(models.TextChoices):
    DAILY="Daily"
    HOURLY="Hourly"
    WEEKLY="Weekly"
    MONTHLY="Monthly"

class VitalDeviceChoices(models.TextChoices):
    BLOOD_PRESSURE_MONITOR="Blood Pressure Monitor"
    BLOOD_GLUCOSE_MONITOR="Blood Glucose Monitor"
    CONTINUOS_GLUCOSE_MONITOR="Continuos Glucose Monitor"
    DIGITAL_THERMOMETER="Digital Thermometer"
    PULSE_OXIMETER="Pulse Oximeter"
    PEAK_FLOW_METER="Peak flow meter"
    SPIROMETER="Spirometer"
    WEIGHT_SCALE="Weight scale"
   

class VitalHourChoices(models.TextChoices):
    H00 = "00"
    H01 = "01"
    H02 = "02"
    H03 = "03"
    H04 = "04"
    H05 = "05"
    H06 = "06"
    H07 = "07"
    H08 = "08"
    H09 = "09"
    H10 = "10"
    H11 = "11"


class VitalMinuteChoices(models.TextChoices):
        M00 = "00"
        M01 = "01"
        M02 = "02"
        M03 = "03"
        M04 = "04"
        M05 = "05"
        M06 = "06"
        M07 = "07"
        M08 = "08"
        M09 = "09"
        M10 = "10"
        M11 = "11"
        M12 = "12"
        M13 = "13"
        M14 = "14"
        M15 = "15"
        M16 = "16"
        M17 = "17"
        M18 = "18"
        M19 = "19"
        M20 = "20"
        M21 = "21"
        M22 = "22"
        M23 = "23"
        M24 = "24"
        M25 = "25"
        M26 = "26"
        M27 = "27"
        M28 = "28"
        M29 = "29"
        M30 = "30"
        M31 = "31"
        M32 = "32"
        M33 = "33"
        M34 = "34"
        M35 = "35"
        M36 = "36"
        M37 = "37"
        M38 = "38"
        M39 = "39"
        M40 = "40"
        M41 = "41"
        M42 = "42"
        M43 = "43"
        M44 = "44"
        M45 = "45"
        M46 = "46"
        M47 = "47"
        M48 = "48"
        M49 = "49"
        M50 = "50"
        M51 = "51"
        M52 = "52"
        M53 = "53"
        M54 = "54"
        M55 = "55"
        M56 = "56"
        M57 = "57"
        M58 = "58"
        M59 = "59"



class Vital(models.Model):
    vital_name=models.CharField(max_length=150) # Blood Pressure,Blood Glucose
    frequency=models.CharField(max_length=150,choices=VitalFrequencyChoices)
    interval=models.IntegerField()
    device=models.CharField(max_length=150,choices=VitalDeviceChoices)
    alert=models.BooleanField(default=False)
    high_alert_hours = models.CharField(max_length=30,choices=VitalHourChoices)
    high_alert_minutes = models.CharField(max_length=30,choices=VitalMinuteChoices)
    medium_altert_hours=models.CharField(max_length=30,choices=VitalHourChoices)
    medium_alert_minutes = models.CharField(max_length=30,choices=VitalMinuteChoices)


    def __str__(self):
        return self.vital_name
