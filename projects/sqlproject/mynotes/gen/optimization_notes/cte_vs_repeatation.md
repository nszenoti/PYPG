QUE

but when we write

SELECT
    c.state,
    COUNT(DISTINCT o.customer_id) as customers_count,
    ROUND(COUNT(DISTINCT o.customer_id) * 100.0 / (SELECT COUNT(DISTINCT customer_id) FROM order_t), 2) as percentage
FROM order_t o
JOIN customer_t c ON c.customer_id = o.customer_id
GROUP BY c.state
ORDER BY customers_count DESC;

does here

COUNT(DISTINCT o.customer_id) is computed twice for each group  and
(SELECT COUNT(DISTINCT customer_id) FROM order_t), 2) is computed for each group despite being constant ?

---


Excellent — you're digging into the **internals of query evaluation**, which is crucial for performance tuning.

Let’s address both parts of your question **precisely**, assuming **MySQL 8+** (similar applies to PostgreSQL, etc.):

---

## 🧮 1. Does `COUNT(DISTINCT o.customer_id)` get computed **twice per group**?

### ✅ Yes — most likely.

Even though it's the **same expression** repeated:

```sql
COUNT(DISTINCT o.customer_id)
```

appears **twice**:

* Once as the raw column: `AS customers_count`
* Again inside the percentage formula

👉 MySQL **does not guarantee** that it will compute it **once and reuse** — each expression is treated separately unless optimized away by the query planner.

So **technically**, it can compute `COUNT(DISTINCT o.customer_id)` **twice per group**.

---

## 📊 2. Does the subquery:

```sql
(SELECT COUNT(DISTINCT customer_id) FROM order_t)
```

get computed **for each group**?

### 🔁 Answer: **Yes**, but... depends.

In most engines **including MySQL**, this is an **uncorrelated scalar subquery**, and:

* It is **logically constant** (same value for every row/group).
* However, **MySQL does not always cache scalar subqueries**.
* So in practice, it **may be evaluated once per group**, unless:

  * The optimizer **materializes** it (unlikely without hints/rewrites).
  * You use a **CTE** or **subquery in `FROM` clause** to cache it.

---

## 🧠 Summary Table:

| Expression                                 | Evaluated Once or Multiple?           | Optimization Tip                 |
| ------------------------------------------ | ------------------------------------- | -------------------------------- |
| `COUNT(DISTINCT o.customer_id)`            | ❌ Likely **computed twice per group** | Alias it or use subquery/CTE     |
| `(SELECT COUNT(DISTINCT customer_id) ...)` | ❌ May be **computed per group**       | Use CTE or move to `FROM` clause |

---

## ✅ Optimized Version (avoid recomputation):

```sql
WITH total_count AS (
    SELECT COUNT(DISTINCT customer_id) AS total_customers FROM order_t
),
customer_counts AS (
    SELECT
        c.state,
        COUNT(DISTINCT o.customer_id) AS customers_count
    FROM order_t o
    JOIN customer_t c ON c.customer_id = o.customer_id
    GROUP BY c.state
)
SELECT
    cc.state,
    cc.customers_count,
    ROUND(cc.customers_count * 100.0 / tc.total_customers, 2) AS percentage
FROM customer_counts cc
JOIN total_count tc
ORDER BY customers_count DESC;
```

💡 Now:

* Each heavy aggregation (`COUNT(DISTINCT ...)`) is computed **exactly once**.
* Optimizer can **reuse** them safely and cleanly.

---

Let me know if you want to benchmark both with `EXPLAIN ANALYZE`.
