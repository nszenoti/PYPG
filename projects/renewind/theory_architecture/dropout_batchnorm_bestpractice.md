











For your questions about best practices:

1. **Dropouts:**
   - **Industry practice:** Typically applied selectively, not universally to all layers
   - **Common approach:** Often applied after larger/wider layers and deeper in the network
   - **Best practice:** Start with dropout on the last few hidden layers, then add to earlier layers if needed
   - **Rates:** Usually higher dropout rates (0.3-0.5) for deeper layers, lower rates (0.1-0.2) or none for early layers

2. **Batch Normalization:**
   - **Industry practice:** Often applied to most or all hidden layers, but before activation functions
   - **Common approach:** Add batch normalization between the dense layer and its activation
   - **Best practice:** More beneficial in deeper networks (4+ layers)
   - **Placement:** Usually placed before the activation function (Dense → BatchNorm → Activation)

Both techniques are typically tuned based on validation performance rather than following rigid rules.
