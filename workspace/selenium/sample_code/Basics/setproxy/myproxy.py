from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "ip_addr:port"
proxy.socks_proxy = "ip_addr:port"
proxy.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)