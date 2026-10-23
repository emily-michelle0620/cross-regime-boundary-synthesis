# Hardware Alignment & Sensor Tuning SOP

## 1. Clinical Scalp Mapping for Subject Sub-01 (Age 35)
To preserve the fidelity of microvolt-scale gamma-band visual responses (30–60 Hz), follow the channel preparation metrics precisely:
- Clean and debride targeted occipital sensor positions (`O1`, `O2`, `Oz`, `POz`).
- Apply chloride-based electrolyte gel into active electrode sockets using a blunt syringe.
- Confirm real-time software diagnostics drop channel impedance metrics strictly below **5 kΩ**.

## 2. Optic Null Measurement Metrics
When monitoring signal suppression via your InGaAs quadrant photodiode sensor array, verify the tracking voltages follow the target limits below:
- **Baseline Carrier Track State (No Modification):** $V_{\text{sum}} \approx 4.5\text{ V}$
- **Active Phase Cancellation State (Maximum Suppression):** $V_{\text{sum}} \le 0.005\text{ V}$ (Absolute Dead Zone Target Reached)
