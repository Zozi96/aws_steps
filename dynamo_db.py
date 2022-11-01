from typing import TypedDict
import boto3


dynamodb = boto3.resource('dynamodb')

people = dynamodb.Table('people')

def get_people():
    response = people.scan()
    return response['Items']


class PeopleObject(TypedDict):
    id: int
    name: str
    age: int
    genre: str


def create_person():
    response = people.put_item(
       Item=PeopleObject(id=1, name='Zozi', age=26, genre='Male')
    )
    return response


print(get_people())