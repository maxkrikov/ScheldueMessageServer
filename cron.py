import threading

from crontab import CronTab
import subprocess
from base import PostgresConnector


async def cros(id: str) -> None:
    all_element = PostgresConnector().get_data_by_id(int(id))
    if not all_element:
        return None
    date = all_element[3]

    with CronTab(user='root') as cron:
        job = cron.new(command=f'curl http://localhost:8000/send_message?id={id}')
        job.setall(date)
        cron.write()
    threading.Thread(target=restart_cron).start()
    return True


def restart_cron():
    try:
        # Выполняем команду для перезапуска службы cron
        subprocess.run(['service', 'cron', 'restart'])
    except subprocess.CalledProcessError as e:
        print(f"Cron restart Error: {e}")
