# Auth APIs

## POST /api/v1/auth/login/
---------------------------

This API helps to login a user. After logging in, an API key is provided so that sub-sequence api calls can be authenticated.


### Request Parameters

None.


### Request Body

| Fields | Description    |
|--------|----------------|
| username | The username to login |
| password | The password to login |


### Response Body

User can find the following information in the response:

| Fields | Description    |
|--------|----------------|
| email | The user's email |
| username | The user's username |
| first_name | The user's firstname |
| last_name | The user's lastname |
| apikey | The api key to authenticate later without user name and password. |

### Response Status Code

| Code | Description    |
|------|----------------|
| 20X  | Success |


### Sample: TODO

#### Request

```
curl -X POST \
  http://localhost:8000/api/v1/auth/login/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"username": "admin",
	"password": "123456"
}'
```

#### Response Body

```
{
    "email": "admin@jobwell.com",
    "first_name": "Admin",
    "id": 1,
    "last_name": "User",
    "apikey": "apikey admin:e7b15e36f91e4c3460a4bc4e222d733b96daae87",
    "username": "admin"
}
```
* Notes that the `apikey` is changed over time.

## POST /api/v1/auth/logout/
---------------------------

Logout the current user.


### Request Parameters

None.


### Request Body

None.

### Response Body

None.

### Response Status Code

| Code | Description    |
|------|----------------|
| 200  | Success |


### Sample: TODO

#### Request

```
curl -X POST \
  http://localhost:8000/api/v1/auth/logout/ \
  -H 'authorization: Basic YWRtaW46MTIzNDU2' \
  -H 'cache-control: no-cache'
```

#### Response Body

```
{
    "success": true
}
```


