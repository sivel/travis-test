from ansible.module_utils.urls import SSLValidationHandler
import os

s = SSLValidationHandler('sh.rustup.rs', 443)
a, _, c = s.get_ca_certs()
print(open(a).read())

for path in c:
    if os.path.exists(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                if os.path.isfile(full_path) and os.path.splitext(full_path)[1] in ('.crt','.pem'):
                    print(full_path)
