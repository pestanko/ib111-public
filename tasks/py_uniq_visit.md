# PyUniqVisit

The tool to track unique visitors on multiple websites.

## Description

The tool is used to track unique visitors on sites where it will be incorporated into.
It sets tracking cookie, in order to determine unique visitor and how long he will stay on a page.

There is also authentication protected User interface and REST API in order to be able to see more detailed analytics.

### Analytics available:

- `anonymized IP` and Geolocation
- User Agent
- The time spend on the webpage

### Storage

- Redis or Database
- configuration file (YAML, TOML)
- Admin user's database (users can be stored also in the file)

### Entities

- Visitor:
    - `id: str` - unique cookie for a user 
    - `first_visit: datetime` - Time when the visitor first visited page
    - `visits: list[Visit]`

- Visit:
    - `visitor: Visitor` - Backreference to the visitor
    - `ip: str` - anonymized IP
    - `UA: str` - User-agent
    - `stated_at: datetime` - when the visit started
    - `ended_at: datetime` - when the visit ended

- Site:
    - `url: str`
    - `name: str` - unique (primary key)
    - `created_at: datetime` - When the tool started tracking the site
    - `admins: list[User]` - List of admin users

- User: 
    - `username: str` (or `email`)
    - `password: str` - hashed password with salt, [example](https://werkzeug.palletsprojects.com/en/0.15.x/utils/#werkzeug.security.generate_password_hash)
    - `sites: list[Site]` - List of sites
    - `is_admin: bool` - Special flag - if it is true - admin user can manage all sites


### Relationships

- User ~ Site - Many to Many
- Visitor ~ Visit - One to Many (Each visitor can have multiple visits, each visit is associated with one visitor)

## Requirements

Application requirements - functional and non-functional

### Functional requirements
- Ability to track uniquie visitors on the website
- Admin user can manage all sites and visitors (CRUD operations)
- Normal user can manage just site he is owning and cannot manage visitors
- Ability to see multiple overall statistics - per day, per month, per site lifetime (how many visitors, how many visitors with Google Chrome ...)
- Authentication protected API and user interface


## Non-funtional requirements:
- Python 3.6 or greater
- Poetry for dependency management and packaing
- Dockerfile with instructions to deploy and run the application
- DB - either text files + REDIS or some relational DB (Postgres or SQLite)
- REST API (I suggest Flask)
- Authentication using the signed [JWT](https://jwt.io/introduction/), algotithm can be just HMAC (`HS256`).
- User interface - either CLI that will requiest the REST API or normal web application - can be Single page.
