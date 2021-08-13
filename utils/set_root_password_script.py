def set_root_password_script(password: str):
    return '#!/bin/bash\n' \
           f'echo root:{password} | sudo chpasswd root\n' \
           'sudo sed -i "s/^.*PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config\n' \
           'sudo sed -i "s/^.*PasswordAuthentication.*/PasswordAuthentication yes/g" /etc/ssh/sshd_config\n' \
           'sudo systemctl restart sshd\n'
