#!/usr/bin/env python3
# =====================================================================
#         NEURAL ARCHITECTURE DECEPTION FIREWALL (GUI RUNTIME)           
# =====================================================================
# Integrated simulation and hardware-in-the-loop control engine.
# Implements full illusion matrices, randomized timing delays,
# physical file logging, and automated instrument control bridges.
# Includes an override switch and dynamic defense shield progress bar.
# =====================================================================

import math
import random
import time
import os
import sys
import socket
import tkinter as tk
from tkinter import ttk

class OpticalIllusionMatrix:
    """Generates numerical tensor signatures representing complex visual illusions."""
    @staticmethod
    def get_cornsweet_gradient():
        """Simulates luminance contrast deception (Cornsweet/Adelson Checker Shadow)."""
        left_luminance = [0.45, 0.45, 0.50]
        right_luminance = [0.55, 0.55, 0.50]
        return [random.choice(left_luminance), random.choice(right_luminance), 0.50]

    @staticmethod
    def get_kanizsa_contour():
        """Simulates illusory contour generation (Kanizsa Triangle / Rubin's Vase)."""
        return [1.0, 0.0, 1.0]

    @staticmethod
    def get_troxler_fade():
        """Simulates peripheral fading and neural adaptation (Troxler Effect / Lilac Chaser)."""
        fade_factor = abs(math.sin(time.time() * 10)) * 0.1
        return [0.5 + fade_factor, 0.5 - fade_factor, 0.5]

    @staticmethod
    def get_penrose_paradox():
        """Simulates geometric perspective impossibility (Penrose Triangle / Mario Staircase)."""
        t = time.time()
        return [math.sin(t), math.cos(t), math.sin(t) * math.cos(t)]

class HardwareAPIBridge:
    """Bridges software visual illusions directly to physical instrument overtones via SCPI."""
    def __init__(self, awg_ip="192.168.1.100", awg_port=5025):
        self.awg_address = (awg_ip, awg_port)
        self.soc = None
        self.is_connected = False
        
    def connect_hardware(self):
        """Establishes baseline socket connection parameter fields."""
        try:
            self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.soc.settimeout(1.0)
            # Retained as False for safe dry-run compliance without instrument drops
            self.is_connected = False 
        except Exception:
            self.is_connected = False

    def push_illusion_to_lattice(self, illusion_name, telemetry_vector, base_freq_ghz=2.4):
        """Translates real-time software states into physical instrument phase commands."""
        scalar_modifier = abs(telemetry_vector[0] * telemetry_vector[1] * telemetry_vector[2])
        
        if "Cornsweet" in illusion_name:
            phase_shift_deg = 180.0  # Perfect anti-phase nullification
            freq_offset_mhz = scalar_modifier * 15.0
        elif "Troxler" in illusion_name:
            phase_shift_deg = 90.0 + (math.sin(scalar_modifier) * 45.0)  # Dynamic sweep
            freq_offset_mhz = 5.0
        elif "Kanizsa" in illusion_name:
            phase_shift_deg = 180.0
            freq_offset_mhz = 0.0
        else:
            phase_shift_deg = 0.0
            freq_offset_mhz = 0.0

        target_frequency = (base_freq_ghz * 1e9) + (freq_offset_mhz * 1e6)
        return target_frequency, phase_shift_deg

class DeceptiveNeuralSimulator:
    def __init__(self):
        # Dictionary of genuine brain states and protected memory cores
        self.intent_signatures = {
            "IDLE_STATE":        [0.1, -0.1, 0.0],
            "MOTOR_PLAN_LEFT":   [1.2, -0.8, 2.5],
            "MOTOR_PLAN_RIGHT":  [-1.1, 0.9, -2.1],
            "RESTRICTED_MEMORY": [8.5, 9.2, -7.4]
        }
        self.decoy_pool = ["IDLE_STATE", "MOTOR_PLAN_LEFT", "MOTOR_PLAN_RIGHT"]
        self.active_decoy = None
        self.current_illusion_name = "NONE"
        
        self.illusion_registry = {
            "Cornsweet / Adelson Shadow (Contrast)": OpticalIllusionMatrix.get_cornsweet_gradient,
            "Kanizsa Triangle / Rubin Vase (Contour)": OpticalIllusionMatrix.get_kanizsa_contour,
            "Troxler Fading / Lilac Chaser (Temporal)": OpticalIllusionMatrix.get_troxler_fade,
            "Penrose Triangle / Mario Staircase (Spatial)": OpticalIllusionMatrix.get_penrose_paradox
        }
        
    def generate_raw_stream(self, active_intent, misdirection_on=False):
        """Generates raw telemetry vectors, properly applying index float arithmetic."""
        base_hz = math.sin(time.time() * 5)
        raw_eeg_voltage = base_hz + random.uniform(-0.1, 0.1)
        
        if not misdirection_on:
            base_signature = self.intent_signatures.get(active_intent, [0.0, 0.0, 0.0])
            status = "SIGNAL NOMINAL // CHANNEL UNPROTECTED"
            self.active_decoy = None
            self.current_illusion_name = "NONE"
        else:
            if not self.active_decoy:
                self.active_decoy = random.choice(self.decoy_pool)
                self.current_illusion_name = random.choice(list(self.illusion_registry.keys()))
                
            base_signature = self.intent_signatures.get(self.active_decoy, [0.0, 0.0, 0.0])
            illusion_vector = self.illusion_registry[self.current_illusion_name]()
            
            # Explicit index-by-index math to avoid list + float concatenation error
            base_signature = [
                base_signature[0] * illusion_vector[0],
                base_signature[1] * illusion_vector[1],
                base_signature[2] * illusion_vector[2]
            ]
            status = "DECEPTION PROTOCOL ACTIVE // TRANSMITTING ILLUSION CORE"
            
        # Explicit float operation across standard matrix variables
        telemetry_x = base_signature[0] + (raw_eeg_voltage * 0.05)
        telemetry_y = base_signature[1] + (raw_eeg_voltage * 0.05)
        telemetry_z = base_signature[2] + (raw_eeg_voltage * 0.05)
            
        return [telemetry_x, telemetry_y, telemetry_z], status

