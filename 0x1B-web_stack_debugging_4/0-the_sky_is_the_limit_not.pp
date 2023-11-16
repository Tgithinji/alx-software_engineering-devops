# Increase ULIMIT

exec { 'nginx_ulimit':
  command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  notify  => Exec['nginx_restart'],
}

exec { 'nginx_restart':
  command => '/usr/sbin/service nginx restart',
}
