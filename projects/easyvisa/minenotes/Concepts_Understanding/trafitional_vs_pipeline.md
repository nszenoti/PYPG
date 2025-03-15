trafitional_vs_pipeline

Yes, exactly!  

- **Traditional Approach:** You manually create and store three versions of `X_train`:  
  - `X_train_default`
  - `X_train_undersampled`
  - `X_train_oversampled`  
  These are **physically stored** and reused.  

- **Pipeline Approach:** It **does not store** multiple versions. Instead, each pipeline (default, undersampled, oversampled)  
  - **Recomputes** transformations dynamically when `fit()` or `predict()` is called.  
  - Keeps **data isolated within each pipeline**, ensuring that transformations apply only when needed.  

Thus, the **pipeline approach eliminates the need to store multiple datasets**, keeping the process modular and efficient.