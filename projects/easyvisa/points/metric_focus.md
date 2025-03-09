

Yes, you should focus on correctly identifying denied visa applications. In this context:

1. **Focus on recall for the "Denied" class**: You want to minimize false negatives (cases where the model predicts "Certified" but the actual outcome was "Denied").

2. **Why this matters**: Missing a potential visa denial (false negative) would mean approving someone who should be denied, which has more serious consequences than the opposite error.

3. **Business impact**: From OFLC's perspective, incorrectly approving a visa that should be denied could:
   - Allow unqualified workers into the system
   - Potentially impact US workers' wages or job opportunities
   - Create compliance issues with immigration regulations

4. **Evaluation metric**: When building your models later, you'll want to optimize for recall on the "Denied" class, possibly using metrics like F2-score (which weights recall higher than precision).

This approach aligns with the regulatory nature of the problem, where false approvals are likely more costly than false denials.
