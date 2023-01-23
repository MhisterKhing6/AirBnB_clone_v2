#Setup a server for the release
exec { 'install ':
  command =>'apt update -y; apt install nginx -y' ,
  path    => ['/usr/bin', '/usr/sbin']
}

exec {'create the folder':
    command => 'mkdir -p /data/web_static/releases/test/; mkdir -p /data/web_static/shared/',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell
}

exec {'create text content of index.html':
    command => 'echo "<h1>Test me</h1>" > /data/web_static/releases/test/index.html',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell
}


exec {'create a symbolic link to test folder':
    command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell

}


exec {'setup the users permisson':
    command => 'chown -Rh ubuntu:ubuntu /data/',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell
}

exec {'setup nginx server':
    command => 'sed -i "/^server {$/a\    location \/hbnb_static {\n\t\talias /data/web_static/current;\n}" /etc/nginx/sites-available/default',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell
}

exec {'restart the nginx server':
    command => 'service nginx restart',
    path    => ['/usr/bin', '/usr/sbin'],
    provider => shell
}
