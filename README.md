# Treelynk REST API

## Auth
| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/auth/signup`   | Register a new user      |
| POST   | `/auth/login`    | Login and receive JWT    |
| POST   | `/auth/logout`   | Logout user              |
| POST   | `/auth/refresh`  | Get new access token     |

---

## Users
| Method | Endpoint       | Description                                  |
|--------|----------------|----------------------------------------------|
| GET    | `/users/me`    | Get logged-in user profile                   |
| PUT    | `/users/me`    | Update user profile (name, bio, avatar, etc.)|
| DELETE | `/users/me`    | Delete account                               |

---

## Pages
| Method | Endpoint              | Description                            |
|--------|-----------------------|----------------------------------------|
| POST   | `/pages`              | Create a new page (link-in-bio style)  |
| GET    | `/pages`              | Get all pages for logged-in user       |
| GET    | `/pages/{page_id}`    | Get details of one page                |
| PUT    | `/pages/{page_id}`    | Update page (theme, title, layout)     |
| DELETE | `/pages/{page_id}`    | Delete page                            |

---

## Links
| Method | Endpoint                              | Description                       |
|--------|---------------------------------------|-----------------------------------|
| POST   | `/pages/{page_id}/links`              | Add a new link to a page          |
| GET    | `/pages/{page_id}/links`              | Get all links for a page          |
| PUT    | `/pages/{page_id}/links/{link_id}`    | Update a link (URL, title, order) |
| DELETE | `/pages/{page_id}/links/{link_id}`    | Remove a link                     |

---

## Analytics
| Method | Endpoint                     | Description                  |
|--------|------------------------------|------------------------------|
| GET    | `/analytics/page/{page_id}`  | Get clicks & views for a page|
| GET    | `/analytics/link/{link_id}`  | Get clicks for a link        |
