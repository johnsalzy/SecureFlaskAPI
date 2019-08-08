# SecureFlaskAPI

A flask API with

- user permission levels
- secure(https)
- layout setup

## Setup

---

1. Clone the Repo
2. Enter project folder
3. Enter a virtual Enviornment and install packages

    ```Cmd Prompt
    virtualenv venv
    venv\Scripts\activate
    pip install requirements.txt
    ```

4. Create https token...
5. Setup database

## User Access

---

### Levels

1. None: User has not authenticated themselves
2. Basic: User Has logged in (not many perms)
3. Moderater: User has a account with elevated privledges
4. Admin: User has almost full control
5. SuperAdmin: User can do every query

### Rules

- If a user if of level *Moderater* they also have the same access as a *Basic* would, and so on.
- SuperAdmin is only meant to be one user.
- Access levels can be bumped up by a user of higher access. Excluding a *Basic* user bumping up a *None* user
- etc.
