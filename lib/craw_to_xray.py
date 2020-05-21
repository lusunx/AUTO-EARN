import sqlite3
import subprocess
from lib import config
from rich.console import Console

console = Console()


# 爬虫爬取并且发送到XRAY
def craw_to_xray(domain_list):
    console.print('正在进行爬虫探测+漏洞检测',style="#ADFF2F")
    console.print('任务数据库连接成功',style="#ADFF2F")
    conn = sqlite3.connect(config.result_sql_path)
    c = conn.cursor()
    for domain in domain_list:
        domain = domain[1]
        # cmd = [config.crawlergo_path, "-c", config.chrome_path,"-t",config.max_tab_count, "-f", "smart", "--fuzz-path", "--push-to-proxy",config.push_to_proxy,  "--push-pool-max", config.max_send_count, domain]
        cmd = "nohup " + config.crawlergo_path + " -c " + config.chrome_path + " -t " + config.max_tab_count + " -f " + " smart " + " --fuzz-path " + " --push-to-proxy " + config.push_to_proxy + " --push-pool-max " + config.max_send_count + " " + domain + " > logs/crawlergo.log 2>&1 &"
        rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            if rsp.poll() == None:
                pass
            else:
                break