import uuid
import boto3
from boto3.dynamodb.conditions import Key

def connect_to_db():
	dynamodb = boto3.resource('dynamodb') #This is how one connects to a resource
	table = dynamodb.Table('StarCloud')

	return table

def get_table():
	table = connect_to_db()
	return table

def get_all():
	all_items = get_table().scan()
	result = all_items['Items']
	
	return result