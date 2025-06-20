# 🐦 Bird App

A simple Flask app connected to a PostgreSQL database, deployed on [Render](https://render.com).

---

## 📌 **Setup Guide**

### 1️⃣ **Create a PostgreSQL Database on Render**

1. Go to the [Render dashboard](https://dashboard.render.com/).
2. Click the **"New +"** button and select **"PostgreSQL"**.
3. Fill in:
   - **Name** — any name you like (e.g. `my_database`).
   - **Version** — choose the PostgreSQL version you prefer.
   - Render will auto-generate the **Database** and **User**, or you can customize them.
   - **Region** — choose a region close to you (e.g. Oregon (US West)).  
     *Tip: Use the same region later for your web service.*
4. Scroll down and click **"Deploy Database"**.

---

### 2️⃣ **Create Your Application Database**

1. After deployment, scroll down to the **Connections** section and copy the **PSQL Command**.
2. Open your terminal and paste that command to connect:
   You should see a prompt like:
   ```
   my_database=>
   ```
3. Create your app-specific database:
   ```sql
   CREATE DATABASE bird_app_db;
   ```

---

### 3️⃣ **Set Up Your Flask App Locally**

1. Create your Flask app project structure and install dependencies using `pipenv`:
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate flask_restful psycopg2-binary gunicorn
   ```
2. Generate a `requirements.txt` for deployment:
   ```bash
   pipenv requirements > requirements.txt
   ```

---

### 4️⃣ **Configure the Database Connection**

1. In your Flask app (`app.py`), add:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
   ```

2. In your terminal, set the `DATABASE_URI` environment variable.  
   - Back on the Render dashboard, go to your database details → **Connections → External Database URL**.
   - Modify:
     - Change `postgres://` → `postgresql://`
     - Replace `my_database` at the end with `bird_app_db`

   Example:
   ```bash   ```bash
   psql ...
   ```
   export DATABASE_URI=postgresql://my_database_user:YOUR_PASSWORD@YOUR_HOST:PORT/bird_app_db
   ```

---

### 5️⃣ **Deploy the Web Service on Render**

1. Go back to the Render dashboard.
2. Click **"New +" → "Web Service"**.
3. Connect your GitHub repo containing your Flask app.
4. In **Advanced Settings**, add the following **Environment Variables**:
   - `PYTHON_VERSION` = `3.8.13`
   - `DATABASE_URI` = *(Use your database’s **Internal Database URL**, not the External one)*  
     - Remember to update `postgres://` to `postgresql://` and the database name to `bird_app_db`.

5. Set your **Start Command**:
   ```bash
   gunicorn app:app
   ```

6. Click **Deploy Web Service**.

---

### ⚡ **Notes**

- If your **database** and **web service** are in different regions, use the **External Database URL** instead of Internal.
- Use `flask db init`, `flask db migrate`, and `flask db upgrade` to set up your migrations before deploying.

---

## ✅ **Done!**

You now have a Flask app connected to a managed PostgreSQL database, fully deployed on Render! 🎉🚀

---

**Happy Coding!** 
```

---
