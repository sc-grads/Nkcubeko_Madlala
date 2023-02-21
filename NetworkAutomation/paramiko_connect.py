import paramiko
from scp import SCPClient
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh_client.connect(hostname='10.1.1.10', port= '22', username='v1', password='cisco' look_for_keys=False, allow_agent=False)
# print(ssh_client.get_transport().is_active())
#
# scp = SCPClient(ssh_client.get_transport())
#
# scp.put('dictionary1', recursive=True, remote_path='/tmp')
#
# scp.get('/etc/passwd', 'passwd')
# scp.close()



















