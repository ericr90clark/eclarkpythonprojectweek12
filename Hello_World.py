#In this project, I will print out an empty list.

#Command Syntax
aws_list = [ ]

#Empty List command
print ("Empty list:")

print ("aws_list")

#Utilize append command to create AWS Inventory List

print ("aws_list:")

aws_list.append("DynamoDB")
aws_list.append("EC2")
aws_list.append("Cloudwatch")
aws_list.append("Amazon RDS")
aws_list.append("S3")



#Print List Length using "len" command
print ("aws_list:")

len("aws_inventorylist")

#Remove two specific services by name

aws_list.remove("S3")
aws_list.remove("EC2")

print ("aws_list")

#Print out length of new list!
len("aws_list")
