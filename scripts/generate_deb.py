import os

package_name = 'piculator-client'
name = 'piculator-client'
desp = 'client (main app) for piculator'
version = input('Please input version:')
package_path = f'{package_name}_{version}'
files_path = f'{package_path}/opt/piculator-client/'
os.makedirs(files_path, exist_ok=True)
os.system(f'cp -r ../src/** {files_path}')
os.system(f'cp piculator-client {package_path}/usr/bin/piculator-client')
os.system(f'cp preinst.sh {package_path}/DEBIAN/preinst')
os.system(f'cp prerm.sh {package_path}/DEBIAN/prerm')
os.system(f'cp postinst.sh {package_path}/DEBIAN/postinst')
os.system(f'cp postrm.sh {package_path}/DEBIAN/postrm')
os.makedirs(f"{package_path}/DEBIAN", exist_ok=True)
control_content = f'''Package: {package_name}
Architecture: all
Name: {name}
Description: {desp}
Version: {version}
Section: base
Depends: python3-pyqt5.qtwebkit, python3-pyqt5, python3-jupyter-console, python3-bluez
Author: Piculator Development Team <piculator@protonmail.com>
Maintainer: Piculator Development Team <piculator@protonmail.com>
HomePage: https://github.com/piculator/{package_name}-software
'''
ctl_file = open(f'{package_path}/DEBIAN/control', mode='w+')
ctl_file.write(control_content)
ctl_file.close()
for r, d, f in os.walk(package_path):
    os.chmod(r, 0o755)
os.system(f'dpkg-deb -b {package_path}')
