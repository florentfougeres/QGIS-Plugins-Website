from celery import shared_task
import subprocess
import os

@shared_task
def run_qgis_script(plugin_path: str):
    script_path = "/usr/local/bin/pyqt5_to_pyqt6.py"
    log_file = "/web/shared/script.log"

    command = [script_path, plugin_path, "--dry_run"]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        logs = result.stdout.decode() + result.stderr.decode()
        print(logs)
        return logs
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution du script : {e.stderr.decode()}"