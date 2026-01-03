Here is a polished, professional **README.md** for your project. I’ve structured it to be scannable for developers and clear for anyone reviewing your portfolio.

---

# 🌐 Yatube API: Social Networking Engine

A robust RESTful API for a social media platform where users can share thoughts, join communities, and stay connected. Built with **Django REST Framework**, this backend provides a secure and scalable foundation for a social network.

## 🚀 Key Features

* **Content Management**: Create and manage posts with support for **Base64 image uploads**.
* **Interactions**: Nested commenting system allowing users to engage with specific posts.
* **Social Graph**: A flexible "Follow" system to subscribe to other users' updates.
* **Communities**: Group-based post categorization for organized content discovery.
* **Security**: Fully implemented **JWT Authentication** (JSON Web Token) via Djoser.
* **Permissions**: Granular access control (Owner-only editing, Read-only for guests).

---

## 🛠 Tech Stack

* **Language:** Python 3.9+
* **Framework:** Django 3.2+
* **API:** Django REST Framework (DRF)
* **Auth:** Djoser + SimpleJWT
* **Database:** SQLite (Development) / PostgreSQL (Production ready)

---

## 🔑 Authentication

The API uses JWT tokens. To access protected endpoints, you must include the token in your headers.

### 1. Obtain Token

`POST /auth/jwt/create/`

```json
{
  "username": "your_username",
  "password": "your_password"
}

```

### 2. Use Token

Include the access token in the header of your requests:
`Authorization: Bearer <access_token>`

---

## 🛰 API Reference

### 📝 Posts

| Method | Endpoint | Description |
| --- | --- | --- |
| **GET** | `/api/v1/posts/` | List all posts |
| **POST** | `/api/v1/posts/` | Create a new post (Auth required) |
| **GET** | `/api/v1/posts/{id}/` | Get post details |
| **PATCH** | `/api/v1/posts/{id}/` | Update own post |
| **DELETE** | `/api/v1/posts/{id}/` | Delete own post |

### 💬 Comments (Nested)

| Method | Endpoint | Description |
| --- | --- | --- |
| **GET** | `/api/v1/posts/{post_id}/comments/` | List all comments for a post |
| **POST** | `/api/v1/posts/{post_id}/comments/` | Add a comment to a post |

### 👥 Groups & Follows

* **Groups**: `GET /api/v1/groups/` — View available communities.
* **Follow**: `GET /api/v1/follow/` — View your subscriptions.
* **Follow**: `POST /api/v1/follow/` — Follow a user by sending `{"following": "username"}`.

---

## 🛡 Permissions Policy

| User Status | Permissions |
| --- | --- |
| **Anonymous** | Read-only access to posts, comments, and groups. |
| **Authenticated** | Can create posts/comments and follow other users. |
| **Author** | Full CRUD (Create, Read, Update, Delete) permissions over their own content. |

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```


2. **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run migrations and start server:**
```bash
python manage.py migrate
python manage.py runserver

```
