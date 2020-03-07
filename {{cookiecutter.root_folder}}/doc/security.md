# Understand APIs Security

The APIs supports both `basic` and `apikey` authentication.
In general `basic` is only good for debugging the apis, e.g., with Postman.
`apikey` is must safer option for production uses.

### Basic Authentication

It is preferred basic authentication for post man since the password doesn't
change over time. You just need to setup the authorization token once as
described in the below image and all authenticated API calls just work.

### ApiKey Authentication

Please check the below image to see how apikey can be used for Postman testing
and also for frontend API calls. For the first login, user should call
`GET /api/v1/auth/login` to login using `username` and `password` first.
After that the backend should return a `apikey` that can be later sent as
a http `Authorization` header to authenticate other api calls.

It is important to note that apikey token is often re-generated over time. It
is better to test the APIs using basic auth.