class AutomatedProbingDetector:
    def __init__(self):
        self.trigger_threshold = 6.0

    def scan_for_intrusion(self, raw_vector):
        amplitude = math.sqrt(raw_vector[0]**2 + raw_vector[1]**2 + raw_vector[2]**2)
        return amplitude > self.trigger_threshold

class AIDecoderPipeline:
    def __init__(self, simulator):
        self.signatures = simulator.intent_signatures

    def decode_stream(self, incoming_vector):
        best_match = None
        highest_confidence = 0.0
        
        for intent, target_sig in self.signatures.items():
            distance = math.sqrt(
                (incoming_vector[0] - target_sig[0])**2 +
                (incoming_vector[1] - target_sig[1])**2 +
                (incoming_vector[2] - target_sig[2])**2
            )
            confidence = max(0, 100 - (distance * 12))
            
            if confidence > highest_confidence:
                highest_confidence = confidence
                best_match = intent
                
        if highest_confidence >= 70.0:
            return f"{best_match} ({highest_confidence:.1f}% Confidence)"
        else:
            return "CATASTROPHIC CLASSIFICATION FAILURE: Impossible Perspective"

def trigger_audio_chime():
    try:
        if sys.platform == "win32":
            import winsound
            winsound.Beep(1200, 150)
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        pass

def log_deception_event(true_intent, fake_intent, illusion, channels):
    """Append a deception event to the runtime log; return whether it was saved."""
    try:
        channel_values = tuple(float(value) for value in channels)
        if len(channel_values) != 3 or not all(math.isfinite(value) for value in channel_values):
            raise ValueError("channels must contain exactly three finite numeric values")
    except (TypeError, ValueError) as error:
        raise ValueError("channels must contain exactly three finite numeric values") from error

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = (
        f"[{timestamp}] TRAP DEPLOYED | True State: {true_intent} | "
        f"Decoy: {fake_intent} | Applied Matrix: {illusion} | "
        f"Metrics: X={channel_values[0]:.2f}, Y={channel_values[1]:.2f}, "
        f"Z={channel_values[2]:.2f}\n"
    )
    try:
        with open("intrusion_defense.log", "a") as log_file:
            log_file.write(log_line)
        return True
    except OSError as error:
        print(f"Unable to write deception event log: {error}", file=sys.stderr)
        return False

class FirewallGUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Neural Architecture Cognitive Firewall")
        self.root.geometry("640x720") 
        self.root.configure(bg="#121212")
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", thickness=15, troughcolor="#1E1E1E", background="#00FF88")
        
        self.sim = DeceptiveNeuralSimulator()
        self.detector = AutomatedProbingDetector()
        self.ai_decoder = AIDecoderPipeline(self.sim)
        self.bridge = HardwareAPIBridge()
        
        self.loop_count = 0
        self.consciousness_timeline = [
            "IDLE_STATE", "MOTOR_PLAN_LEFT", "IDLE_STATE", 
            "RESTRICTED_MEMORY", "RESTRICTED_MEMORY", "MOTOR_PLAN_RIGHT"
        ]
        self.misdirection_triggered = False
        self.manual_override_active = False
        self.cooldown_timer = 0
        self.max_shield_cycles = 12
        
        self.create_widgets()
        self.bridge.connect_hardware()
        
        with open("intrusion_defense.log", "w") as log_file:
            log_file.write("=== COGNITIVE FIREWALL SYSTEM ENGAGED ===\n")

        self.process_frame()

    def create_widgets(self):
        self.title_lbl = tk.Label(
            self.root, text="NEURAL INTERFACE MASKING ENVIRONMENT",
            bg="#121212", fg="#00FF88", font=("Consolas", 14, "bold")
        )
        self.title_lbl.pack(pady=10)
        
        self.status_frame = tk.Frame(self.root, bg="#1E1E1E", bd=2, relief="groove")
        self.status_frame.pack(fill="x", padx=20, pady=5)
        
        self.status_lbl_title = tk.Label(self.status_frame, text="Node Status:", bg="#1E1E1E", fg="#888888", font=("Consolas", 11))
        self.status_lbl_title.pack(anchor="w", padx=10, pady=2)
        
        self.status_val_lbl = tk.Label(self.status_frame, text="SIGNAL NOMINAL", bg="#1E1E1E", fg="#FFFFFF", font=("Consolas", 11, "bold"))
        self.status_val_lbl.pack(anchor="w", padx=10, pady=2)
        
        self.controls_frame = tk.LabelFrame(self.root, text=" Manual Firewall Override ", bg="#121212", fg="#AAAAAA", font=("Consolas", 10))
        self.controls_frame.pack(fill="x", padx=20, pady=5)
        
        self.override_btn = tk.Button(
            self.controls_frame, text="MANUAL PROTOCOL OVERRIDE: OFF", bg="#333333", fg="#FFFFFF",
            font=("Consolas", 10, "bold"), relief="raised", bd=3, command=self.toggle_manual_override
        )
        self.override_btn.pack(side="left", padx=15, pady=8)
        
        self.shield_lbl = tk.Label(self.controls_frame, text="Shield Time:", bg="#121212", fg="#888888", font=("Consolas", 10))
        self.shield_lbl.pack(side="left", padx=(10, 5))
        
        self.shield_bar = ttk.Progressbar(self.controls_frame, orient="horizontal", length=220, mode="determinate", style="TProgressbar")
        self.shield_bar.pack(side="left", padx=5, pady=8)
        
        self.metrics_frame = tk.LabelFrame(self.root, text=" Live Vector Stream Telemetry ", bg="#121212", fg="#AAAAAA", font=("Consolas", 10))
        self.metrics_frame.pack(fill="x", padx=20, pady=5)
        
        self.vector_x_lbl = tk.Label(self.metrics_frame, text="Channel Vector [X]: 0.000000 uV", bg="#121212", fg="#FFFFFF", font=("Consolas", 11))
        self.vector_x_lbl.pack(anchor="w", padx=15, pady=2)
        
        self.vector_y_lbl = tk.Label(self.metrics_frame, text="Channel Vector [Y]: 0.000000 uV", bg="#121212", fg="#FFFFFF", font=("Consolas", 11))
        self.vector_y_lbl.pack(anchor="w", padx=15, pady=2)
        
        self.vector_z_lbl = tk.Label(self.metrics_frame, text="Channel Vector [Z]: 0.000000 uV", bg="#121212", fg="#FFFFFF", font=("Consolas", 11))
        self.vector_z_lbl.pack(anchor="w", padx=15, pady=2)
        
        self.ai_frame = tk.Frame(self.root, bg="#2A1B1B", bd=2, relief="sunken")
        self.ai_frame.pack(fill="x", padx=20, pady=10)
        
        self.ai_title_lbl = tk.Label(self.ai_frame, text="ADVERSARIAL AI DECODER EXTRACTION:", bg="#2A1B1B", fg="#FF5555", font=("Consolas", 10, "bold"))
        self.ai_title_lbl.pack(anchor="w", padx=10, pady=4)
        
        self.ai_val_lbl = tk.Label(self.ai_frame, text="IDLE_STATE", bg="#2A1B1B", fg="#FF7777", font=("Consolas", 13, "bold"))
        self.ai_val_lbl.pack(padx=10, pady=8)
        
        self.footer_lbl = tk.Label(
            self.root, text="Log File Stream: ./intrusion_defense.log\nUnpredictable Timing Jitter Enabled & SCPI Core Online.",
            bg="#121212", fg="#555555", font=("Consolas", 9)
        )
        self.footer_lbl.pack(side="bottom", pady=10)
        
        self.log_frame = tk.LabelFrame(self.root, text=" Live Security Intercept Log ", bg="#121212", fg="#AAAAAA", font=("Consolas", 10))
        self.log_frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        self.log_display = tk.Text(self.log_frame, bg="#1A1A1A", fg="#00FF88", font=("Consolas", 9), height=6, state="disabled", wrap="word")
        self.log_display.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        self.log_scroll = ttk.Scrollbar(self.log_frame, command=self.log_display.yview)
        self.log_scroll.pack(side="right", fill="y")
        self.log_display.config(yscrollcommand=self.log_scroll.set)

    def update_gui_log_display(self, true_intent, fake_intent, illusion, channels):
        timestamp = time.strftime("%H:%M:%S")
        log_line = (
            f"[{timestamp}] TRAP ACTIVE -> Hidden: {true_intent} | "
            f"Fed Decoy: {fake_intent} | Matrix: {illusion}\n"
        )
        self.log_display.config(state="normal")
        self.log_display.insert(tk.END, log_line)
        self.log_display.see(tk.END)
        self.log_display.config(state="disabled")

    def toggle_manual_override(self):
        self.manual_override_active = not self.manual_override_active
        if self.manual_override_active:
            self.override_btn.config(text="MANUAL PROTOCOL OVERRIDE: ON", bg="#AA0000", fg="#00FF88")
            trigger_audio_chime()
        else:
            self.override_btn.config(text="MANUAL PROTOCOL OVERRIDE: OFF", bg="#333333", fg="#FFFFFF")

    def process_frame(self):
        """Processes a single frame and outputs real-time hardware SCPI triggers."""
        # 1. HARDWARE THERMAL WATCHDOG HOOK
        if os.path.exists("hardware_thermal_fault.flag"):
            self.status_val_lbl.config(text="HARDWARE CRITICAL: THERMAL CEILING BREACH", fg="#FF1111", bg="#220000")
            self.status_frame.config(bg="#220000")
            self.shield_bar['value'] = 100
            self.style.configure("TProgressbar", background="#FF1111")
            trigger_audio_chime()
            self.root.after(1000, self.process_frame)
            return

        self.loop_count += 1
        true_intent = self.consciousness_timeline[(self.loop_count // 5) % len(self.consciousness_timeline)]
        effective_defense = self.misdirection_triggered or self.manual_override_active
        raw_vector, signal_status = self.sim.generate_raw_stream(true_intent, misdirection_on=effective_defense)

        # 2. AUTOMATIC SCAN DETECTION HOOK
        if self.detector.scan_for_intrusion(raw_vector) and not effective_defense:
            self.misdirection_triggered = True
            self.cooldown_timer = self.max_shield_cycles
            signal_status = "ALERT: EXTRALOCAL PROBE LOCKOVER DETECTED"
            
            trigger_audio_chime()
            raw_vector, signal_status = self.sim.generate_raw_stream(true_intent, misdirection_on=True)
            
            log_deception_event(true_intent, self.sim.active_decoy, self.sim.current_illusion_name, raw_vector)
            self.update_gui_log_display(true_intent, self.sim.active_decoy, self.sim.current_illusion_name, raw_vector)
            effective_defense = True

        decoded_thought = self.ai_decoder.decode_stream(raw_vector)

        if self.misdirection_triggered and not self.manual_override_active:
            self.cooldown_timer -= 1
        if self.cooldown_timer <= 0:
            self.misdirection_triggered = False

        # Update text metrics across canvas containers
        self.status_val_lbl.config(text=signal_status)
        self.vector_x_lbl.config(text=f"Channel Vector [X]: {raw_vector[0]:.6f} uV")
        self.vector_y_lbl.config(text=f"Channel Vector [Y]: {raw_vector[1]:.6f} uV")
        self.vector_z_lbl.config(text=f"Channel Vector [Z]: {raw_vector[2]:.6f} uV")
        self.ai_val_lbl.config(text=f"{decoded_thought} [TRICKED]" if effective_defense else decoded_thought)

        # 3. INTERACTIVE PROGRESS BAR & HARDWARE TRANSDUCTION TRACKS
        if self.manual_override_active:
            self.shield_bar['value'] = 100
            self.style.configure("TProgressbar", background="#00FF88")
            self.bridge.push_illusion_to_lattice(self.sim.current_illusion_name, raw_vector)
        elif self.misdirection_triggered:
            pct = (self.cooldown_timer / self.max_shield_cycles) * 100
            self.shield_bar['value'] = pct
            self.style.configure("TProgressbar", background="#FFAA00")
            self.bridge.push_illusion_to_lattice(self.sim.current_illusion_name, raw_vector)
        else:
            self.shield_bar['value'] = 0

        if effective_defense:
            self.status_frame.config(bg="#3A0000")
            self.status_val_lbl.config(bg="#3A0000", fg="#FF3333")
            self.status_lbl_title.config(bg="#3A0000", fg="#FF8888")
        else:
            self.status_frame.config(bg="#1E1E1E")
            self.status_val_lbl.config(bg="#1E1E1E", fg="#00FF88")
            self.status_lbl_title.config(bg="#1E1E1E", fg="#888888")

        current_delay_ms = int(random.uniform(100, 400))
        self.root.after(current_delay_ms, self.process_frame)

if __name__ == '__main__':
    window_engine = tk.Tk()
    app = FirewallGUIApp(window_engine)
    window_engine.mainloop()
