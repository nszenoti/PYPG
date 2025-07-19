Question

```
SELECT
    quarter_number,
    COUNT(*) as order_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage_of_total
FROM order_t
GROUP BY quarter_number
ORDER BY quarter_number;
```

why empty `over()` ??

---


Ah, great question! The `OVER ()` clause is important here because it helps us calculate the total across ALL rows while still keeping our grouped data. Let me explain the difference:

Without `OVER ()`:
```sql
COUNT(*) / SUM(COUNT(*))
```
This wouldn't work because when we use `GROUP BY`, each group only sees its own rows. We'd get an error because you can't nest aggregate functions this way.

With `OVER ()`:
```sql
COUNT(*) / SUM(COUNT(*)) OVER ()
```
The `OVER ()` clause creates what's called a "window function" that can see ALL rows, regardless of the `GROUP BY`. The empty parentheses `()` mean "consider the entire table as one window."

Here's a simpler example to illustrate:
Let's say we have these orders:
```
Q1: 100 orders
Q2: 200 orders
Q3: 300 orders
Q4: 400 orders
Total: 1000 orders
```

When calculating the percentage for Q1:
- `COUNT(*)` gives us 100 (orders in Q1)
- `SUM(COUNT(*)) OVER ()` gives us 1000 (total orders across ALL quarters)
- So: `100 / 1000 * 100 = 10%`

Without the `OVER ()`, we wouldn't be able to access the total of 1000 while still keeping our data grouped by quarter.

Think of it like this:
- `GROUP BY` divides data into quarters
- `OVER ()` lets us peek at the whole table to get the total
- This allows us to calculate each quarter's percentage of the total in a single query

Is that clearer now why we need the empty `OVER ()`?