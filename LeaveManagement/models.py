from django.db import models
from django.contrib.auth.models import User




class LeaveRecordDetail(models.Model):
    employee = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)
    reporting_manager = models.ForeignKey(User, related_name='reporting_manager' ,on_delete=models.CASCADE)
    sick_leaves = models.IntegerField(default=14)
    earned_leaves = models.IntegerField(default=14)
    personal_leaves = models.IntegerField(default=14)

    def __str__(self):
        return str(self.employee) + " " + str(self.reporting_manager)

    class Meta:
        db_table = 'LeaveRecord'



class LeaveApplication(models.Model):

    TYPES_OF_LEAVES = (
        ('SL', 'SickLeave'),
        ('EL', 'EarnedLeave'),
        ('PL', 'PersonalLeave')
    )

    LEAVE_STATUS = (
        ('A', 'Approved'),
        ('R', 'Rejected')
    )

    leave_id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(User, related_name='applicant', on_delete=models.CASCADE)
    approver = models.ForeignKey(User, related_name='approver', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    responded_on = models.DateTimeField(auto_now=True, null=True)
    leave_type = models.CharField(max_length=2, choices=TYPES_OF_LEAVES)
    number_of_days= models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    leave_status = models.CharField(max_length=1, choices=LEAVE_STATUS, default='R')
    additional_message = models.TextField(max_length=200)

    def __str__(self):
        return self.leave_status

    class Meta:
        db_table = 'LeaveApplication'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        a = LeaveRecordDetail.objects.get(employee = self.applicant)
        if self.applicant == a.employee and self.approver == a.reporting_manager:
            super(LeaveApplication,self).save()
        else:
            raise Exception



