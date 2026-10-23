#!/usr/bin/env python3
# =====================================================================
#         COGNITIVE FIREWALL SECURITY INTERCEPT LOG PARSER
# =====================================================================
# Audits, sanitizes, and evaluates historical intrusion logs generated
# by the active firewall. Tracks adversarial vector targets.
# =====================================================================

import os
import re
import sys
from datetime import datetime

class SecurityLogParser:
    def __init__(self, log_path="intrusion_defense.log"):
        self.log_path = log_path
        # Precise regex to extract timestamp, true intent, fake decoy, applied illusion, and channel metrics
        self.log_pattern = re.compile(
            r"\[(?P<timestamp>.*?)\] TRAP DEPLOYED \| True State: (?P<true_state>.*?) \| "
            r"Decoy: (?P<decoy>.*?) \| Applied Matrix: (?P<matrix>.*?) \| "
            r"Metrics: X=(?P<x>.*?), Y=(?P<y>.*?), Z=(?P<z>.*?)$"
        )

    def run_security_audit(self):
        """Parses the local file stream to extract core statistical trends and threat analytics."""
        if not os.path.exists(self.log_path):
            print(f"[-] Verification Error: Active log target [{self.log_path}] not found.", file=sys.stderr)
            return

        total_intrusions = 0
        illusion_matrix_counts = {}
        targeted_memory_cores = 0
        channel_vectors = {"X": [], "Y": [], "Z": []}

        print(f"[*] Parsing security telemetry profiles from: {self.log_path}\n")

        try:
            with open(self.log_path, "r") as log_file:
                for line in log_file:
                    line = line.strip()
                    match = self.log_pattern.search(line)
                    if match:
                        total_intrusions += 1
                        data = match.groupdict()
                        
                        # Track matrix usage distribution profiles
                        matrix = data["matrix"].strip()
                        illusion_matrix_counts[matrix] = illusion_matrix_counts.get(matrix, 0) + 1
                        
                        # Track severe attempts specifically aimed at accessing RESTRICTED_MEMORY cores
                        if data["true_state"] == "RESTRICTED_MEMORY":
                            targeted_memory_cores += 1
                            
                        # Append coordinates to track boundary amplitudes
                        try:
                            channel_vectors["X"].append(float(data["x"]))
                            channel_vectors["Y"].append(float(data["y"]))
                            channel_vectors["Z"].append(float(data["z"]))
                        except ValueError:
                            continue
        except OSError as e:
            print(f"[-] Error reading log file: {e}", file=sys.stderr)
            return

        # Print structured corporate-grade safety evaluation report
        print("=====================================================================")
        print("             COGNITIVE FIREWALL SECURITY INTERCEPT REPORT             ")
        print("=====================================================================")
        print(f"Report Generated On      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Probing Incidents  : {total_intrusions}")
        print(f"Restricted Core Attacks  : {targeted_memory_cores} (Flagged Critical)")
        print("---------------------------------------------------------------------")
        print("Active Deception Matrix Deployments:")
        if illusion_matrix_counts:
            for mat_name, count in illusion_matrix_counts.items():
                percentage = (count / total_intrusions) * 100 if total_intrusions > 0 else 0
                print(f" - {mat_name:<45}: {count} ({percentage:.1f}%)")
        else:
            print(" - No active deception matrix deployments recorded.")
        print("---------------------------------------------------------------------")
        
        if total_intrusions > 0 and len(channel_vectors["X"]) > 0:
            print("Mean Sensor Vector Delta During Deflection:")
            print(f" - Avg Channel X Threshold: {sum(channel_vectors['X'])/len(channel_vectors['X']):.4f} uV")
            print(f" - Avg Channel Y Threshold: {sum(channel_vectors['Y'])/len(channel_vectors['Y']):.4f} uV")
            print(f" - Avg Channel Z Threshold: {sum(channel_vectors['Z'])/len(channel_vectors['Z']):.4f} uV")
        else:
            print("[-] Insufficient baseline data tracking vectors logged for signal profiling.")
        print("=====================================================================\n")

if __name__ == "__main__":
    # If the file does not exist locally yet, create mock records to test script execution loops
    if not os.path.exists("intrusion_defense.log"):
        with open("intrusion_defense.log", "w") as f:
            f.write("=== COGNITIVE FIREWALL SYSTEM ENGAGED ===\n")
            f.write("[2026-10-23 04:15:22] TRAP DEPLOYED | True State: RESTRICTED_MEMORY | Decoy: MOTOR_PLAN_LEFT | Applied Matrix: Cornsweet / Adelson Shadow (Contrast) | Metrics: X=6.42, Y=-2.11, Z=0.88\n")
            f.write("[2026-10-23 04:32:01] TRAP DEPLOYED | True State: MOTOR_PLAN_RIGHT | Decoy: IDLE_STATE | Applied Matrix: Troxler Fading / Lilac Chaser (Temporal) | Metrics: X=1.05, Y=6.12, Z=-4.32\n")
            f.write("[2026-10-23 04:55:10] TRAP DEPLOYED | True State: RESTRICTED_MEMORY | Decoy: MOTOR_PLAN_RIGHT | Applied Matrix: Penrose Triangle / Mario Staircase (Spatial) | Metrics: X=7.11, Y=0.95, Z=6.55\n")

    parser = SecurityLogParser()
    parser.run_security_audit()
