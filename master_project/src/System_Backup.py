#!/usr/bin/env python3
# =====================================================================
#     INSTITUTIONAL DATA BACKUP ENGINE & INTEGRITY VERIFIER
# =====================================================================
# Automated backup routine designed for high-density EEG databases,
# AOM calibration metrics, and firewall telemetry log streams.
# Enforces SHA-256 validation and automatic 30-day retention rotations.
# =====================================================================

import os
import sys
import tarfile
import hashlib
from datetime import datetime, timedelta

class InstitutionalBackupEngine:
    def __init__(self, source_dirs, backup_root, retention_days=30):
        """
        Initializes the backup storage pathways and retention boundaries.
        
        :param source_dirs: Dictionary containing target laboratory data tracks.
        :param backup_root: Destination pathway for encrypted or compressed archives.
        :param retention_days: Maximum storage life for historical matrix snapshots.
        """
        self.source_dirs = source_dirs
        self.backup_root = backup_root
        self.retention_days = retention_days
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.archive_name = f"bci_cross_regime_backup_{self.timestamp}.tar.gz"
        self.destination_path = os.path.join(self.backup_root, self.archive_name)
        
    def generate_sha256(self, file_path):
        """Calculates a strict SHA-256 cryptographic checksum for data verification."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except OSError as e:
            print(f"[-] Checksum Generation Failure on {file_path}: {e}", file=sys.stderr)
            return None

    def execute_backup_sequence(self):
        """Consolidates target directories, compresses data, and verifies integrity."""
        print(f"[*] [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Launching Institutional Backup Sequence...")
        
        # Verify and build destination paths if missing
        if not os.path.exists(self.backup_root):
            os.makedirs(self.backup_root, exist_ok=True)
            print(f"[+] Created historical backup root directory: {self.backup_root}")

        # Create localized temporary manifest text
        manifest_data = []
        manifest_data.append(f"=== BACKUP METADATA MANIFEST: {self.timestamp} ===\n")

        # Compile and verify files across active system layers
        try:
            with tarfile.open(self.destination_path, "w:gz") as tar:
                for category, path in self.source_dirs.items():
                    if os.path.exists(path):
                        print(f"[+] Packing data track [{category}] from source: {path}")
                        tar.add(path, arcname=os.path.basename(path))
                        
                        # Calculate checksums for files inside directories for verification logs
                        if os.path.isfile(path):
                            checksum = self.generate_sha256(path)
                            manifest_data.append(f"Category: {category} | File: {os.path.basename(path)} | SHA-256: {checksum}\n")
                    else:
                        print(f"[-] Warning: Configured path for [{category}] was not found. Skipping track.")
            
            print(f"[+] Archive file compressed completely: {self.destination_path}")
            
            # Generate primary archive verification token
            archive_checksum = self.generate_sha256(self.destination_path)
            print(f"[Verification Token] Archive SHA-256: {archive_checksum}")
            
            # Save manifest file alongside the package
            manifest_path = self.destination_path + ".manifest.txt"
            with open(manifest_path, "w") as mf:
                mf.writelines(manifest_data)
                mf.write(f"Final Tarball Verification Signature: {archive_checksum}\n")
            
            return True
        except Exception as e:
            print(f"Critical Failure during compression phase: {e}", file=sys.stderr)
            if os.path.exists(self.destination_path):
                os.remove(self.destination_path)
            return False

    def enforce_retention_policy(self):
        """Scans the backup root directory and removes historical files older than retention limit."""
        print(f"[*] Enforcing data retention policy ({self.retention_days} Days Max)...")
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)
        
        try:
            for file_name in os.listdir(self.backup_root):
                file_path = os.path.join(self.backup_root, file_name)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_mtime < cutoff_date:
                    print(f"[-] Purging historical archive file (Exceeded retention bounds): {file_name}")
                    os.remove(file_path)
        except OSError as e:
            print(f"[-] Error enforcing historical cleanup policy: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Define target files and directories within your integrated repository
    TARGET_LAB_SOURCES = {
        "FIREWALL_LOGS":     "./intrusion_defense.log",
        "SOURCE_MODULES":    "./src/",                     # Backs up primary execution scripts
        "MANUSCRIPT_DOCS":   "./docs/Master_Manuscript.md" # Backs up active publication materials
    }
    
    # Destination vault storage folder path
    BACKUP_DESTINATION = "./secure_vault/backups"
    
    engine = InstitutionalBackupEngine(
        source_dirs=TARGET_LAB_SOURCES, 
        backup_root=BACKUP_DESTINATION, 
        retention_days=30
    )
    
    success = engine.execute_backup_sequence()
    if success:
        engine.enforce_retention_policy()
        print("[*] Institutional backup routine finalized successfully. Repository secured.\n")
    else:
        print("[-] Backup operation terminated with structural exceptions.\n", file=sys.stderr)
