# Cookie, session, JWT, and authorization header

Explain the difference between:

- Cookie
- Session
- JSON Web Token (JWT)
- `Authorization`-Header

Keep the following questions in mind:

1. Where is data stored?
2. What does the browser send during a request?
3. What part plays the server?
4. What security risks occur?
5. Can the concepts be combined?

## Practical part

Open `http_examples.txt` and answer:

- Which row sets a cookie? - **4**
- Which row sends a cookie back? - **11**
- Which request uses an Authorization Header? - **C and D**
- Which example could contain a JWT? - **C**
- Where is there a hint of a server-side session? - **`session_id` in A and B** 

## Answer

### Cookie

A cookie is a key-value-pair stored client-side.  
The browser sends the cookie automatically to the server that then can read the cookie value and possibly could adjust
its response accordingly.  
The data stored in the cookie are stored in plain text and can be easily read during a man-in-the-middle-attack when
sending the request in plain HTTP or by an infiltrator of the client.

### Session

A session is in general the term for a logically defined period of an interaction between client and server.  
It is possible to store data during a session using cookies. But the term 'session' does not necessarily mean that
something is stored.

### JSON Web Token (JWT)

A JWT is a server-issued token which is sent to the client (typically after login).  
This allows stateless servers because the server does not have to store session state data. This also allows sending a
request with the JWT to another instance of the server (e.g. because of a load balancer) without the client noticing a
change in server instance.

A signed JWT consists of header, payload, and signature. Encrypted JWTs use a different structure.  
The header contains information about which algorithm was used to sign the token whereas the body contains claims which
represent for example the issuer, the expiration, the principal or subject.

This is typically sent in a Cookie or the `Authorization`-Header using `Authorization: Bearer <token>`.

### `Authorization`-Header

The `Authorization`-Header is an HTTP header used to send credentials for authentication. It is typically sent from
client to server to authorize the request.

### Comparison

The comparison of these four terms is pretty simple as, even though they all work together in some way, none of them are
of the same kind.

|      | Cookie                                              | Session        | JSON Web Token          | `Authorization`-Header                                  |
|------|-----------------------------------------------------|----------------|-------------------------|---------------------------------------------------------|
| type | name-value-storage and automatic transport for HTTP | logical period | token format for claims | HTTP header for transmitting authentication credentials |