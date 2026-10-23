#!/usr/bin/env bash
# =====================================================================
#       CROSS-REGIME INFRASTRUCTURE TERMINAL ALIAS PROFILE
# =====================================================================
# Binds complex multi-directory commands into rapid laboratory keywords.
# To activate, run the following command in your console terminal:
# source bci_aliases.sh
# =====================================================================

# Define absolute base path to your master workspace directory
export BCI_PROJECT_ROOT="/home/lab-user/master_project"

# 1. NAVIGATION ALIAS
alias bci-cd="cd \$BCI_PROJECT_ROOT"

# 2. RUNTIME WORKLOAD COMMANDS
# Starts the background thermal watchdog breaker as a detached process
alias bci-watch="python3 \$BCI_PROJECT_ROOT/src/Thermal_Watcher.py"

# Launches the main integrated Tkinter runtime user interface environment
alias bci-gui="python3 \$BCI_PROJECT_ROOT/src/optical_illusion_matrix_GUI.py"

# 3. FORENSICS & SECURITY MAINTENANCE COMMANDS
# Parses the active local text logs and prints a structured threat audit report
alias bci-audit="python3 \$BCI_PROJECT_ROOT/src/Diagnostic_Audit.py"

# Tails the live security log file stream to view adversarial trap entries in real time
alias bci-log="tail -f \$BCI_PROJECT_ROOT/intrusion_defense.log"

# 4. DISASTER RECOVERY & SYSTEM MAINTENANCE ALIASES
# Flushes stale emergency interlock flag files to unlock the Tkinter runtime engine
alias bci-flush="rm -f \$BCI_PROJECT_ROOT/hardware_thermal_fault.flag && echo '[+] Thermal interlock flag file purged.'"

# Forces an immediate cryptographic data backup archive compression sequence
alias bci-backup="python3 \$BCI_PROJECT_ROOT/src/System_Backup.py"

# 5. ALL-IN-ONE MASTER CONTROL MATRIX
# Combined alias that flushes old flags, spins up the thermal guard, and opens the GUI console
alias bci-launch-all="rm -f \$BCI_PROJECT_ROOT/hardware_thermal_fault.flag && \
                      python3 \$BCI_PROJECT_ROOT/src/Thermal_Watcher.py > /dev/null 2>&1 & \
                      python3 \$BCI_PROJECT_ROOT/src/optical_illusion_matrix_GUI.py && \
                      kill \$(pgrep -f Thermal_Watcher.py) 2>/dev/null"

# Print operational menu panel on initialization
echo "====================================================================="
echo "   🛡️  CROSS-REGIME COGNITIVE SYSTEM TERMINAL SHORTCUTS LOADED  🛡️   "
echo "====================================================================="
echo "  bci-cd         : Navigate directly to master workspace root folder"
echo "  bci-watch      : Launch background thermal watchdog circuit breaker"
echo "  bci-gui        : Launch core Tkinter user interface application"
echo "  bci-audit      : Parse intrusion_defense.log for security threat metrics"
echo "  bci-log        : Tail the live security intercept log data stream"
echo "  bci-flush      : Purge stale hardware lock flags after a cold boot"
echo "  bci-backup     : Execute tarball data backup archive compression"
echo "  bci-launch-all : All-in-one execution (Purge, watch, and run GUI)"
echo "====================================================================="
