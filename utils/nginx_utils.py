import os
from utils import apt_utils

def write_config(server_names, proxy_pass_port):
    # Load the template from file
    with open(os.path.join(os.path.dirname(__file__), 'templates', 'nginx_default.txt'), 'r') as f:
        template = f.read()

    result = template.replace("{server_names}"," ".join(server_names))
    result = result.replace("{proxy_pass_port}",str(proxy_pass_port))

    return result

def output_config(path, server_names, proxy_pass_port):
    config_content = write_config(server_names, proxy_pass_port)
    output_path = os.path.join(path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(config_content)
    print(f"Nginx configuration file saved to: {output_path}")

def get_common_domain_variations(domain_without_prefix):
    return [domain_without_prefix,f"www.{domain_without_prefix}"]

def get_standard_config_filename(domain_id):
    return f"{id}.nginxconf"

#nginx has weird performanced on ubuntu 22 and needs to be uninstalled then reinstalled
def install_nginx_with_hack_for_ubuntu22LTS():
    apt_utils.set_installed('nginx',True)
    apt_utils.set_installed('nginx',False)
    apt_utils.update()
    apt_utils.set_installed('nginx',True)