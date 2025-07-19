Great question!

### ✅ No — `AS` is **not mandatory** when assigning table aliases in SQL joins.

You can write:

```sql
FROM customer_t c
JOIN order_t o ON c.customer_id = o.customer_id
```

instead of:

```sql
FROM customer_t AS c
JOIN order_t AS o ON c.customer_id = o.customer_id
```

Both are **valid and equivalent** in most SQL dialects (including MySQL, PostgreSQL, SQL Server, etc.).

---

### 📌 When is `AS` **required**?

* `AS` **is required for column aliasing in `SELECT`**, e.g.:

  ```sql
  SELECT COUNT(*) AS total_count
  ```

  (Some engines like PostgreSQL let you skip `AS` here too, but it's clearer with it.)

---

### ✅ Summary:

| Usage           | With `AS`         | Without `AS`   | Required?          |
| --------------- | ----------------- | -------------- | ------------------ |
| Table aliasing  | `FROM table AS t` | `FROM table t` | ❌ Not required     |
| Column aliasing | `SELECT col AS x` | `SELECT col x` | ✅ Usually required |

So you can safely skip `AS` for table aliases if you prefer a cleaner look.

Let me know if you're targeting a specific SQL dialect (e.g. MySQL, PostgreSQL) — a few nuances might vary!
